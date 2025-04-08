<?php
namespace App\Http\Controllers;

use App\Models\MobileApp;
use App\Models\Article;
use App\Models\ArticleReadingProgress;
use Illuminate\Http\Request;

class MobileAppController extends Controller
{
    public function index()
    {
        $mobileApp = MobileApp::first();
        if (!$mobileApp || !$mobileApp->is_published) {
            return response()->json(['message' => 'App not published'], 403);
        }

        $data = [
            'app' => [
                'name' => $mobileApp->name,
                'version' => $mobileApp->version,
                'android_download_link' => $mobileApp->android_download_link,
                'ios_download_link' => $mobileApp->ios_download_link,
                'settings' => $mobileApp->settings,
            ],
            'content' => [],
        ];

        if ($mobileApp->settings['sync_articles'] ?? false) {
            $data['content']['articles'] = Article::with('user', 'comments', 'likes', 'readingProgress')->get();
        }

        return response()->json($data);
    }

    public function articles()
    {
        $articles = Article::with(['user', 'comments' => function ($query) {
            $query->where('approved', true);
        }, 'likes', 'readingProgress' => function ($query) {
            $query->where('user_id', auth()->id());
        }])->get();

        return response()->json($articles);
    }

    public function updateReadingProgress(Request $request)
    {
        $request->validate([
            'article_id' => 'required|exists:articles,id',
            'words_read' => 'required|integer|min:0',
        ]);

        $progress = ArticleReadingProgress::updateOrCreate(
            ['user_id' => auth()->user()->id, 'article_id' => $request->article_id],
            ['words_read' => $request->words_read]
        );

        return response()->json([
            'progress_percentage' => $progress->progress_percentage,
        ]);
    }
}