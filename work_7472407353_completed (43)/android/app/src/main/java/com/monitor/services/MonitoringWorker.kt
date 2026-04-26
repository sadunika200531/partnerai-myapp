package com.monitor.services

import android.content.Context
import androidx.work.Worker
import androidx.work.WorkerParameters

class MonitoringWorker(ctx: Context, params: WorkerParameters) : Worker(ctx, params) {
    override fun doWork(): Result {
        // Logic to fetch metrics and trigger notification
        return Result.success()
    }
}