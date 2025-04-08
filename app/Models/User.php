<?php
namespace App\Models;

use Illuminate\Foundation\Auth\User as Authenticatable;
use Laravel\Sanctum\HasApiTokens;

class User extends Authenticatable
{
    use HasApiTokens;

    protected $fillable = ['name', 'email', 'password', 'role', 'bio'];

    protected $hidden = ['password', 'remember_token'];

    public function articles()
    {
        return $this->hasMany(Article::class);
    }

    public function comments()
    {
        return $this->hasMany(Comment::class);
    }

    public function likes()
    {
        return $this->hasMany(Like::class);
    }

    public function readingProgress()
    {
        return $this->hasMany(ArticleReadingProgress::class);
    }

    public function isAdmin()
    {
        return $this->role === 'admin';
    }
}