import os

# Define the project structure
BASE_DIR = os.getcwd()  # Should be E:\Drsalim\bookapp-backend

# Directories
MODELS_DIR = os.path.join(BASE_DIR, "app", "Models")
CONTROLLERS_DIR = os.path.join(BASE_DIR, "app", "Http", "Controllers")
INERTIA_PAGES_DIR = os.path.join(BASE_DIR, "resources", "js", "Pages", "Admin")
ROUTES_DIR = os.path.join(BASE_DIR, "routes")

# Ensure directories exist
os.makedirs(MODELS_DIR, exist_ok=True)
os.makedirs(CONTROLLERS_DIR, exist_ok=True)
os.makedirs(INERTIA_PAGES_DIR, exist_ok=True)
os.makedirs(ROUTES_DIR, exist_ok=True)

# Helper function to write files
def write_file(path, content):
    with open(path, "w") as f:
        f.write(content.strip())

# Helper function to append to a file (to preserve Breeze routes)
def append_to_file(path, content):
    with open(path, "a") as f:
        f.write("\n" + content.strip())

# Model Template (simplified and escaped braces correctly)
model_template = """
<?php
namespace App\\Models;

use Illuminate\\Database\\Eloquent\\Model;

class {class_name} extends Model
{{
    protected $fillable = [{fillable}];

    {relationships}
}}
"""

# User Model (update existing Breeze User model)
user_model = """
<?php
namespace App\\Models;

use Illuminate\\Foundation\\Auth\\User as Authenticatable;
use Illuminate\\Notifications\\Notifiable;
use Laravel\\Sanctum\\HasApiTokens;

class User extends Authenticatable
{{
    use HasApiTokens, Notifiable;

    protected $fillable = ['name', 'email', 'password'];
}}
"""

# Admin Controller with CRUD
admin_controller = """
<?php
namespace App\\Http\\Controllers;

use App\\Models\\User;
use App\\Models\\Book;
use App\\Models\\AudioBook;
use App\\Models\\Video;
use App\\Models\\Category;
use Illuminate\\Http\\Request;
use Inertia\\Inertia;

class AdminController extends Controller
{{
    public function index()
    {{
        return Inertia::render('Admin/Dashboard', [
            'users' => User::all(),
            'books' => Book::with('category')->get(),
            'audioBooks' => AudioBook::with('category')->get(),
            'videos' => Video::with('category')->get(),
            'categories' => Category::all(),
        ]);
    }}

    // Users
    public function storeUser(Request $request)
    {{
        $request->validate([
            'name' => 'required',
            'email' => 'required|email|unique:users',
            'password' => 'required',
        ]);
        User::create([
            'name' => $request->name,
            'email' => $request->email,
            'password' => bcrypt($request->password),
        ]);
        return redirect()->back();
    }}

    public function updateUser(Request $request, User $user)
    {{
        $request->validate([
            'name' => 'required',
            'email' => 'required|email|unique:users,email,' . $user->id,
        ]);
        $user->update($request->only('name', 'email'));
        return redirect()->back();
    }}

    public function destroyUser(User $user)
    {{
        $user->delete();
        return redirect()->back();
    }}

    // Categories
    public function storeCategory(Request $request)
    {{
        $request->validate(['name' => 'required']);
        Category::create($request->all());
        return redirect()->back();
    }}

    public function updateCategory(Request $request, Category $category)
    {{
        $request->validate(['name' => 'required']);
        $category->update($request->all());
        return redirect()->back();
    }}

    public function destroyCategory(Category $category)
    {{
        $category->delete();
        return redirect()->back();
    }}

    // Books
    public function storeBook(Request $request)
    {{
        $request->validate([
            'title' => 'required',
            'category_id' => 'required|exists:categories,id',
        ]);
        Book::create($request->all());
        return redirect()->back();
    }}

    public function updateBook(Request $request, Book $book)
    {{
        $request->validate([
            'title' => 'required',
            'category_id' => 'required|exists:categories,id',
        ]);
        $book->update($request->all());
        return redirect()->back();
    }}

    public function destroyBook(Book $book)
    {{
        $book->delete();
        return redirect()->back();
    }}

    // Audio Books
    public function storeAudioBook(Request $request)
    {{
        $request->validate([
            'title' => 'required',
            'file_url' => 'required',
            'category_id' => 'required|exists:categories,id',
        ]);
        AudioBook::create($request->all());
        return redirect()->back();
    }}

    public function updateAudioBook(Request $request, AudioBook $audioBook)
    {{
        $request->validate([
            'title' => 'required',
            'file_url' => 'required',
            'category_id' => 'required|exists:categories,id',
        ]);
        $audioBook->update($request->all());
        return redirect()->back();
    }}

    public function destroyAudioBook(AudioBook $audioBook)
    {{
        $audioBook->delete();
        return redirect()->back();
    }}

    // Videos
    public function storeVideo(Request $request)
    {{
        $request->validate([
            'title' => 'required',
            'file_url' => 'required',
            'category_id' => 'required|exists:categories,id',
        ]);
        Video::create($request->all());
        return redirect()->back();
    }}

    public function updateVideo(Request $request, Video $video)
    {{
        $request->validate([
            'title' => 'required',
            'file_url' => 'required',
            'category_id' => 'required|exists:categories,id',
        ]);
        $video->update($request->all());
        return redirect()->back();
    }}

    public function destroyVideo(Video $video)
    {{
        $video->delete();
        return redirect()->back();
    }}
}}
"""

