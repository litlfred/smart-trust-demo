// The demonstrator app (plan step 5, option B: memory/dir-app-platform.md):
// a lean Compose Multiplatform app, Android first, running the journeys
// offline with the Kotlin HCERT library. Every artifact Gradle resolves is
// pinned by sha256 in gradle/verification-metadata.xml.
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

rootProject.name = "smart-trust-demo-app"
