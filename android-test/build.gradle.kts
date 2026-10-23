// An Android library module with no code of its own: its instrumented tests
// run the HCERT library's JVM jars (lib/hcert/build/libs/, built from the
// pinned smart-trust-tools commit by lib/hcert/build.py) on an emulator, on
// Android's own crypto providers. [STT-GEN-004]
plugins {
    id("com.android.library") version "8.10.1"
    id("org.jetbrains.kotlin.android") version "2.0.21" // the Kotlin the library is built with
}

val hcertLibs = rootProject.file("../lib/hcert/build/libs")
// The vectors at the same pinned commit the jars are built from.
val hcertVectors = rootProject.file("../lib/hcert/build/src/vectors")

android {
    namespace = "org.smarttrust.demo.androidtest"
    compileSdk = 35
    defaultConfig {
        // 26: the oldest Android a clinic phone plausibly runs and the first
        // with java.util.Base64; the CI matrix also runs 35.
        minSdk = 26
        testInstrumentationRunner = "androidx.test.runner.AndroidJUnitRunner"
    }
    compileOptions {
        sourceCompatibility = JavaVersion.VERSION_11
        targetCompatibility = JavaVersion.VERSION_11
    }
    sourceSets["androidTest"].assets.srcDir(hcertVectors)
}

kotlin {
    compilerOptions {
        jvmTarget.set(org.jetbrains.kotlin.gradle.dsl.JvmTarget.JVM_11)
    }
}

dependencies {
    androidTestImplementation(files(hcertLibs.resolve("hcert-api-jvm.jar"), hcertLibs.resolve("hcert-core-jvm.jar")))
    androidTestImplementation("androidx.test:runner:1.6.2")
    androidTestImplementation("androidx.test.ext:junit:1.2.1")
    androidTestImplementation("org.jetbrains.kotlin:kotlin-test-junit:2.0.21")
}
