// Option B, step 1 of the app: the J2 read and the J3 verification of the
// guide's two signed DVCs, offline, on Android. Kotlin 2.3.21 is the Kotlin
// the OHS KMP libraries (dev.ohs.fhir) are built with, so they join in
// without a Kotlin bump: the J3 import uses the OHS FHIR R4 model. The
// HCERT jars are the pinned ones from lib/hcert/build/libs/.
plugins {
    kotlin("multiplatform") version "2.3.21"
    kotlin("plugin.compose") version "2.3.21"
    id("org.jetbrains.compose") version "1.11.1"
    id("com.android.application") version "8.10.1"
}

val hcertLibs = rootProject.file("../lib/hcert/build/libs")
// The guide's example at the same pinned smart-trust-tools commit as the jars.
val hcertVectors = rootProject.file("../lib/hcert/build/src/vectors/smart-trust-af75be2")

kotlin {
    androidTarget {
        compilerOptions {
            jvmTarget.set(org.jetbrains.kotlin.gradle.dsl.JvmTarget.JVM_11)
        }
    }

    sourceSets {
        commonMain.dependencies {
            implementation(compose.runtime)
            implementation(compose.foundation)
            implementation(compose.material3)
            // J3 import: FHIR R4 Immunization and Provenance (OHS KMP model).
            implementation("dev.ohs.fhir:fhir-model-r4:1.0.0-rc03")
            implementation("org.jetbrains.kotlinx:kotlinx-serialization-json:1.11.0")
            implementation("org.jetbrains.kotlinx:kotlinx-datetime:0.8.0")
        }
        androidMain.dependencies {
            implementation(files(hcertLibs.resolve("hcert-api-jvm.jar"), hcertLibs.resolve("hcert-core-jvm.jar")))
            implementation("androidx.activity:activity-compose:1.10.1")
        }
        val androidUnitTest by getting {
            dependencies {
                implementation(kotlin("test-junit"))
            }
        }
    }
}

android {
    namespace = "org.smarttrust.demo.app"
    // 36: dev.ohs.fhir:fhir-model-r4-android asks for it in its AAR metadata.
    compileSdk = 36
    defaultConfig {
        applicationId = "org.smarttrust.demo.app"
        minSdk = 26
        targetSdk = 35
        versionCode = 1
        versionName = "0.1.0"
    }
    compileOptions {
        sourceCompatibility = JavaVersion.VERSION_11
        targetCompatibility = JavaVersion.VERSION_11
    }
    sourceSets["main"].assets.srcDir(hcertVectors)
}

tasks.withType<Test>().configureEach {
    systemProperty("vectors.dir", hcertVectors.absolutePath)
}
