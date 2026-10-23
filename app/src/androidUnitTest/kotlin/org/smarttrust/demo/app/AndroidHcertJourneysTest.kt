package org.smarttrust.demo.app

import java.io.File
import kotlin.test.Test
import kotlin.test.assertEquals
import kotlin.test.assertNotNull
import kotlin.test.assertNull
import kotlin.test.assertTrue

/** The journeys' logic on the JVM, against the same pinned vectors the app bundles. */
class AndroidHcertJourneysTest {
    private val dir = File(System.getProperty("vectors.dir"))
    // An hour after the guide's iat, inside the DVCs' validity.
    private val journeys = AndroidHcertJourneys(read = { File(dir, it).readText() }, now = { 1792657800L + 3600 })

    @Test fun j2ReadsBothDvcsOfflineAndMarksThemUnverified() {
        val views = journeys.examples().map { (label, hc1) -> journeys.readOffline(label, hc1) }
        assertEquals(2, views.size)
        for (v in views) {
            assertEquals("Chanthala SOUVANNALATH", assertNotNull(v.dose).name)
            assertTrue(v.readOffline.contains("NOT verified"))
            assertNull(v.verified)
        }
    }

    @Test fun j3VerifiesBothAgainstXxrsDsc() {
        for ((label, hc1) in journeys.examples()) {
            val v = journeys.verify(journeys.readOffline(label, hc1), hc1)
            assertTrue(assertNotNull(v.verified).startsWith("Verified"), v.verified)
        }
    }
}
