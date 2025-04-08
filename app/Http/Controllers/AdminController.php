<?php
namespace App\Http\Controllers;

use App\Models\User;
use App\Models\Book;
use App\Models\AudioBook;
use App\Models\Video;
use App\Models\Category;
use App\Models\Article;
use App\Models\Comment;
use App\Models\Like;
use App\Models\ArticleReadingProgress;
use App\Models\MobileApp;
use Illuminate\Http\Request;
use Inertia\Inertia;
use Illuminate\Support\Facades\Hash;

class AdminController extends Controller
{
    public function index()
    {
        return Inertia::render('Admin/Dashboard', [
            'users' => User::with('articles', 'comments', 'likes', 'readingProgress')->get(),
            'books' => Book::with('category')->get(),
            'audioBooks' => AudioBook::with('category')->get(),
            'videos' => Video::with('category')->get(),
            'categories' => Category::all(),
            'articles' => Article::with('category', 'user', 'comments', 'likes', 'readingProgress')->get(),
            'comments' => Comment::with(['user', 'commentable'])->get(),
            'mobileApp' => MobileApp::first(),
            'authUser' => auth()->user(),
        ]);
    }

    public function storeUser(Request $request)
    {
        $request->validate([
            'name' => 'required|string|max:255',
            'email' => 'required|string|email|max:255|unique:users',
            'password' => 'required|string|min:8',
            'role' => 'required|in:user,admin',
            'bio' => 'nullable|string',
        ]);

        User::create([
            'name' => $request->name,
            'email' => $request->email,
            'password' => Hash::make($request->password),
            'role' => $request->role,
            'bio' => $request->bio,
        ]);

        return redirect()->back();
    }

    public function updateUser(Request $request, User $user)
    {
        if (!auth()->user()->isAdmin()) {
            return response()->json(['message' => 'Unauthorized'], 403);
        }

        $request->validate([
            'name' => 'required|string|max:255',
            'email' => 'required|string|email|max:255|unique:users,email,' . $user->id,
            'role' => 'required|in:user,admin',
            'bio' => 'nullable|string',
            'password' => 'nullable|string|min:8',
        ]);

        $data = $request->only('name', 'email', 'role', 'bio');
        if ($request->filled('password')) {
            $data['password'] = Hash::make($request->password);
        }

        $user->update($data);
        return redirect()->back();
    }

    public function toggleAdmin(User $user)
    {
        if (!auth()->user()->isAdmin() || $user->id === auth()->user()->id) {
            return response()->json(['message' => 'Unauthorized'], 403);
        }

        $user->update(['role' => $user->isAdmin() ? 'user' : 'admin']);
        return redirect()->back();
    }

    public function destroyUser(User $user)
    {
        if (!auth()->user()->isAdmin() || $user->id === auth()->user()->id) {
            return response()->json(['message' => 'Unauthorized'], 403);
        }

        $user->delete();
        return redirect()->back();
    }

    public function storeArticle(Request $request)
    {
        $request->validate([
            'title' => 'required|string|max:255',
            'content' => 'required|string',
            'category_id' => 'nullable|exists:categories,id',
            'thumbnail' => 'nullable|image|max:2048',
        ]);

        $data = $request->only('title', 'content', 'category_id');
        $data['user_id'] = auth()->user()->id;
        if ($request->hasFile('thumbnail')) {
            $data['thumbnail'] = $request->file('thumbnail')->store('thumbnails', 'public');
        }
        $article = Article::create($data);
        $article->setWordCountAttribute();
        $article->save();

        return redirect()->back();
    }

    public function updateArticle(Request $request, Article $article)
    {
        $request->validate([
            'title' => 'required|string|max:255',
            'content' => 'required|string',
            'category_id' => 'nullable|exists:categories,id',
            'thumbnail' => 'nullable|image|max:2048',
        ]);

        $data = $request->only('title', 'content', 'category_id');
        if ($request->hasFile('thumbnail')) {
            if ($article->thumbnail) {
                \Storage::disk('public')->delete($article->thumbnail);
            }
            $data['thumbnail'] = $request->file('thumbnail')->store('thumbnails', 'public');
        }
        $article->update($data);
        $article->setWordCountAttribute();
        $article->save();

        return redirect()->back();
    }

    public function destroyArticle(Article $article)
    {
        if ($article->thumbnail) {
            \Storage::disk('public')->delete($article->thumbnail);
        }
        $article->delete();
        return redirect()->back();
    }

    public function storeComment(Request $request)
    {
        $request->validate([
            'commentable_id' => 'required',
            'commentable_type' => 'required|in:App\Models\Article',
            'content' => 'required|string',
        ]);

        Comment::create([
            'user_id' => auth()->user()->id,
            'commentable_id' => $request->commentable_id,
            'commentable_type' => $request->commentable_type,
            'content' => $request->content,
            'approved' => auth()->user()->isAdmin(),
        ]);

        return redirect()->back();
    }

    public function addRandomLikes(Request $request)
    {
        $request->validate([
            'likeable_id' => 'required',
            'likeable_type' => 'required|in:App\Models\Article',
            'count' => 'required|integer|min:0',
        ]);

        if (!auth()->user()->isAdmin()) {
            return response()->json(['message' => 'Unauthorized'], 403);
        }

        $likeable = $request->likeable_type::findOrFail($request->likeable_id);
        $currentLikes = $likeable->likes()->count();
        $targetLikes = $request->count;

        if ($targetLikes > $currentLikes) {
            $users = User::where('id', '!=', auth()->user()->id)->inRandomOrder()
                ->limit($targetLikes - $currentLikes)->get();
            foreach ($users as $user) {
                $likeable->likes()->firstOrCreate(['user_id' => $user->id]);
            }
        } elseif ($targetLikes < $currentLikes) {
            $likeable->likes()->orderBy('id', 'desc')->limit($currentLikes - $targetLikes)->delete();
        }

        return redirect()->back();
    }

    public function addRandomComment(Request $request)
    {
        $request->validate([
            'commentable_id' => 'required',
            'commentable_type' => 'required|in:App\Models\Article',
            'content' => 'required|string',
        ]);

        if (!auth()->user()->isAdmin()) {
            return response()->json(['message' => 'Unauthorized'], 403);
        }

        Comment::create([
            'user_id' => auth()->user()->id,
            'commentable_id' => $request->commentable_id,
            'commentable_type' => $request->commentable_type,
            'content' => $request->content,
            'approved' => true,
        ]);

        return redirect()->back();
    }

    public function approveComment(Comment $comment)
    {
        $comment->update(['approved' => true]);
        return redirect()->back();
    }

    public function destroyComment(Comment $comment)
    {
        $comment->delete();
        return redirect()->back();
    }

    public function updateMobileApp(Request $request)
    {
        $request->validate([
            'name' => 'required|string|max:255',
            'version' => 'nullable|string|max:20',
            'android_download_link' => 'nullable|url',
            'ios_download_link' => 'nullable|url',
            'is_published' => 'boolean',
            'settings' => 'nullable|array',
        ]);

        $mobileApp = MobileApp::firstOrCreate([], []);
        $mobileApp->update($request->all());
        return redirect()->back();
    }
}