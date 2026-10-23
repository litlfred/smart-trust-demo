package org.smarttrust.demo.app

/** One dose as a DVC carries it. */
data class Dose(val name: String, val dob: String, val product: String, val date: String, val batch: String)

/** What a screen shows for one DVC. */
data class DvcView(
    val label: String,
    val dose: Dose?,
    /** J2: read without a trust list, marked unverified (STT-VER-011). */
    val readOffline: String,
    /** J3: verified against the trust list held on the device, or the step and reason it failed (STT-VER-008). */
    val verified: String?,
)

/** The library, as the journeys use it; implemented per platform. */
interface HcertJourneys {
    /** The guide's two signed DVCs (QR Code Generation §12), as the family carries them. */
    fun examples(): List<Pair<String, String>>

    fun readOffline(label: String, hc1: String): DvcView

    fun verify(view: DvcView, hc1: String): DvcView
}