# Admin Dashboard Vue Component
admin_dashboard_vue = """
<template>
    <div>
        <h1>BookApp Admin Panel</h1>

        <!-- Categories -->
        <div class="section">
            <h2>Categories</h2>
            <form @submit.prevent="addCategory">
                <input v-model="newCategory.name" placeholder="Category Name" required />
                <button type="submit">Add</button>
            </form>
            <ul>
                <li v-for="category in categories" :key="category.id">
                    <form @submit.prevent="updateCategory(category)">
                        <input v-model="category.name" required />
                        <button type="submit">Update</button>
                        <button type="button" @click="deleteCategory(category)">Delete</button>
                    </form>
                </li>
            </ul>
        </div>

        <!-- Books -->
        <div class="section">
            <h2>Books</h2>
            <form @submit.prevent="addBook">
                <input v-model="newBook.title" placeholder="Title" required />
                <input v-model="newBook.description" placeholder="Description" />
                <input v-model="newBook.thumbnail" placeholder="Thumbnail URL" />
                <select v-model="newBook.category_id" required>
                    <option v-for="category in categories" :value="category.id" :key="category.id">{{ category.name }}</option>
                </select>
                <button type="submit">Add</button>
            </form>
            <ul>
                <li v-for="book in books" :key="book.id">
                    <form @submit.prevent="updateBook(book)">
                        <input v-model="book.title" required />
                        <input v-model="book.description" />
                        <input v-model="book.thumbnail" />
                        <select v-model="book.category_id" required>
                            <option v-for="category in categories" :value="category.id" :key="category.id">{{ category.name }}</option>
                        </select>
                        <button type="submit">Update</button>
                        <button type="button" @click="deleteBook(book)">Delete</button>
                    </form>
                </li>
            </ul>
        </div>

        <!-- Audio Books -->
        <div class="section">
            <h2>Audio Books</h2>
            <form @submit.prevent="addAudioBook">
                <input v-model="newAudioBook.title" placeholder="Title" required />
                <input v-model="newAudioBook.file_url" placeholder="File URL" required />
                <input v-model="newAudioBook.thumbnail" placeholder="Thumbnail URL" />
                <select v-model="newAudioBook.category_id" required>
                    <option v-for="category in categories" :value="category.id" :key="category.id">{{ category.name }}</option>
                </select>
                <button type="submit">Add</button>
            </form>
            <ul>
                <li v-for="audioBook in audioBooks" :key="audioBook.id">
                    <form @submit.prevent="updateAudioBook(audioBook)">
                        <input v-model="audioBook.title" required />
                        <input v-model="audioBook.file_url" required />
                        <input v-model="audioBook.thumbnail" />
                        <select v-model="audioBook.category_id" required>
                            <option v-for="category in categories" :value="category.id" :key="category.id">{{ category.name }}</option>
                        </select>
                        <button type="submit">Update</button>
                        <button type="button" @click="deleteAudioBook(audioBook)">Delete</button>
                    </form>
                </li>
            </ul>
        </div>

        <!-- Videos -->
        <div class="section">
            <h2>Videos</h2>
            <form @submit.prevent="addVideo">
                <input v-model="newVideo.title" placeholder="Title" required />
                <input v-model="newVideo.file_url" placeholder="File URL" required />
                <input v-model="newVideo.thumbnail" placeholder="Thumbnail URL" />
                <select v-model="newVideo.category_id" required>
                    <option v-for="category in categories" :value="category.id" :key="category.id">{{ category.name }}</option>
                </select>
                <button type="submit">Add</button>
            </form>
            <ul>
                <li v-for="video in videos" :key="video.id">
                    <form @submit.prevent="updateVideo(video)">
                        <input v-model="video.title" required />
                        <input v-model="video.file_url" required />
                        <input v-model="video.thumbnail" />
                        <select v-model="video.category_id" required>
                            <option v-for="category in categories" :value="category.id" :key="category.id">{{ category.name }}</option>
                        </select>
                        <button type="submit">Update</button>
                        <button type="button" @click="deleteVideo(video)">Delete</button>
                    </form>
                </li>
            </ul>
        </div>

        <!-- Users -->
        <div class="section">
            <h2>Users</h2>
            <form @submit.prevent="addUser">
                <input v-model="newUser.name" placeholder="Name" required />
                <input v-model="newUser.email" placeholder="Email" type="email" required />
                <input v-model="newUser.password" placeholder="Password" type="password" required />
                <button type="submit">Add</button>
            </form>
            <ul>
                <li v-for="user in users" :key="user.id">
                    <form @submit.prevent="updateUser(user)">
                        <input v-model="user.name" required />
                        <input v-model="user.email" type="email" required />
                        <button type="submit">Update</button>
                        <button type="button" @click="deleteUser(user)">Delete</button>
                    </form>
                </li>
            </ul>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {{
    props: {{
        users: Array,
        books: Array,
        audioBooks: Array,
        videos: Array,
        categories: Array,
    }},
    data() {{
        return {{
            newUser: {{ name: '', email: '', password: '' }},
            newBook: {{ title: '', description: '', thumbnail: '', category_id: '' }},
            newAudioBook: {{ title: '', file_url: '', thumbnail: '', category_id: '' }},
            newVideo: {{ title: '', file_url: '', thumbnail: '', category_id: '' }},
            newCategory: {{ name: '' }},
        }};
    }},
    methods: {{
        async addUser() {{
            await axios.post('/admin/user', this.newUser);
            this.newUser = {{ name: '', email: '', password: '' }};
            this.$inertia.reload();
        }},
        async updateUser(user) {{
            await axios.put(`/admin/user/${{user.id}}`, user);
            this.$inertia.reload();
        }},
        async deleteUser(user) {{
            await axios.delete(`/admin/user/${{user.id}}`);
            this.$inertia.reload();
        }},
        async addBook() {{
            await axios.post('/admin/book', this.newBook);
            this.newBook = {{ title: '', description: '', thumbnail: '', category_id: '' }};
            this.$inertia.reload();
        }},
        async updateBook(book) {{
            await axios.put(`/admin/book/${{book.id}}`, book);
            this.$inertia.reload();
        }},
        async deleteBook(book) {{
            await axios.delete(`/admin/book/${{book.id}}`);
            this.$inertia.reload();
        }},
        async addAudioBook() {{
            await axios.post('/admin/audio-book', this.newAudioBook);
            this.newAudioBook = {{ title: '', file_url: '', thumbnail: '', category_id: '' }};
            this.$inertia.reload();
        }},
        async updateAudioBook(audioBook) {{
            await axios.put(`/admin/audio-book/${{audioBook.id}}`, audioBook);
            this.$inertia.reload();
        }},
        async deleteAudioBook(audioBook) {{
            await axios.delete(`/admin/audio-book/${{audioBook.id}}`);
            this.$inertia.reload();
        }},
        async addVideo() {{
            await axios.post('/admin/video', this.newVideo);
            this.newVideo = {{ title: '', file_url: '', thumbnail: '', category_id: '' }};
            this.$inertia.reload();
        }},
        async updateVideo(video) {{
            await axios.put(`/admin/video/${{video.id}}`, video);
            this.$inertia.reload();
        }},
        async deleteVideo(video) {{
            await axios.delete(`/admin/video/${{video.id}}`);
            this.$inertia.reload();
        }},
        async addCategory() {{
            await axios.post('/admin/category', this.newCategory);
            this.newCategory = {{ name: '' }};
            this.$inertia.reload();
        }},
        async updateCategory(category) {{
            await axios.put(`/admin/category/${{category.id}}`, category);
            this.$inertia.reload();
        }},
        async deleteCategory(category) {{
            await axios.delete(`/admin/category/${{category.id}}`);
            this.$inertia.reload();
        }},
    }},
}};
</script>

<style>
.section {{ margin-bottom: 20px; }}
input, select {{ margin-right: 10px; }}
button {{ margin-right: 5px; }}
</style>
"""

