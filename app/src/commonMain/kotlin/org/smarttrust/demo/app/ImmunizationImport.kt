package org.smarttrust.demo.app

import dev.ohs.fhir.model.r4.Code
import dev.ohs.fhir.model.r4.CodeableConcept
import dev.ohs.fhir.model.r4.Coding
import dev.ohs.fhir.model.r4.DateTime
import dev.ohs.fhir.model.r4.Enumeration
import dev.ohs.fhir.model.r4.FhirDateTime
import dev.ohs.fhir.model.r4.Identifier
import dev.ohs.fhir.model.r4.Immunization
import dev.ohs.fhir.model.r4.Instant
import dev.ohs.fhir.model.r4.Provenance
import dev.ohs.fhir.model.r4.Reference
import dev.ohs.fhir.model.r4.Uri
import kotlinx.datetime.TimeZone
import kotlinx.datetime.UtcOffset
import kotlinx.datetime.toLocalDateTime
import kotlinx.serialization.json.Json
import dev.ohs.fhir.model.r4.Boolean as FBoolean
import dev.ohs.fhir.model.r4.String as FString

/**
 * J3: a verified DVC imported into the clinic's record as one FHIR R4
 * `Immunization` (one DVC is one immunization event, STT-PAY-003) and the
 * `Provenance` that says where it came from.
 *
 * The fields follow WHO's DVCMin logical model (smart-trust-phw) and its
 * DVCImmunization profile: `vx.vp` is the vaccine product id from the WHO
 * PreQual database, `vx.dv` the date of vaccination, `vx.bo` the batch.
 * The record is secondary (`primarySource = false`): it was read from a
 * certificate, not observed. The certificate's signer (the DSC's kid and
 * country) is kept in the Provenance, so the record can be traced to the
 * trust list entry that verified it.
 */
object ImmunizationImport {
    /** The PreQual product id code system named by trust-phw's DVCMinVaccineDetailsPreQual. */
    const val PREQUAL_PRODUCT_IDS = "http://smart.who.int/pcmt-vaxprequal/CodeSystem/PreQualProductIds"

    /** The HCERT kid, as an identifier system local to this demonstrator. */
    const val KID_SYSTEM = "urn:smart-trust-demo:hcert-kid"

    /** One imported certificate: the Immunization and its Provenance. */
    data class Imported(val immunization: Immunization, val provenance: Provenance)

    /**
     * Maps a verified [dose] to FHIR. [patientRef] is the clinic's own
     * Patient (matching the holder to a record is the clinic's step, not the
     * certificate's). [kidHex] and [country] name the DSC that signed it;
     * [nowMillis] is when the import was recorded.
     */
    fun import(dose: Dose, id: String, patientRef: String, kidHex: String, country: String?, nowMillis: Long): Imported {
        val immunization = Immunization(
            id = id,
            status = Enumeration(value = Immunization.ImmunizationStatusCodes.Completed),
            vaccineCode = CodeableConcept(
                coding = listOf(Coding(system = Uri(value = PREQUAL_PRODUCT_IDS), code = Code(value = dose.product))),
            ),
            patient = Reference(reference = FString(value = patientRef), display = FString(value = dose.name)),
            occurrence = Immunization.Occurrence.DateTime(DateTime(value = FhirDateTime.fromString(dose.date))),
            primarySource = FBoolean(value = false),
            lotNumber = FString(value = dose.batch),
        )
        val recorded = kotlin.time.Instant.fromEpochMilliseconds(nowMillis).toLocalDateTime(TimeZone.UTC)
        val provenance = Provenance(
            id = "$id-provenance",
            target = listOf(Reference(reference = FString(value = "Immunization/$id"))),
            recorded = Instant(value = FhirDateTime.DateTime(recorded, UtcOffset.ZERO)),
            agent = listOf(
                Provenance.Agent(
                    who = Reference(
                        identifier = Identifier(system = Uri(value = KID_SYSTEM), value = FString(value = kidHex)),
                        display = FString(value = "Document Signer${country?.let { " of $it" } ?: ""} (kid $kidHex)"),
                    ),
                ),
            ),
        )
        return Imported(immunization, provenance)
    }

    private val json = Json { prettyPrint = true }

    fun toJson(imported: Imported): String =
        json.encodeToString(Immunization.serializer(), imported.immunization) + "\n" +
            json.encodeToString(Provenance.serializer(), imported.provenance)
}
