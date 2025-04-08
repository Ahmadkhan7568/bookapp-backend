<?php
namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class Category extends Model
{
    protected $fillable = ['name'];

    public function books()
    {
        return $this->hasMany(Book::class);
    }

    public function audioBooks()
    {
        return $this->hasMany(AudioBook::class);
    }

    public function videos()
    {
        return $this->hasMany(Video::class);
    }
}