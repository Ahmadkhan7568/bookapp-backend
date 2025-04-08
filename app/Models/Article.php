<?php
namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class Article extends Model
{
    protected $fillable = ['title', 'content', 'category_id', 'user_id', 'thumbnail', 'word_count'];

    public function category()
    {
        return $this->belongsTo(Category::class);
    }

    public function user()
    {
        return $this->belongsTo(User::class);
    }

    public function comments()
    {
        return $this->morphMany(Comment::class, 'commentable');
    }

    public function likes()
    {
        return $this->morphMany(Like::class, 'likeable');
    }

    public function readingProgress()
    {
        return $this->hasMany(ArticleReadingProgress::class);
    }

    public function setWordCountAttribute()
    {
        $this->attributes['word_count'] = str_word_count(strip_tags($this->content));
    }
}