# Web Routes to append
web_routes_append = """
use App\\Http\\Controllers\\AdminController;

Route::middleware('auth')->group(function () {{
    Route::get('/admin', [AdminController::class, 'index'])->name('admin.dashboard');
    Route::post('/admin/user', [AdminController::class, 'storeUser'])->name('admin.storeUser');
    Route::put('/admin/user/{{user}}', [AdminController::class, 'updateUser'])->name('admin.updateUser');
    Route::delete('/admin/user/{{user}}', [AdminController::class, 'destroyUser'])->name('admin.destroyUser');
    Route::post('/admin/book', [AdminController::class, 'storeBook'])->name('admin.storeBook');
    Route::put('/admin/book/{{book}}', [AdminController::class, 'updateBook'])->name('admin.updateBook');
    Route::delete('/admin/book/{{book}}', [AdminController::class, 'destroyBook'])->name('admin.destroyBook');
    Route::post('/admin/audio-book', [AdminController::class, 'storeAudioBook'])->name('admin.storeAudioBook');
    Route::put('/admin/audio-book/{{audioBook}}', [AdminController::class, 'updateAudioBook'])->name('admin.updateAudioBook');
    Route::delete('/admin/audio-book/{{audioBook}}', [AdminController::class, 'destroyAudioBook'])->name('admin.destroyAudioBook');
    Route::post('/admin/video', [AdminController::class, 'storeVideo'])->name('admin.storeVideo');
    Route::put('/admin/video/{{video}}', [AdminController::class, 'updateVideo'])->name('admin.updateVideo');
    Route::delete('/admin/video/{{video}}', [AdminController::class, 'destroyVideo'])->name('admin.destroyVideo');
    Route::post('/admin/category', [AdminController::class, 'storeCategory'])->name('admin.storeCategory');
    Route::put('/admin/category/{{category}}', [AdminController::class, 'updateCategory'])->name('admin.updateCategory');
    Route::delete('/admin/category/{{category}}', [AdminController::class, 'destroyCategory'])->name('admin.destroyCategory');
}});
"""

