package org.smarttrust.demo.app

import who.smart.trust.HcertResult
import who.smart.trust.core.DEFAULT_LIMITS
import who.smart.trust.core.HcertTrustStore
import who.smart.trust.core.HcertVerifier
import who.smart.trust.core.SubclaimRegistry
import who.smart.trust.payloads.Payload
import who.smart.trust.verifier.VerificationResult
import who.smart.trust.verifier.VerifierOptions

/**
 * The journeys on the Kotlin HCERT library's JVM jars. [read] loads a file
 * of the guide's example (assets on a device, files in a unit test).
 * The trust store is loaded once, before any visit: XXR's DSC DID document
 * from the GDHCN DEV trust list, as the clinic's last refresh left it (J3's
 * precondition). Verifying fetches nothing.
 */
class AndroidHcertJourneys(private val read: (String) -> String, private val now: () -> Long) : HcertJourneys {
    private val reg = SubclaimRegistry()
    private val options = VerifierOptions(DEFAULT_LIMITS, clockSkewSeconds = 300)
    private val store by lazy { HcertTrustStore().apply { addDidDocument(read("XXR-DSC-did.json")) } }

    override fun examples(): List<Pair<String, String>> {
        val hc1s = Regex("\"hc1\"\\s*:\\s*\"(HC1:[^\"]+)\"").findAll(read("dvc-qr-example-XXR.json")).map { it.groupValues[1] }.toList()
        return listOf("Hep B (birth dose)", "BCG").zip(hc1s)
    }

    override fun readOffline(label: String, hc1: String): DvcView =
        when (val r = HcertVerifier.readUnverified(hc1, reg, DEFAULT_LIMITS)) {
            is HcertResult.Ok -> {
                val p = r.value.entries.firstOrNull()?.payload as? Payload.DvcMin
                val dose = p?.value?.let { Dose(it.n, it.dob, it.vx.vp, it.vx.dv, it.vx.bo) }
                DvcView(label, dose, "Read offline, NOT verified (issuer ${r.value.iss})", null)
            }
            is HcertResult.Err -> DvcView(label, null, "Could not read: ${r.error.step} ${r.error.reason}", null)
        }

    override fun verify(view: DvcView, hc1: String): DvcView =
        when (val r = HcertVerifier.verify(hc1, store, reg, now(), options)) {
            is VerificationResult.Verified -> view.copy(
                verified = "Verified: signed by ${r.value.dsc.country}'s DSC on the trust list",
                signer = Signer(r.value.dsc.kid.joinToString("") { "%02x".format(it) }, r.value.dsc.country),
            )
            is VerificationResult.Failed -> view.copy(verified = "Not verified at ${r.value.step}: ${r.value.reason}")
        }

    override fun import(view: DvcView, index: Int): DvcView {
        val dose = view.dose ?: return view
        val signer = view.signer ?: return view
        // The clinic's own record for the child; matching holder to record is the clinic's step.
        val imported = ImmunizationImport.import(dose, "dvc-${index + 1}", "Patient/chanthala", signer.kidHex, signer.country, now() * 1000)
        return view.copy(imported = ImmunizationImport.toJson(imported))
    }
}
