package org.smarttrust.demo.app

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        val journeys = AndroidHcertJourneys(
            read = { name -> assets.open(name).bufferedReader().use { it.readText() } },
            now = { System.currentTimeMillis() / 1000 },
        )
        setContent { JourneyScreen(journeys) }
    }
}
