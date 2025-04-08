<?php
namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class MobileApp extends Model
{
    protected $fillable = [
        'name', 'version', 'android_download_link', 'ios_download_link', 'is_published', 'settings'
    ];

    protected $casts = [
        'settings' => 'array',
        'is_published' => 'boolean',
    ];
}