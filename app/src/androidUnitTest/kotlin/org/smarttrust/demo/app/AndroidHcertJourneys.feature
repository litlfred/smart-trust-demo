Feature: The demo app's journeys J2 and J3 on the JVM, against the pinned vectors the app bundles
  The clock is fixed an hour after the guide's iat, inside the DVCs' validity.

  @test:app/src/androidUnitTest/kotlin/org/smarttrust/demo/app/AndroidHcertJourneysTest.kt::AndroidHcertJourneysTest::j2ReadsBothDvcsOfflineAndMarksThemUnverified
  Scenario: j2ReadsBothDvcsOfflineAndMarksThemUnverified
    Given the guide's two example DVCs
    When each is read offline
    Then there are 2 views
    And each view has a dose whose name is "Chanthala SOUVANNALATH"
    And each view's offline reading says "NOT verified"
    And no view carries a verification result

  @test:app/src/androidUnitTest/kotlin/org/smarttrust/demo/app/AndroidHcertJourneysTest.kt::AndroidHcertJourneysTest::j3VerifiesBothAgainstXxrsDsc
  Scenario: j3VerifiesBothAgainstXxrsDsc
    Given the guide's two example DVCs, each read offline
    When each is verified
    Then each has a verification result that starts with "Verified"

  @test:app/src/androidUnitTest/kotlin/org/smarttrust/demo/app/AndroidHcertJourneysTest.kt::AndroidHcertJourneysTest::j3ImportsOnlyVerifiedDvcsAsImmunizationWithProvenance
  Scenario: j3ImportsOnlyVerifiedDvcsAsImmunizationWithProvenance
    Given the first of the guide's example DVCs, read offline
    When it is imported before it is verified
    Then nothing is imported
    When it is verified and then imported
    Then the import is an Immunization whose lotNumber, occurrenceDateTime and code are the dose's batch, date and product
    And its primarySource is false
    And it carries a Provenance with the value "916ffa567c0f44a2"
