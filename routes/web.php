<?php
use App\Http\Controllers\AdminController;
use Illuminate\Support\Facades\Route;

Route::middleware(['auth'])->prefix('admin')->group(function () {
    Route::get('/', [AdminController::class, 'index'])->name('admin.dashboard');
    Route::post('/user', [AdminController::class, 'storeUser']);
    Route::put('/user/{user}', [AdminController::class, 'updateUser']);
    Route::put('/user/{user}/toggle-admin', [AdminController::class, 'toggleAdmin']);
    Route::delete('/user/{user}', [AdminController::class, 'destroyUser']);
    Route::post('/category', [AdminController::class, 'storeCategory']);
    Route::put('/category/{category}', [AdminController::class, 'updateCategory']);
    Route::delete('/category/{category}', [AdminController::class, 'destroyCategory']);
    Route::post('/book', [AdminController::class, 'storeBook']);
    Route::post('/book/{book}', [AdminController::class, 'updateBook']);
    Route::delete('/book/{book}', [AdminController::class, 'destroyBook']);
    Route::post('/audio-book', [AdminController::class, 'storeAudioBook']);
    Route::post('/audio-book/{audioBook}', [AdminController::class, 'updateAudioBook']);
    Route::delete('/audio-book/{audioBook}', [AdminController::class, 'destroyAudioBook']);
    Route::post('/video', [AdminController::class, 'storeVideo']);
    Route::put('/video/{video}', [AdminController::class, 'updateVideo']);
    Route::delete('/video/{video}', [AdminController::class, 'destroyVideo']);
    Route::post('/article', [AdminController::class, 'storeArticle']);
    Route::put('/article/{article}', [AdminController::class, 'updateArticle']);
    Route::delete('/article/{article}', [AdminController::class, 'destroyArticle']);
    Route::post('/comment', [AdminController::class, 'storeComment']);
    Route::post('/likes/random', [AdminController::class, 'addRandomLikes']);
    Route::post('/comment/random', [AdminController::class, 'addRandomComment']);
    Route::put('/comment/{comment}/approve', [AdminController::class, 'approveComment']);
    Route::delete('/comment/{comment}', [AdminController::class, 'destroyComment']);
    Route::put('/mobile-app', [AdminController::class, 'updateMobileApp']);
});

Route::middleware(['auth'])->group(function () {
    Route::get('/articles', function () {
        return Inertia::render('Articles', [
            'articles' => \App\Models\Article::with('user', 'comments', 'likes', 'readingProgress')->get(),
            'authUser' => auth()->user(),
        ]);
    })->name('articles');

    Route::post('/comment', [AdminController::class, 'storeComment']);
    Route::post('/like', function (Request $request) {
        $request->validate([
            'likeable_id' => 'required',
            'likeable_type' => 'required|in:App\Models\Article',
        ]);
        \App\Models\Like::firstOrCreate([
            'user_id' => auth()->user()->id,
            'likeable_id' => $request->likeable_id,
            'likeable_type' => $request->likeable_type,
        ]);
        return redirect()->back();
    });
    Route::delete('/like/{article_id}', function ($article_id) {
        \App\Models\Like::where([
            'user_id' => auth()->user()->id,
            'likeable_id' => $article_id,
            'likeable_type' => 'App\Models\Article',
        ])->delete();
        return redirect()->back();
    });
    Route::post('/reading-progress', function (Request $request) {
        $request->validate([
            'article_id' => 'required|exists:articles,id',
            'words_read' => 'required|integer|min:0',
        ]);
        \App\Models\ArticleReadingProgress::updateOrCreate(
            ['user_id' => auth()->user()->id, 'article_id' => $request->article_id],
            ['words_read' => $request->words_read]
        );
        return response()->json(['success' => true]);
    });
});