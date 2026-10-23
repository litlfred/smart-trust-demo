package org.smarttrust.demo.androidtest

import android.security.keystore.KeyGenParameterSpec
import android.security.keystore.KeyProperties
import androidx.test.ext.junit.runners.AndroidJUnit4
import androidx.test.platform.app.InstrumentationRegistry
import java.security.KeyPairGenerator
import java.security.KeyStore
import java.security.PrivateKey
import java.security.Signature
import kotlin.test.assertEquals
import kotlin.test.assertIs
import kotlin.test.assertTrue
import org.junit.Before
import org.junit.Test
import org.junit.runner.RunWith
import who.smart.trust.core.DEFAULT_LIMITS
import who.smart.trust.core.HcertIssuer
import who.smart.trust.core.HcertTrustStore
import who.smart.trust.core.HcertVerifier
import who.smart.trust.core.SubclaimRegistry
import who.smart.trust.issuer.IssueRequest
import who.smart.trust.issuer.Validity
import who.smart.trust.payloads.Payload
import who.smart.trust.types.CoseAlgorithm
import who.smart.trust.types.FailureReason
import who.smart.trust.types.Step
import who.smart.trust.verifier.VerificationResult

/**
 * The Kotlin HCERT library on Android, on the platform's own crypto
 * providers (STT-GEN-004): what the journeys J1 to J3 ask of it.
 */
@RunWith(AndroidJUnit4::class)
class HcertOnAndroidTest {
    private val reg = SubclaimRegistry()

    @Before fun assets() {
        val am = InstrumentationRegistry.getInstrumentation().context.assets
        asset = { path -> am.open(path).bufferedReader().use { it.readText() } }
    }

    /** J3: the clinic verifies the guide's two DVCs against XXR's DSC from the DEV trust list. */
    @Test fun guideExampleVerifiesAgainstXxrDsc() {
        val store = HcertTrustStore().apply { assertEquals(1, addDidDocument(GuideExample.xxrDscDid).ok()) }
        val certs = GuideExample.certificates
        for (name in listOf("hepb1", "bcg")) {
            val c = certs.getJSONObject(name)
            val v = assertIs<VerificationResult.Verified>(
                HcertVerifier.verify(c.getString("hc1"), store, reg, c.getLong("iat") + 3600, OPTIONS), name,
            ).value
            assertEquals("XR", v.iss, name)
            assertEquals(GuideExample.KID_HEX, hex(v.dsc.kid), name)
            val p = assertIs<Payload.DvcMin>(v.entries.single().payload, name).value
            assertEquals(c.getJSONObject("payload").getJSONObject("vx").getString("vp"), p.vx.vp, name)
        }
    }

    /** J2: the CHW app reads the same DVCs offline, with no trust list (STT-VER-011). */
    @Test fun guideExampleReadsUnverified() {
        val certs = GuideExample.certificates
        for (name in listOf("hepb1", "bcg")) {
            val u = HcertVerifier.readUnverified(certs.getJSONObject(name).getString("hc1"), reg, DEFAULT_LIMITS).ok()
            assertEquals(GuideExample.KID_HEX, hex(u.kid!!), name)
            assertEquals(-6, u.entries.single().subclaim, name)
        }
    }

    /** J1 in the demo: issue with the TEST-ONLY ES256 key (prepare, platform sign, finish) and verify it. */
    @Test fun issueAndVerifyEs256() {
        assertVerified(issueAndVerify(CoseAlgorithm.ES256, Testkit.esDsc, Testkit::signEs256))
    }

    /**
     * PS256 on Android's providers, the open question of plan step 4: the
     * library verifies with the name "RSASSA-PSS". The testkit's PS256 DSC
     * may sign test certificates only (STT-VER-004), so a DVC fails at
     * KEY_USAGE, the step after SIGNATURE: reaching it shows the PS256
     * signature verified.
     */
    @Test fun issueAndVerifyPs256() {
        val f = assertIs<VerificationResult.Failed>(issueAndVerify(CoseAlgorithm.PS256, Testkit.psDsc, Testkit::signPs256)).value
        assertEquals(Step.KEY_USAGE to FailureReason.KEY_USAGE_MISMATCH, f.step to f.reason)
    }

    /** J1 on a device: the signing key lives in the Android Keystore and never leaves it (STT-COS-006). */
    @Test fun issueWithAndroidKeystoreKeyAndVerify() {
        val alias = "hcert-test-" + System.nanoTime()
        val kpg = KeyPairGenerator.getInstance(KeyProperties.KEY_ALGORITHM_EC, "AndroidKeyStore")
        kpg.initialize(
            KeyGenParameterSpec.Builder(alias, KeyProperties.PURPOSE_SIGN or KeyProperties.PURPOSE_VERIFY)
                .setDigests(KeyProperties.DIGEST_SHA256)
                .build(),
        )
        kpg.generateKeyPair()
        val ks = KeyStore.getInstance("AndroidKeyStore").apply { load(null) }
        try {
            val key = ks.getKey(alias, null) as PrivateKey
            // The Keystore's own self-signed certificate stands in for a DSC.
            val dsc = ks.getCertificate(alias).encoded
            assertVerified(
                issueAndVerify(CoseAlgorithm.ES256, dsc) { tbs ->
                    Signature.getInstance("SHA256withECDSA").run { initSign(key); update(tbs); sign() }
                },
            )
        } finally {
            ks.deleteEntry(alias)
        }
    }

    private fun assertVerified(r: VerificationResult) {
        val v = assertIs<VerificationResult.Verified>(r, r.toString()).value
        assertEquals(NEWBORN.vx.vp, assertIs<Payload.DvcMin>(v.entries.single().payload).value.vx.vp)
    }

    /** Issue NEWBORN's DVC (prepare, sign with [sign], finish) and verify it against [dsc] alone. */
    private fun issueAndVerify(alg: CoseAlgorithm, dsc: ByteArray, sign: (ByteArray) -> ByteArray): VerificationResult {
        val now = System.currentTimeMillis() / 1000
        val req = IssueRequest(
            listOf(Payload.DvcMin(NEWBORN)), "XX", Validity(now, now + 86400), dsc, alg, allowDevelopmentSubclaims = true,
        )
        val pending = HcertIssuer.prepare(req, reg).ok()
        val issued = HcertIssuer.finish(pending, sign(pending.toBeSigned())).ok()
        assertTrue(issued.hc1.startsWith("HC1:"))
        val store = HcertTrustStore().apply { addPem(certificatePem(dsc)).ok() }
        return HcertVerifier.verify(issued.hc1, store, reg, now + 60, OPTIONS)
    }
}
