package org.smarttrust.demo.app

import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.material3.Button
import androidx.compose.material3.Card
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp

/** J2 then J3 on the guide's DVCs: the CHW reads them offline, the clinic verifies them. */
@Composable
fun JourneyScreen(journeys: HcertJourneys) {
    val examples = remember { journeys.examples() }
    var views by remember { mutableStateOf(examples.map { (label, hc1) -> journeys.readOffline(label, hc1) }) }
    MaterialTheme {
        Column(Modifier.padding(16.dp), verticalArrangement = Arrangement.spacedBy(12.dp)) {
            Text("Chanthala's birth-dose DVCs", style = MaterialTheme.typography.titleLarge)
            Row(horizontalArrangement = Arrangement.spacedBy(8.dp)) {
                Button(onClick = { views = examples.map { (label, hc1) -> journeys.readOffline(label, hc1) } }) {
                    Text("J2: read offline")
                }
                Button(onClick = { views = views.zip(examples).map { (v, e) -> journeys.verify(v, e.second) } }) {
                    Text("J3: verify")
                }
                Button(onClick = { views = views.mapIndexed { i, v -> journeys.import(v, i) } }) {
                    Text("J3: import")
                }
            }
            LazyColumn(verticalArrangement = Arrangement.spacedBy(8.dp)) {
                items(views) { v -> DvcCard(v) }
            }
        }
    }
}

@Composable
private fun DvcCard(v: DvcView) {
    Card(Modifier.fillMaxWidth()) {
        Column(Modifier.padding(12.dp), verticalArrangement = Arrangement.spacedBy(4.dp)) {
            Text(v.label, style = MaterialTheme.typography.titleMedium)
            v.dose?.let { d ->
                Text("${d.name}, born ${d.dob}")
                Text("Product ${d.product}, given ${d.date}, batch ${d.batch}")
            }
            Text(v.readOffline)
            v.verified?.let { Text(it, style = MaterialTheme.typography.bodyLarge) }
            v.imported?.let { Text(it, style = MaterialTheme.typography.bodySmall) }
        }
    }
}
