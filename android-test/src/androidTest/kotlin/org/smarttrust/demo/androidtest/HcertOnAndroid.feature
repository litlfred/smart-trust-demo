Feature: The Kotlin HCERT library on Android, on the platform's own crypto providers
  What the journeys J1 to J3 ask of the library (STT-GEN-004), run on an emulator.

  @test:android-test/src/androidTest/kotlin/org/smarttrust/demo/androidtest/HcertOnAndroidTest.kt::guideExampleVerifiesAgainstXxrDsc
  Scenario: guideExampleVerifiesAgainstXxrDsc
    Given a trust store holding exactly XXR's DSC from its DID document
    When the guide's "hepb1" and "bcg" DVCs are each verified an hour after their iat
    Then each is verified with issuer "XR"
    And each was signed by the DSC with the guide's kid
    And each has a single minimal DVC entry whose vaccine product matches the guide's payload

  @test:android-test/src/androidTest/kotlin/org/smarttrust/demo/androidtest/HcertOnAndroidTest.kt::guideExampleReadsUnverified
  Scenario: guideExampleReadsUnverified
    Given no trust list
    When the guide's "hepb1" and "bcg" DVCs are each read unverified with the default limits
    Then each names the guide's kid
    And each has a single entry under subclaim -6

  @test:android-test/src/androidTest/kotlin/org/smarttrust/demo/androidtest/HcertOnAndroidTest.kt::issueAndVerifyEs256
  Scenario: issueAndVerifyEs256
    Given the testkit's TEST-ONLY ES256 DSC and key
    When the newborn's DVC is issued by prepare, sign and finish
    Then the issued certificate starts with "HC1:"
    And verifying it against that DSC alone succeeds
    And its single entry carries the newborn's vaccine product

  @test:android-test/src/androidTest/kotlin/org/smarttrust/demo/androidtest/HcertOnAndroidTest.kt::issueAndVerifyPs256
  Scenario: issueAndVerifyPs256
    Given the testkit's PS256 DSC, which may sign test certificates only
    When the newborn's DVC is issued by prepare, sign and finish
    Then the issued certificate starts with "HC1:"
    And verifying it against that DSC alone fails at the KEY_USAGE step with KEY_USAGE_MISMATCH
    # Failing at KEY_USAGE, the step after SIGNATURE, shows the PS256 signature verified.

  @test:android-test/src/androidTest/kotlin/org/smarttrust/demo/androidtest/HcertOnAndroidTest.kt::issueWithAndroidKeystoreKeyAndVerify
  Scenario: issueWithAndroidKeystoreKeyAndVerify
    Given a new EC signing key generated inside the Android Keystore
    And the Keystore's self-signed certificate for it standing in for a DSC
    When the newborn's DVC is issued, signed with SHA256withECDSA by that key
    Then the issued certificate starts with "HC1:"
    And verifying it against that certificate alone succeeds
    And its single entry carries the newborn's vaccine product
    And the key is deleted from the Keystore afterwards
