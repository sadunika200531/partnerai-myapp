package com.monitor.data

import retrofit2.http.POST
import retrofit2.http.Body

interface ApiService {
    @POST("auth/register")
    suspend fun register(@Body user: Any): retrofit2.Response<Unit>
}