package org.smarttrust.demo.androidtest

import java.security.KeyFactory
import java.security.PrivateKey
import java.security.Signature
import java.security.spec.MGF1ParameterSpec
import java.security.spec.PKCS8EncodedKeySpec
import java.security.spec.PSSParameterSpec
import java.util.Base64
import org.json.JSONObject
import who.smart.trust.HcertResult
import who.smart.trust.core.DEFAULT_LIMITS
import who.smart.trust.dvc.DvcMin
import who.smart.trust.dvc.DvcMinVaccineDetails
import who.smart.trust.verifier.VerifierOptions

/*
 * What the tests share: the vectors of smart-trust-tools at the commit the
 * jars are built from (assets, from lib/hcert/build/src/vectors/), and the
 * PEM and key handling. Nothing here depends on Android, so the same file
 * compiles on a JVM.
 */

/** Reads a vectors/ file; [asset] is set by the test's instrumentation context. */
lateinit var asset: (String) -> String

val OPTIONS = VerifierOptions(DEFAULT_LIMITS, clockSkewSeconds = 300)

fun <T, E> HcertResult<T, E>.ok(): T = when (this) {
    is HcertResult.Ok -> value
    is HcertResult.Err -> throw AssertionError("expected Ok, got $error")
}

/** The two signed DVCs of the WHO guide's QR Code Generation §12 example (Hep B, BCG), issued by XXR. */
object GuideExample {
    val certificates: JSONObject get() = JSONObject(asset("smart-trust-af75be2/dvc-qr-example-XXR.json")).getJSONObject("certificates")
    val xxrDscDid: String get() = asset("smart-trust-af75be2/XXR-DSC-did.json")
    const val KID_HEX = "916ffa567c0f44a2"
}

/** A DVCMin for a newborn, as the clinic in J1 would issue. Fictional. */
val NEWBORN = DvcMin(
    n = "Test CHILD", dob = "2026-10-21", s = "female", nt = "LAO", gn = "Test MOTHER",
    vx = DvcMinVaccineDetails(vp = "XM9V38", dv = "2026-10-21", `is` = "org-test", bo = "HEPB-TEST"),
    v = "1.0.0", extensions = emptyList(),
)

fun pemBlocks(pem: String, label: String): List<ByteArray> =
    Regex("-----BEGIN $label-----(.*?)-----END $label-----", RegexOption.DOT_MATCHES_ALL)
        .findAll(pem).map { Base64.getMimeDecoder().decode(it.groupValues[1].trim()) }.toList()

fun certificatePem(der: ByteArray): String =
    "-----BEGIN CERTIFICATE-----\n" + Base64.getMimeEncoder(64, "\n".toByteArray()).encodeToString(der) + "\n-----END CERTIFICATE-----\n"

fun hex(b: ByteArray) = b.joinToString("") { "%02x".format(it) }

/** The TEST-ONLY keys of vectors/testkit/, signed with in software on the platform's providers. */
object Testkit {
    val esDsc: ByteArray get() = pemBlocks(asset("testkit/es256-dsc.pem"), "CERTIFICATE").single()
    val psDsc: ByteArray get() = pemBlocks(asset("testkit/ps256-dsc-test-eku.pem"), "CERTIFICATE").single()

    private fun key(file: String, type: String): PrivateKey =
        KeyFactory.getInstance(type).generatePrivate(PKCS8EncodedKeySpec(pemBlocks(asset(file), "PRIVATE KEY").single()))

    fun signEs256(tbs: ByteArray): ByteArray =
        Signature.getInstance("SHA256withECDSA").run { initSign(key("testkit/es256-key.pem", "EC")); update(tbs); sign() }

    /** PS256 under the standard name first, then Android's "SHA256withRSA/PSS" (the open item in docs/plan.md, step 4). */
    fun signPs256(tbs: ByteArray): ByteArray {
        val k = key("testkit/ps256-key.pem", "RSA")
        return try {
            Signature.getInstance("RSASSA-PSS").run {
                setParameter(PSSParameterSpec("SHA-256", "MGF1", MGF1ParameterSpec.SHA256, 32, 1))
                initSign(k); update(tbs); sign()
            }
        } catch (e: java.security.NoSuchAlgorithmException) {
            Signature.getInstance("SHA256withRSA/PSS").run { initSign(k); update(tbs); sign() }
        }
    }
}
