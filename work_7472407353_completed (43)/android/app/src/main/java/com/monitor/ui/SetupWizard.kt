package com.monitor.ui

import androidx.compose.runtime.*
import androidx.compose.material3.*

@Composable
fun SetupWizard(onComplete: (String) -> Unit) {
    var url by remember { mutableStateOf("") }
    Column {
        TextField(value = url, onValueChange = { url = it }, label = { Text("Server URL") })
        Button(onClick = { onComplete(url) }) { Text("Connect") }
    }
}