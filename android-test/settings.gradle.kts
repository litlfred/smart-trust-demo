// The Android emulator test of the Kotlin HCERT library (STT-GEN-004; plan
// step 4). Every artifact Gradle resolves, Google Maven and Maven Central
// alike, is pinned by sha256 in gradle/verification-metadata.xml.
pluginManagement {
    repositories {
        google()
        mavenCentral()
        gradlePluginPortal()
    }
}

dependencyResolutionManagement {
    repositoriesMode.set(RepositoriesMode.FAIL_ON_PROJECT_REPOS)
    repositories {
        google()
        mavenCentral()
    }
}

rootProject.name = "hcert-android-test"