# Entities to generate (models only)
entities = {
    "categories": {
        "fillable": "'name'",
        "relationships": """
    public function books()
    {{
        return $this->hasMany(Book::class);
    }}

    public function audioBooks()
    {{
        return $this->hasMany(AudioBook::class);
    }}

    public function videos()
    {{
        return $this->hasMany(Video::class);
    }}
"""
    },
    "books": {
        "fillable": "'title', 'description', 'thumbnail', 'category_id'",
        "relationships": """
    public function category()
    {{
        return $this->belongsTo(Category::class);
    }}
"""
    },
    "audio_books": {
        "fillable": "'title', 'file_url', 'thumbnail', 'category_id'",
        "relationships": """
    public function category()
    {{
        return $this->belongsTo(Category::class);
    }}
"""
    },
    "videos": {
        "fillable": "'title', 'file_url', 'thumbnail', 'category_id'",
        "relationships": """
    public function category()
    {{
        return $this->belongsTo(Category::class);
    }}
"""
    }
}

# Generate models
for table in entities:
    config = entities[table]
    # Compute class_name separately
    if table.endswith('s'):
        class_name = table[:-1].capitalize()
    else:
        class_name = table.capitalize()
    model_filename = os.path.join(MODELS_DIR, f"{class_name}.php")
    model_content = model_template.format(
        class_name=class_name,
        fillable=config["fillable"],
        relationships=config["relationships"]
    )
    write_file(model_filename, model_content)

# Update User model
write_file(os.path.join(MODELS_DIR, "User.php"), user_model)

# Generate AdminController
write_file(os.path.join(CONTROLLERS_DIR, "AdminController.php"), admin_controller)

# Append admin routes to web.php
web_php_path = os.path.join(ROUTES_DIR, "web.php")
if os.path.exists(web_php_path):
    append_to_file(web_php_path, web_routes_append)
else:
    write_file(web_php_path, "<?php\n" + web_routes_append)

# Generate Admin/Dashboard.vue
write_file(os.path.join(INERTIA_PAGES_DIR, "Dashboard.vue"), admin_dashboard_vue)

print("Admin panel files generated successfully (migrations skipped)!")