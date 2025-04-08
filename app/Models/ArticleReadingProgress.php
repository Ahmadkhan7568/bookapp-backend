<?php
namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class ArticleReadingProgress extends Model
{
    protected $fillable = ['user_id', 'article_id', 'words_read'];

    public function user()
    {
        return $this->belongsTo(User::class);
    }

    public function article()
    {
        return $this->belongsTo(Article::class);
    }

    public function getProgressPercentageAttribute()
    {
        return $this->article->word_count > 0 
            ? min(100, round(($this->words_read / $this->article->word_count) * 100)) 
            : 0;
    }
}