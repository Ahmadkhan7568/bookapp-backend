<?php
namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class AudioBook extends Model
{
    protected $fillable = ['title', 'file_url', 'thumbnail', 'category_id'];

    public function category()
    {
        return $this->belongsTo(Category::class);
    }
}