<?php
use App\Http\Controllers\MobileAppController;
use Illuminate\Support\Facades\Route;

Route::middleware('auth:sanctum')->group(function () {
    Route::get('/mobile-app', [MobileAppController::class, 'index']);
    Route::get('/articles', [MobileAppController::class, 'articles']);
    Route::post('/reading-progress', [MobileAppController::class, 'updateReadingProgress']);
});