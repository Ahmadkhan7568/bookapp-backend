<template>
  <div class="min-h-screen bg-gray-100 font-sans flex">
    <!-- Sidebar -->
    <aside class="w-64 bg-white shadow-lg p-6 fixed h-full overflow-y-auto">
      <div class="flex items-center mb-8">
        <span class="text-2xl font-bold text-indigo-600">BookApp</span>
      </div>
      <nav>
        <ul class="space-y-2">
          <li v-for="tab in tabs" :key="tab">
            <button
              @click="activeTab = tab"
              class="w-full flex items-center p-3 rounded-lg transition-all duration-300"
              :class="activeTab === tab ? 'bg-indigo-500 text-white' : 'text-gray-600 hover:bg-indigo-50'"
            >
              <span class="mr-3">
                <span v-if="tab === 'Dashboard'">🏠</span>
                <span v-else-if="tab === 'Categories'">📁</span>
                <span v-else-if="tab === 'Books'">📖</span>
                <span v-else-if="tab === 'Audio Books'">🎧</span>
                <span v-else-if="tab === 'Videos'">▶️</span>
                <span v-else-if="tab === 'Users'">👥</span>
                <span v-else-if="tab === 'Comments'">💬</span>
                <span v-else-if="tab === 'Analytics'">📊</span>
                <span v-else-if="tab === 'Settings'">⚙️</span>
                <span v-else-if="tab === 'Profile'">👤</span>
              </span>
              {{ tab }}
            </button>
          </li>
        </ul>
      </nav>
      <div class="mt-8">
        <button class="w-full flex items-center p-3 rounded-lg bg-gray-200 text-gray-600 hover:bg-gray-300 transition-all duration-300">
          <span class="mr-3">📚</span> Documentation
        </button>
      </div>
    </aside>

    <!-- Main Content -->
    <div class="flex-1 ml-64 p-6">
      <!-- Header -->
      <header class="flex justify-between items-center mb-6">
        <h1 class="text-2xl font-semibold text-gray-800">{{ activeTab }}</h1>
        <div class="flex space-x-4">
          <input type="text" placeholder="Type here..." class="p-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-transparent" />
          <button @click="logout" class="bg-pink-500 text-white p-2 rounded-lg hover:bg-pink-600 transition-all duration-300">Sign Out</button>
        </div>
      </header>

      <!-- Dynamic Content -->
      <transition name="fade" mode="out-in">
        <div :key="activeTab">
          <!-- Dashboard Overview -->
          <section v-if="activeTab === 'Dashboard'" class="space-y-6">
            <!-- Stats Cards -->
            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
              <div class="bg-white p-6 rounded-xl shadow-md flex items-center space-x-4">
                <div class="p-3 bg-indigo-100 rounded-full">
                  <span class="text-2xl">💰</span>
                </div>
                <div>
                  <h3 class="text-sm text-gray-600">Today's Revenue</h3>
                  <p class="text-xl font-semibold text-gray-800">$53,000 <span class="text-green-500 text-sm">+55%</span></p>
                </div>
              </div>
              <div class="bg-white p-6 rounded-xl shadow-md flex items-center space-x-4">
                <div class="p-3 bg-pink-100 rounded-full">
                  <span class="text-2xl">👥</span>
                </div>
                <div>
                  <h3 class="text-sm text-gray-600">Today's Users</h3>
                  <p class="text-xl font-semibold text-gray-800">2,300 <span class="text-green-500 text-sm">+3%</span></p>
                </div>
              </div>
              <div class="bg-white p-6 rounded-xl shadow-md flex items-center space-x-4">
                <div class="p-3 bg-purple-100 rounded-full">
                  <span class="text-2xl">📖</span>
                </div>
                <div>
                  <h3 class="text-sm text-gray-600">New Books</h3>
                  <p class="text-xl font-semibold text-gray-800">+3,462 <span class="text-red-500 text-sm">-2%</span></p>
                </div>
              </div>
              <div class="bg-white p-6 rounded-xl shadow-md flex items-center space-x-4">
                <div class="p-3 bg-blue-100 rounded-full">
                  <span class="text-2xl">💸</span>
                </div>
                <div>
                  <h3 class="text-sm text-gray-600">Sales</h3>
                  <p class="text-xl font-semibold text-gray-800">$103,430 <span class="text-green-500 text-sm">+5%</span></p>
                </div>
              </div>
            </div>
            <!-- Content Cards -->
            <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
              <div class="bg-white p-6 rounded-xl shadow-md">
                <h2 class="text-xl font-semibold text-gray-800 mb-4">Built by Developers</h2>
                <p class="text-gray-600 mb-4">Soft UI Dashboard: From colors, cards, typography to complex elements, you will find the full documentation.</p>
                <button class="text-indigo-500 hover:underline">Read More</button>
              </div>
              <div class="bg-gradient-to-r from-purple-500 to-pink-500 p-6 rounded-xl shadow-md text-white">
                <h2 class="text-xl font-semibold mb-4">Work with the Rockets</h2>
                <p class="mb-4">Wealth creation is an evolutionarily recent positive-sum game. It is all about who takes the opportunity first.</p>
                <button class="text-white hover:underline">Read More</button>
              </div>
            </div>
          </section>

          <!-- Categories Section -->
          <section v-if="activeTab === 'Categories'" class="grid md:grid-cols-2 gap-6">
            <div class="bg-white p-6 rounded-xl shadow-md">
              <h2 class="text-xl font-semibold text-gray-800 mb-4">Add New Category</h2>
              <form @submit.prevent="addCategory" class="space-y-4">
                <input
                  v-model="newCategory.name"
                  placeholder="Category Name"
                  required
                  :disabled="loading.categories.add"
                  class="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-transparent"
                />
                <button
                  type="submit"
                  :disabled="loading.categories.add"
                  class="w-full bg-indigo-500 text-white p-3 rounded-lg hover:bg-indigo-600 transition-all duration-300 disabled:bg-gray-400"
                >
                  {{ loading.categories.add ? 'Adding...' : 'Add Category' }}
                </button>
              </form>
            </div>
            <div class="bg-white p-6 rounded-xl shadow-md">
              <h2 class="text-xl font-semibold text-gray-800 mb-4">Existing Categories</h2>
              <ul class="space-y-4">
                <li v-if="!categories || categories.length === 0" class="text-gray-500 italic">No categories found.</li>
                <li v-for="category in categories" :key="category.id" class="p-4 bg-gray-50 rounded-lg shadow-sm">
                  <form @submit.prevent="updateCategory(category)" class="space-y-4">
                    <div class="flex items-center space-x-4">
                      <input
                        v-model="category.name"
                        required
                        :disabled="loading.categories.update === category.id || loading.categories.delete === category.id"
                        class="flex-1 p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-transparent"
                      />
                      <button
                        type="submit"
                        :disabled="loading.categories.update === category.id || loading.categories.delete === category.id"
                        class="bg-green-500 text-white p-2 rounded-lg hover:bg-green-600 transition-all duration-300 disabled:bg-gray-400"
                      >
                        {{ loading.categories.update === category.id ? 'Saving...' : 'Update' }}
                      </button>
                      <button
                        type="button"
                        @click="deleteCategory(category)"
                        :disabled="loading.categories.update === category.id || loading.categories.delete === category.id"
                        class="bg-red-500 text-white p-2 rounded-lg hover:bg-red-600 transition-all duration-300 disabled:bg-gray-400"
                      >
                        {{ loading.categories.delete === category.id ? 'Deleting...' : 'Delete' }}
                      </button>
                    </div>
                  </form>
                </li>
              </ul>
            </div>
          </section>

          <!-- Books Section -->
          <section v-if="activeTab === 'Books'" class="grid md:grid-cols-2 gap-6">
            <div class="bg-white p-6 rounded-xl shadow-md">
              <h2 class="text-xl font-semibold text-gray-800 mb-4">Add New Book</h2>
              <form @submit.prevent="addBook" class="space-y-4">
                <input
                  v-model="newBook.title"
                  placeholder="Title"
                  required
                  :disabled="loading.books.add"
                  class="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-transparent"
                />
                <textarea
                  v-model="newBook.description"
                  placeholder="Description (Optional)"
                  :disabled="loading.books.add"
                  class="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-transparent"
                ></textarea>
                <select
                  v-model="newBook.category_id"
                  required
                  :disabled="loading.books.add"
                  class="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-transparent"
                >
                  <option value="" disabled>Select Category</option>
                  <option v-for="category in categories" :value="category.id" :key="'cat-add-'+category.id">{{ category.name }}</option>
                </select>
                <div>
                  <label class="block text-sm text-gray-600 mb-1">Book File (PDF, EPUB, etc.)</label>
                  <input
                    type="file"
                    ref="bookFile"
                    @change="handleBookFile"
                    required
                    :disabled="loading.books.add"
                    class="w-full p-2 border border-dashed border-gray-300 rounded-lg file:mr-4 file:py-2 file:px-4 file:rounded-lg file:border-0 file:bg-gray-200 file:text-gray-700 hover:file:bg-gray-300"
                  />
                </div>
                <div>
                  <label class="block text-sm text-gray-600 mb-1">Thumbnail Image (Optional)</label>
                  <input
                    type="file"
                    ref="bookThumbnail"
                    @change="handleBookThumbnail"
                    accept="image/*"
                    :disabled="loading.books.add"
                    class="w-full p-2 border border-dashed border-gray-300 rounded-lg file:mr-4 file:py-2 file:px-4 file:rounded-lg file:border-0 file:bg-gray-200 file:text-gray-700 hover:file:bg-gray-300"
                  />
                </div>
                <button
                  type="submit"
                  :disabled="loading.books.add"
                  class="w-full bg-indigo-500 text-white p-3 rounded-lg hover:bg-indigo-600 transition-all duration-300 disabled:bg-gray-400"
                >
                  {{ loading.books.add ? 'Adding...' : 'Add Book' }}
                </button>
              </form>
            </div>
            <div class="bg-white p-6 rounded-xl shadow-md">
              <h2 class="text-xl font-semibold text-gray-800 mb-4">Existing Books</h2>
              <ul class="space-y-4">
                <li v-if="!books || books.length === 0" class="text-gray-500 italic">No books found.</li>
                <li v-for="book in books" :key="book.id" class="p-4 bg-gray-50 rounded-lg shadow-sm">
                  <form @submit.prevent="updateBook(book)" class="space-y-4">
                    <input
                      v-model="book.title"
                      required
                      :disabled="loading.books.update === book.id || loading.books.delete === book.id"
                      class="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-transparent"
                    />
                    <textarea
                      v-model="book.description"
                      placeholder="Description"
                      :disabled="loading.books.update === book.id || loading.books.delete === book.id"
                      class="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-transparent"
                    ></textarea>
                    <select
                      v-model="book.category_id"
                      required
                      :disabled="loading.books.update === book.id || loading.books.delete === book.id"
                      class="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-transparent"
                    >
                      <option value="" disabled>Select Category</option>
                      <option v-for="category in categories" :value="category.id" :key="'cat-update-'+category.id">{{ category.name }}</option>
                    </select>
                    <div>
                      <label class="block text-sm text-gray-600 mb-1">Replace Book File (Optional)</label>
                      <input
                        type="file"
                        :ref="'updateBookFile_' + book.id"
                        @change="handleUpdateBookFile(book, $event)"
                        :disabled="loading.books.update === book.id || loading.books.delete === book.id"
                        class="w-full p-2 border border-dashed border-gray-300 rounded-lg file:mr-4 file:py-2 file:px-4 file:rounded-lg file:border-0 file:bg-gray-200 file:text-gray-700 hover:file:bg-gray-300"
                      />
                    </div>
                    <div>
                      <label class="block text-sm text-gray-600 mb-1">Replace Thumbnail (Optional)</label>
                      <input
                        type="file"
                        :ref="'updateBookThumbnail_' + book.id"
                        @change="handleUpdateBookThumbnail(book, $event)"
                        accept="image/*"
                        :disabled="loading.books.update === book.id || loading.books.delete === book.id"
                        class="w-full p-2 border border-dashed border-gray-300 rounded-lg file:mr-4 file:py-2 file:px-4 file:rounded-lg file:border-0 file:bg-gray-200 file:text-gray-700 hover:file:bg-gray-300"
                      />
                    </div>
                    <div class="flex space-x-4">
                      <button
                        type="submit"
                        :disabled="loading.books.update === book.id || loading.books.delete === book.id"
                        class="flex-1 bg-green-500 text-white p-2 rounded-lg hover:bg-green-600 transition-all duration-300 disabled:bg-gray-400"
                      >
                        {{ loading.books.update === book.id ? 'Saving...' : 'Update' }}
                      </button>
                      <button
                        type="button"
                        @click="deleteBook(book)"
                        :disabled="loading.books.update === book.id || loading.books.delete === book.id"
                        class="flex-1 bg-red-500 text-white p-2 rounded-lg hover:bg-red-600 transition-all duration-300 disabled:bg-gray-400"
                      >
                        {{ loading.books.delete === book.id ? 'Deleting...' : 'Delete' }}
                      </button>
                    </div>
                  </form>
                </li>
              </ul>
            </div>
          </section>

          <!-- Audio Books Section -->
          <section v-if="activeTab === 'Audio Books'" class="grid md:grid-cols-2 gap-6">
            <div class="bg-white p-6 rounded-xl shadow-md">
              <h2 class="text-xl font-semibold text-gray-800 mb-4">Add New Audio Book</h2>
              <form @submit.prevent="addAudioBook" class="space-y-4">
                <input
                  v-model="newAudioBook.title"
                  placeholder="Title"
                  required
                  :disabled="loading.audioBooks.add"
                  class="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-transparent"
                />
                <select
                  v-model="newAudioBook.category_id"
                  required
                  :disabled="loading.audioBooks.add"
                  class="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-transparent"
                >
                  <option value="" disabled>Select Category</option>
                  <option v-for="category in categories" :value="category.id" :key="'cat-add-audio-'+category.id">{{ category.name }}</option>
                </select>
                <div>
                  <label class="block text-sm text-gray-600 mb-1">Audio File (MP3, M4A, etc.)</label>
                  <input
                    type="file"
                    ref="audioFile"
                    @change="handleAudioFile"
                    required
                    accept="audio/*"
                    :disabled="loading.audioBooks.add"
                    class="w-full p-2 border border-dashed border-gray-300 rounded-lg file:mr-4 file:py-2 file:px-4 file:rounded-lg file:border-0 file:bg-gray-200 file:text-gray-700 hover:file:bg-gray-300"
                  />
                </div>
                <div>
                  <label class="block text-sm text-gray-600 mb-1">Thumbnail Image (Optional)</label>
                  <input
                    type="file"
                    ref="audioThumbnail"
                    @change="handleAudioThumbnail"
                    accept="image/*"
                    :disabled="loading.audioBooks.add"
                    class="w-full p-2 border border-dashed border-gray-300 rounded-lg file:mr-4 file:py-2 file:px-4 file:rounded-lg file:border-0 file:bg-gray-200 file:text-gray-700 hover:file:bg-gray-300"
                  />
                </div>
                <button
                  type="submit"
                  :disabled="loading.audioBooks.add"
                  class="w-full bg-indigo-500 text-white p-3 rounded-lg hover:bg-indigo-600 transition-all duration-300 disabled:bg-gray-400"
                >
                  {{ loading.audioBooks.add ? 'Adding...' : 'Add Audio Book' }}
                </button>
              </form>
            </div>
            <div class="bg-white p-6 rounded-xl shadow-md">
              <h2 class="text-xl font-semibold text-gray-800 mb-4">Existing Audio Books</h2>
              <ul class="space-y-4">
                <li v-if="!audioBooks || audioBooks.length === 0" class="text-gray-500 italic">No audio books found.</li>
                <li v-for="audioBook in audioBooks" :key="audioBook.id" class="p-4 bg-gray-50 rounded-lg shadow-sm">
                  <form @submit.prevent="updateAudioBook(audioBook)" class="space-y-4">
                    <input
                      v-model="audioBook.title"
                      required
                      :disabled="loading.audioBooks.update === audioBook.id || loading.audioBooks.delete === audioBook.id"
                      class="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-transparent"
                    />
                    <select
                      v-model="audioBook.category_id"
                      required
                      :disabled="loading.audioBooks.update === audioBook.id || loading.audioBooks.delete === audioBook.id"
                      class="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-transparent"
                    >
                      <option value="" disabled>Select Category</option>
                      <option v-for="category in categories" :value="category.id" :key="'cat-update-audio-'+category.id">{{ category.name }}</option>
                    </select>
                    <div>
                      <label class="block text-sm text-gray-600 mb-1">Replace Audio File (Optional)</label>
                      <input
                        type="file"
                        :ref="'updateAudioFile_' + audioBook.id"
                        @change="handleUpdateAudioFile(audioBook, $event)"
                        accept="audio/*"
                        :disabled="loading.audioBooks.update === audioBook.id || loading.audioBooks.delete === audioBook.id"
                        class="w-full p-2 border border-dashed border-gray-300 rounded-lg file:mr-4 file:py-2 file:px-4 file:rounded-lg file:border-0 file:bg-gray-200 file:text-gray-700 hover:file:bg-gray-300"
                      />
                    </div>
                    <div>
                      <label class="block text-sm text-gray-600 mb-1">Replace Thumbnail (Optional)</label>
                      <input
                        type="file"
                        :ref="'updateAudioThumbnail_' + audioBook.id"
                        @change="handleUpdateAudioThumbnail(audioBook, $event)"
                        accept="image/*"
                        :disabled="loading.audioBooks.update === audioBook.id || loading.audioBooks.delete === audioBook.id"
                        class="w-full p-2 border border-dashed border-gray-300 rounded-lg file:mr-4 file:py-2 file:px-4 file:rounded-lg file:border-0 file:bg-gray-200 file:text-gray-700 hover:file:bg-gray-300"
                      />
                    </div>
                    <div class="flex space-x-4">
                      <button
                        type="submit"
                        :disabled="loading.audioBooks.update === audioBook.id || loading.audioBooks.delete === audioBook.id"
                        class="flex-1 bg-green-500 text-white p-2 rounded-lg hover:bg-green-600 transition-all duration-300 disabled:bg-gray-400"
                      >
                        {{ loading.audioBooks.update === audioBook.id ? 'Saving...' : 'Update' }}
                      </button>
                      <button
                        type="button"
                        @click="deleteAudioBook(audioBook)"
                        :disabled="loading.audioBooks.update === audioBook.id || loading.audioBooks.delete === audioBook.id"
                        class="flex-1 bg-red-500 text-white p-2 rounded-lg hover:bg-red-600 transition-all duration-300 disabled:bg-gray-400"
                      >
                        {{ loading.audioBooks.delete === audioBook.id ? 'Deleting...' : 'Delete' }}
                      </button>
                    </div>
                  </form>
                </li>
              </ul>
            </div>
          </section>

          <!-- Videos Section -->
          <section v-if="activeTab === 'Videos'" class="grid md:grid-cols-2 gap-6">
            <div class="bg-white p-6 rounded-xl shadow-md">
              <h2 class="text-xl font-semibold text-gray-800 mb-4">Add New Video</h2>
              <form @submit.prevent="addVideo" class="space-y-4">
                <input
                  v-model="newVideo.title"
                  placeholder="Title"
                  required
                  :disabled="loading.videos.add"
                  class="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-transparent"
                />
                <input
                  v-model="newVideo.file_url"
                  placeholder="Video File URL (e.g., YouTube, Vimeo, or direct link)"
                  required
                  :disabled="loading.videos.add"
                  class="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-transparent"
                />
                <input
                  v-model="newVideo.thumbnail"
                  placeholder="Thumbnail Image URL (Optional)"
                  :disabled="loading.videos.add"
                  class="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-transparent"
                />
                <select
                  v-model="newVideo.category_id"
                  required
                  :disabled="loading.videos.add"
                  class="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-transparent"
                >
                  <option value="" disabled>Select Category</option>
                  <option v-for="category in categories" :value="category.id" :key="'cat-add-vid-'+category.id">{{ category.name }}</option>
                </select>
                <button
                  type="submit"
                  :disabled="loading.videos.add"
                  class="w-full bg-indigo-500 text-white p-3 rounded-lg hover:bg-indigo-600 transition-all duration-300 disabled:bg-gray-400"
                >
                  {{ loading.videos.add ? 'Adding...' : 'Add Video' }}
                </button>
              </form>
            </div>
            <div class="bg-white p-6 rounded-xl shadow-md">
              <h2 class="text-xl font-semibold text-gray-800 mb-4">Existing Videos</h2>
              <ul class="space-y-4">
                <li v-if="!videos || videos.length === 0" class="text-gray-500 italic">No videos found.</li>
                <li v-for="video in videos" :key="video.id" class="p-4 bg-gray-50 rounded-lg shadow-sm">
                  <form @submit.prevent="updateVideo(video)" class="space-y-4">
                    <input
                      v-model="video.title"
                      required
                      :disabled="loading.videos.update === video.id || loading.videos.delete === video.id"
                      class="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-transparent"
                    />
                    <input
                      v-model="video.file_url"
                      placeholder="Video File URL"
                      required
                      :disabled="loading.videos.update === video.id || loading.videos.delete === video.id"
                      class="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-transparent"
                    />
                    <input
                      v-model="video.thumbnail"
                      placeholder="Thumbnail Image URL"
                      :disabled="loading.videos.update === video.id || loading.videos.delete === video.id"
                      class="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-transparent"
                    />
                    <select
                      v-model="video.category_id"
                      required
                      :disabled="loading.videos.update === video.id || loading.videos.delete === video.id"
                      class="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-transparent"
                    >
                      <option value="" disabled>Select Category</option>
                      <option v-for="category in categories" :value="category.id" :key="'cat-update-vid-'+category.id">{{ category.name }}</option>
                    </select>
                    <div class="flex space-x-4">
                      <button
                        type="submit"
                        :disabled="loading.videos.update === video.id || loading.videos.delete === video.id"
                        class="flex-1 bg-green-500 text-white p-2 rounded-lg hover:bg-green-600 transition-all duration-300 disabled:bg-gray-400"
                      >
                        {{ loading.videos.update === video.id ? 'Saving...' : 'Update' }}
                      </button>
                      <button
                        type="button"
                        @click="deleteVideo(video)"
                        :disabled="loading.videos.update === video.id || loading.videos.delete === video.id"
                        class="flex-1 bg-red-500 text-white p-2 rounded-lg hover:bg-red-600 transition-all duration-300 disabled:bg-gray-400"
                      >
                        {{ loading.videos.delete === video.id ? 'Deleting...' : 'Delete' }}
                      </button>
                    </div>
                  </form>
                </li>
              </ul>
            </div>
          </section>

          <!-- Users Section -->
          <section v-if="activeTab === 'Users'" class="grid md:grid-cols-2 gap-6">
            <div class="bg-white p-6 rounded-xl shadow-md">
              <h2 class="text-xl font-semibold text-gray-800 mb-4">Add New User</h2>
              <form @submit.prevent="addUser" class="space-y-4">
                <input
                  v-model="newUser.name"
                  placeholder="Name"
                  required
                  :disabled="loading.users.add"
                  class="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-transparent"
                />
                <input
                  v-model="newUser.email"
                  placeholder="Email"
                  type="email"
                  required
                  :disabled="loading.users.add"
                  class="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-transparent"
                />
                <input
                  v-model="newUser.password"
                  placeholder="Password"
                  type="password"
                  required
                  :disabled="loading.users.add"
                  class="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-transparent"
                />
                <select
                  v-model="newUser.role"
                  required
                  :disabled="loading.users.add"
                  class="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-transparent"
                >
                  <option value="" disabled>Select Role</option>
                  <option value="admin">Admin</option>
                  <option value="user">User</option>
                </select>
                <button
                  type="submit"
                  :disabled="loading.users.add"
                  class="w-full bg-indigo-500 text-white p-3 rounded-lg hover:bg-indigo-600 transition-all duration-300 disabled:bg-gray-400"
                >
                  {{ loading.users.add ? 'Adding...' : 'Add User' }}
                </button>
              </form>
            </div>
            <div class="bg-white p-6 rounded-xl shadow-md">
              <h2 class="text-xl font-semibold text-gray-800 mb-4">Existing Users</h2>
              <ul class="space-y-4">
                <li v-if="!users || users.length === 0" class="text-gray-500 italic">No users found.</li>
                <li v-for="user in users" :key="user.id" class="p-4 bg-gray-50 rounded-lg shadow-sm">
                  <form @submit.prevent="updateUser(user)" class="space-y-4">
                    <div class="flex items-center space-x-4">
                      <input
                        v-model="user.name"
                        required
                        :disabled="loading.users.update === user.id || loading.users.delete === user.id"
                        class="flex-1 p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-transparent"
                      />
                      <input
                        v-model="user.email"
                        type="email"
                        required
                        :disabled="loading.users.update === user.id || loading.users.delete === user.id"
                        class="flex-1 p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-transparent"
                      />
                      <select
                        v-model="user.role"
                        required
                        :disabled="loading.users.update === user.id || loading.users.delete === user.id"
                        class="flex-1 p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-transparent"
                      >
                        <option value="admin">Admin</option>
                        <option value="user">User</option>
                      </select>
                      <button
                        type="submit"
                        :disabled="loading.users.update === user.id || loading.users.delete === user.id"
                        class="bg-green-500 text-white p-2 rounded-lg hover:bg-green-600 transition-all duration-300 disabled:bg-gray-400"
                      >
                        {{ loading.users.update === user.id ? 'Saving...' : 'Update' }}
                      </button>
                      <button
                        type="button"
                        @click="deleteUser(user)"
                        :disabled="loading.users.update === user.id || loading.users.delete === user.id"
                        class="bg-red-500 text-white p-2 rounded-lg hover:bg-red-600 transition-all duration-300 disabled:bg-gray-400"
                      >
                        {{ loading.users.delete === user.id ? 'Deleting...' : 'Delete' }}
                      </button>
                    </div>
                  </form>
                </li>
              </ul>
            </div>
          </section>

          <!-- Comments Section -->
          <section v-if="activeTab === 'Comments'" class="bg-white p-6 rounded-xl shadow-md">
            <h2 class="text-xl font-semibold text-gray-800 mb-4">Manage Comments</h2>
            <div class="mb-4">
              <select
                v-model="commentFilter"
                @change="fetchComments"
                class="p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-transparent"
              >
                <option value="all">All Comments</option>
                <option value="pending">Pending Approval</option>
                <option value="approved">Approved</option>
              </select>
            </div>
            <ul class="space-y-4">
              <li v-if="!comments || comments.length === 0" class="text-gray-500 italic">No comments found.</li>
              <li v-for="comment in comments" :key="comment.id" class="p-4 bg-gray-50 rounded-lg shadow-sm">
                <div class="flex items-center space-x-4">
                  <div class="flex-1">
                    <p class="text-gray-800"><strong>{{ comment.user.name }}</strong> on <strong>{{ comment.commentable_type }}: {{ comment.commentable.title }}</strong></p>
                    <p class="text-gray-600">{{ comment.content }}</p>
                    <p class="text-sm text-gray-500">Status: {{ comment.approved ? 'Approved' : 'Pending' }}</p>
                  </div>
                  <div class="flex space-x-2">
                    <button
                      v-if="!comment.approved"
                      @click="approveComment(comment)"
                      :disabled="loading.comments.approve === comment.id"
                      class="bg-green-500 text-white p-2 rounded-lg hover:bg-green-600 transition-all duration-300 disabled:bg-gray-400"
                    >
                      {{ loading.comments.approve === comment.id ? 'Approving...' : 'Approve' }}
                    </button>
                    <button
                      @click="deleteComment(comment)"
                      :disabled="loading.comments.delete === comment.id"
                      class="bg-red-500 text-white p-2 rounded-lg hover:bg-red-600 transition-all duration-300 disabled:bg-gray-400"
                    >
                      {{ loading.comments.delete === comment.id ? 'Deleting...' : 'Delete' }}
                    </button>
                  </div>
                </div>
              </li>
            </ul>
          </section>

          <!-- Analytics Section -->
          <section v-if="activeTab === 'Analytics'" class="space-y-6">
            <div class="bg-white p-6 rounded-xl shadow-md">
              <h2 class="text-xl font-semibold text-gray-800 mb-4">Book Downloads</h2>
              <BarChart :data="bookDownloadsData" :options="chartOptions" />
            </div>
            <div class="bg-white p-6 rounded-xl shadow-md">
              <h2 class="text-xl font-semibold text-gray-800 mb-4">User Growth</h2>
              <LineChart :data="userGrowthData" :options="chartOptions" />
            </div>
          </section>

          <!-- Settings Section -->
          <section v-if="activeTab === 'Settings'" class="bg-white p-6 rounded-xl shadow-md">
            <h2 class="text-xl font-semibold text-gray-800 mb-4">App Settings</h2>
            <form @submit.prevent="updateSettings" class="space-y-4">
              <div>
                <label class="block text-sm text-gray-600 mb-1">Max File Size for Books (MB)</label>
                <input
                  v-model.number="settings.maxBookFileSize"
                  type="number"
                  required
                  class="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-transparent"
                />
              </div>
              <div>
                <label class="block text-sm text-gray-600 mb-1">Max File Size for Audio Books (MB)</label>
                <input
                  v-model.number="settings.maxAudioBookFileSize"
                  type="number"
                  required
                  class="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-transparent"
                />
              </div>
              <div>
                <label class="block text-sm text-gray-600 mb-1">Max File Size for Thumbnails (MB)</label>
                <input
                  v-model.number="settings.maxThumbnailSize"
                  type="number"
                  required
                  class="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-transparent"
                />
              </div>
              <button
                type="submit"
                :disabled="loading.settings"
                class="w-full bg-indigo-500 text-white p-3 rounded-lg hover:bg-indigo-600 transition-all duration-300 disabled:bg-gray-400"
              >
                {{ loading.settings ? 'Saving...' : 'Save Settings' }}
              </button>
            </form>
          </section>

          <!-- Profile Section -->
          <section v-if="activeTab === 'Profile'" class="bg-white p-6 rounded-xl shadow-md">
            <h2 class="text-xl font-semibold text-gray-800 mb-4">User Profile</h2>
            <form @submit.prevent="updateProfile" class="space-y-4">
              <div>
                <label class="block text-sm text-gray-600 mb-1">Name</label>
                <input
                  v-model="profile.name"
                  placeholder="Your Name"
                  required
                  :disabled="loading.profile"
                  class="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-transparent"
                />
              </div>
              <div>
                <label class="block text-sm text-gray-600 mb-1">Email</label>
                <input
                  v-model="profile.email"
                  placeholder="Your Email"
                  type="email"
                  required
                  :disabled="loading.profile"
                  class="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-transparent"
                />
              </div>
              <div>
                <label class="block text-sm text-gray-600 mb-1">New Password (Leave blank to keep current)</label>
                <input
                  v-model="profile.password"
                  placeholder="New Password"
                  type="password"
                  :disabled="loading.profile"
                  class="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-transparent"
                />
              </div>
              <button
                type="submit"
                :disabled="loading.profile"
                class="w-full bg-indigo-500 text-white p-3 rounded-lg hover:bg-indigo-600 transition-all duration-300 disabled:bg-gray-400"
              >
                {{ loading.profile ? 'Saving...' : 'Update Profile' }}
              </button>
            </form>
          </section>
        </div>
      </transition>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { Bar, Line } from 'vue-chartjs';
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, LineElement, CategoryScale, LinearScale, PointElement } from 'chart.js';

ChartJS.register(Title, Tooltip, Legend, BarElement, LineElement, CategoryScale, LinearScale, PointElement);

export default {
  components: {
    BarChart: Bar,
    LineChart: Line,
  },
  props: {
    users: Array,
    books: Array,
    audioBooks: Array,
    videos: Array,
    categories: Array,
    comments: Array,
    authUser: Object, // Current authenticated user
  },
  data() {
    return {
      activeTab: 'Dashboard',
      tabs: ['Dashboard', 'Categories', 'Books', 'Audio Books', 'Videos', 'Users', 'Comments', 'Analytics', 'Settings', 'Profile'],
      newUser: { name: '', email: '', password: '', role: '' },
      newBook: { title: '', description: '', file: null, thumbnail: null, category_id: '' },
      newAudioBook: { title: '', file: null, thumbnail: null, category_id: '' },
      newVideo: { title: '', file_url: '', thumbnail: '', category_id: '' },
      newCategory: { name: '' },
      commentFilter: 'all',
      loading: {
        categories: { add: false, update: null, delete: null },
        books: { add: false, update: null, delete: null },
        audioBooks: { add: false, update: null, delete: null },
        videos: { add: false, update: null, delete: null },
        users: { add: false, update: null, delete: null },
        comments: { approve: null, delete: null },
        settings: false,
        profile: false,
      },
      updateFiles: {
        bookFile: {},
        bookThumbnail: {},
        audioFile: {},
        audioThumbnail: {},
      },
      settings: {
        maxBookFileSize: 10, // Default: 10MB
        maxAudioBookFileSize: 10, // Default: 10MB
        maxThumbnailSize: 2, // Default: 2MB
      },
      profile: {
        name: this.authUser?.name || '',
        email: this.authUser?.email || '',
        password: '',
      },
      bookDownloadsData: {
        labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
        datasets: [
          {
            label: 'Book Downloads',
            backgroundColor: '#6366F1',
            data: [120, 190, 300, 500, 200, 300],
          },
        ],
      },
      userGrowthData: {
        labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
        datasets: [
          {
            label: 'User Growth',
            borderColor: '#EC4899',
            backgroundColor: 'rgba(236, 72, 153, 0.2)',
            data: [50, 100, 150, 200, 250, 300],
            fill: true,
          },
        ],
      },
      chartOptions: {
        responsive: true,
        maintainAspectRatio: false,
      },
    };
  },
  watch: {
    tabs(newTabs) {
      if (newTabs && newTabs.length > 0 && !newTabs.includes(this.activeTab)) {
        this.activeTab = newTabs[0];
      } else if (!newTabs || newTabs.length === 0) {
        this.activeTab = null;
      }
    },
  },
  methods: {
    showToast(message, type = 'success') {
      this.$toast[type](message);
    },
    confirmAction(message) {
      return window.confirm(message);
    },
    resetAddForms() {
      this.newCategory = { name: '' };
      this.newUser = { name: '', email: '', password: '', role: '' };
      this.newVideo = { title: '', file_url: '', thumbnail: '', category_id: '' };
      this.newBook = { title: '', description: '', file: null, thumbnail: null, category_id: '' };
      if (this.$refs.bookFile) this.$refs.bookFile.value = null;
      if (this.$refs.bookThumbnail) this.$refs.bookThumbnail.value = null;
      this.newAudioBook = { title: '', file: null, thumbnail: null, category_id: '' };
      if (this.$refs.audioFile) this.$refs.audioFile.value = null;
      if (this.$refs.audioThumbnail) this.$refs.audioThumbnail.value = null;
    },
    handleBookFile(event) {
      const file = event.target.files[0];
      if (file && file.size > this.settings.maxBookFileSize * 1024 * 1024) {
        this.showToast(`Book file size exceeds ${this.settings.maxBookFileSize}MB`, 'error');
        this.$refs.bookFile.value = null;
        return;
      }
      this.newBook.file = file;
    },
    handleBookThumbnail(event) {
      const file = event.target.files[0];
      if (file && file.size > this.settings.maxThumbnailSize * 1024 * 1024) {
        this.showToast(`Thumbnail size exceeds ${this.settings.maxThumbnailSize}MB`, 'error');
        this.$refs.bookThumbnail.value = null;
        return;
      }
      this.newBook.thumbnail = file;
    },
    handleAudioFile(event) {
      const file = event.target.files[0];
      if (file && file.size > this.settings.maxAudioBookFileSize * 1024 * 1024) {
        this.showToast(`Audio file size exceeds ${this.settings.maxAudioBookFileSize}MB`, 'error');
        this.$refs.audioFile.value = null;
        return;
      }
      this.newAudioBook.file = file;
    },
    handleAudioThumbnail(event) {
      const file = event.target.files[0];
      if (file && file.size > this.settings.maxThumbnailSize * 1024 * 1024) {
        this.showToast(`Thumbnail size exceeds ${this.settings.maxThumbnailSize}MB`, 'error');
        this.$refs.audioThumbnail.value = null;
        return;
      }
      this.newAudioBook.thumbnail = file;
    },
    handleUpdateBookFile(book, event) {
      const file = event.target.files[0];
      if (file && file.size > this.settings.maxBookFileSize * 1024 * 1024) {
        this.showToast(`Book file size exceeds ${this.settings.maxBookFileSize}MB`, 'error');
        this.$refs['updateBookFile_' + book.id][0].value = null;
        return;
      }
      this.$set(this.updateFiles.bookFile, book.id, file);
    },
    handleUpdateBookThumbnail(book, event) {
      const file = event.target.files[0];
      if (file && file.size > this.settings.maxThumbnailSize * 1024 * 1024) {
        this.showToast(`Thumbnail size exceeds ${this.settings.maxThumbnailSize}MB`, 'error');
        this.$refs['updateBookThumbnail_' + book.id][0].value = null;
        return;
      }
      this.$set(this.updateFiles.bookThumbnail, book.id, file);
    },
    handleUpdateAudioFile(audioBook, event) {
      const file = event.target.files[0];
      if (file && file.size > this.settings.maxAudioBookFileSize * 1024 * 1024) {
        this.showToast(`Audio file size exceeds ${this.settings.maxAudioBookFileSize}MB`, 'error');
        this.$refs['updateAudioFile_' + audioBook.id][0].value = null;
        return;
      }
      this.$set(this.updateFiles.audioFile, audioBook.id, file);
    },
    handleUpdateAudioThumbnail(audioBook, event) {
      const file = event.target.files[0];
      if (file && file.size > this.settings.maxThumbnailSize * 1024 * 1024) {
        this.showToast(`Thumbnail size exceeds ${this.settings.maxThumbnailSize}MB`, 'error');
        this.$refs['updateAudioThumbnail_' + audioBook.id][0].value = null;
        return;
      }
      this.$set(this.updateFiles.audioThumbnail, audioBook.id, file);
    },
    clearUpdateFiles(type, id) {
      if (type === 'book') {
        this.$delete(this.updateFiles.bookFile, id);
        this.$delete(this.updateFiles.bookThumbnail, id);
        if (this.$refs['updateBookFile_' + id]?.[0]) this.$refs['updateBookFile_' + id][0].value = null;
        if (this.$refs['updateBookThumbnail_' + id]?.[0]) this.$refs['updateBookThumbnail_' + id][0].value = null;
      } else if (type === 'audioBook') {
        this.$delete(this.updateFiles.audioFile, id);
        this.$delete(this.updateFiles.audioThumbnail, id);
        if (this.$refs['updateAudioFile_' + id]?.[0]) this.$refs['updateAudioFile_' + id][0].value = null;
        if (this.$refs['updateAudioThumbnail_' + id]?.[0]) this.$refs['updateAudioThumbnail_' + id][0].value = null;
      }
    },
    async performApiCall(action, loadingStateKey, successMessage, errorMessagePrefix) {
      this.loading[loadingStateKey].add = true;
      try {
        await action();
        this.showToast(successMessage);
        this.$inertia.reload({ preserveScroll: true });
        this.resetAddForms();
      } catch (error) {
        console.error(`${errorMessagePrefix}:`, error.response?.data || error.message);
        const message = error.response?.data?.message || error.message || 'An unknown error occurred.';
        this.showToast(`${errorMessagePrefix}: ${message}`, 'error');
      } finally {
        this.loading[loadingStateKey].add = false;
      }
    },
    async performItemApiCall(action, itemType, itemAction, itemId, successMessage, errorMessagePrefix) {
      this.loading[itemType][itemAction] = itemId;
      try {
        await action();
        this.showToast(successMessage);
        if (itemAction === 'update') {
          this.clearUpdateFiles(itemType, itemId);
        }
        this.$inertia.reload({ preserveScroll: true });
      } catch (error) {
        console.error(`${errorMessagePrefix} (ID: ${itemId}):`, error.response?.data || error.message);
        const message = error.response?.data?.message || error.message || 'An unknown error occurred.';
        this.showToast(`${errorMessagePrefix}: ${message}`, 'error');
      } finally {
        this.loading[itemType][itemAction] = null;
      }
    },
    async addCategory() {
      await this.performApiCall(() => axios.post('/admin/category', this.newCategory), 'categories', 'Category added!', 'Failed to add category');
      this.newCategory = { name: '' };
    },
    async updateCategory(category) {
      await this.performItemApiCall(() => axios.put(`/admin/category/${category.id}`, { name: category.name }), 'categories', 'update', category.id, `Category updated!`, 'Failed to update category');
    },
    async deleteCategory(category) {
      if (!this.confirmAction(`Delete category "${category.name}"?`)) return;
      await this.performItemApiCall(() => axios.delete(`/admin/category/${category.id}`), 'categories', 'delete', category.id, `Category deleted!`, 'Failed to delete category');
    },
    async addBook() {
      const formData = new FormData();
      formData.append('title', this.newBook.title);
      formData.append('description', this.newBook.description || '');
      formData.append('category_id', this.newBook.category_id);
      if (this.newBook.file) formData.append('file', this.newBook.file);
      if (this.newBook.thumbnail) formData.append('thumbnail', this.newBook.thumbnail);
      await this.performApiCall(() => axios.post('/admin/book', formData, { headers: { 'Content-Type': 'multipart/form-data' } }), 'books', 'Book added!', 'Failed to add book');
    },
    async updateBook(book) {
      const formData = new FormData();
      formData.append('_method', 'PUT');
      formData.append('title', book.title);
      formData.append('description', book.description || '');
      formData.append('category_id', book.category_id);
      if (this.updateFiles.bookFile[book.id]) formData.append('file', this.updateFiles.bookFile[book.id]);
      if (this.updateFiles.bookThumbnail[book.id]) formData.append('thumbnail', this.updateFiles.bookThumbnail[book.id]);
      await this.performItemApiCall(() => axios.post(`/admin/book/${book.id}`, formData, { headers: { 'Content-Type': 'multipart/form-data' } }), 'books', 'update', book.id, `Book updated!`, 'Failed to update book');
    },
    async deleteBook(book) {
      if (!this.confirmAction(`Delete book "${book.title}"?`)) return;
      await this.performItemApiCall(() => axios.delete(`/admin/book/${book.id}`), 'books', 'delete', book.id, `Book deleted!`, 'Failed to delete book');
    },
    async addAudioBook() {
      const formData = new FormData();
      formData.append('title', this.newAudioBook.title);
      formData.append('category_id', this.newAudioBook.category_id);
      if (this.newAudioBook.file) formData.append('file', this.newAudioBook.file);
      if (this.newAudioBook.thumbnail) formData.append('thumbnail', this.newAudioBook.thumbnail);
      await this.performApiCall(() => axios.post('/admin/audio-book', formData, { headers: { 'Content-Type': 'multipart/form-data' } }), 'audioBooks', 'Audio book added!', 'Failed to add audio book');
    },
    async updateAudioBook(audioBook) {
      const formData = new FormData();
      formData.append('_method', 'PUT');
      formData.append('title', audioBook.title);
      formData.append('category_id', audioBook.category_id);
      if (this.updateFiles.audioFile[audioBook.id]) formData.append('file', this.updateFiles.audioFile[audioBook.id]);
      if (this.updateFiles.audioThumbnail[audioBook.id]) formData.append('thumbnail', this.updateFiles.audioThumbnail[audioBook.id]);
      await this.performItemApiCall(() => axios.post(`/admin/audio-book/${audioBook.id}`, formData, { headers: { 'Content-Type': 'multipart/form-data' } }), 'audioBooks', 'update', audioBook.id, `Audio Book updated!`, 'Failed to update audio book');
    },
    async deleteAudioBook(audioBook) {
      if (!this.confirmAction(`Delete audio book "${audioBook.title}"?`)) return;
      await this.performItemApiCall(() => axios.delete(`/admin/audio-book/${audioBook.id}`), 'audioBooks', 'delete', audioBook.id, `Audio book deleted!`, 'Failed to delete audio book');
    },
    async addVideo() {
      await this.performApiCall(() => axios.post('/admin/video', this.newVideo), 'videos', 'Video added!', 'Failed to add video');
      this.newVideo = { title: '', file_url: '', thumbnail: '', category_id: '' };
    },
    async updateVideo(video) {
      const updateData = {
        title: video.title,
        file_url: video.file_url,
        thumbnail: video.thumbnail,
        category_id: video.category_id,
      };
      await this.performItemApiCall(() => axios.put(`/admin/video/${video.id}`, updateData), 'videos', 'update', video.id, `Video updated!`, 'Failed to update video');
    },
    async deleteVideo(video) {
      if (!this.confirmAction(`Delete video "${video.title}"?`)) return;
      await this.performItemApiCall(() => axios.delete(`/admin/video/${video.id}`), 'videos', 'delete', video.id, `Video deleted!`, 'Failed to delete video');
    },
    async addUser() {
      await this.performApiCall(() => axios.post('/admin/user', this.newUser), 'users', 'User added!', 'Failed to add user');
      this.newUser = { name: '', email: '', password: '', role: '' };
    },
    async updateUser(user) {
      const updateData = { name: user.name, email: user.email, role: user.role };
      await this.performItemApiCall(() => axios.put(`/admin/user/${user.id}`, updateData), 'users', 'update', user.id, `User updated!`, 'Failed to update user');
    },
    async deleteUser(user) {
      if (!this.confirmAction(`Delete user "${user.name}"?`)) return;
      await this.performItemApiCall(() => axios.delete(`/admin/user/${user.id}`), 'users', 'delete', user.id, `User deleted!`, 'Failed to delete user');
    },
    async fetchComments() {
      try {
        const response = await axios.get(`/admin/comments?filter=${this.commentFilter}`);
        this.comments = response.data;
      } catch (error) {
        this.showToast('Failed to fetch comments', 'error');
      }
    },
    async approveComment(comment) {
      this.loading.comments.approve = comment.id;
      try {
        await axios.put(`/admin/comment/${comment.id}/approve`);
        this.showToast('Comment approved!');
        this.$inertia.reload({ preserveScroll: true });
      } catch (error) {
        this.showToast('Failed to approve comment', 'error');
      } finally {
        this.loading.comments.approve = null;
      }
    },
    async deleteComment(comment) {
      if (!this.confirmAction(`Delete comment by "${comment.user.name}"?`)) return;
      this.loading.comments.delete = comment.id;
      try {
        await axios.delete(`/admin/comment/${comment.id}`);
        this.showToast('Comment deleted!');
        this.$inertia.reload({ preserveScroll: true });
      } catch (error) {
        this.showToast('Failed to delete comment', 'error');
      } finally {
        this.loading.comments.delete = null;
      }
    },
    async updateSettings() {
      this.loading.settings = true;
      try {
        await axios.put('/admin/settings', this.settings);
        this.showToast('Settings updated!');
      } catch (error) {
        this.showToast('Failed to update settings', 'error');
      } finally {
        this.loading.settings = false;
      }
    },
    async updateProfile() {
      this.loading.profile = true;
      try {
        const updateData = {
          name: this.profile.name,
          email: this.profile.email,
        };
        if (this.profile.password) updateData.password = this.profile.password;
        await axios.put('/admin/profile', updateData);
        this.showToast('Profile updated!');
        this.profile.password = '';
        this.$inertia.reload({ preserveScroll: true });
      } catch (error) {
        this.showToast('Failed to update profile', 'error');
      } finally {
        this.loading.profile = false;
      }
    },
    async logout() {
      if (!this.confirmAction('Are you sure you want to sign out?')) return;
      try {
        await axios.post('/logout');
        this.$inertia.visit('/login');
      } catch (error) {
        this.showToast('Failed to sign out', 'error');
      }
    },
  },
  mounted() {
    // Fetch initial settings
    axios.get('/admin/settings').then(response => {
      this.settings = response.data;
    }).catch(() => {
      this.showToast('Failed to load settings', 'error');
    });

    // Fetch comments if on Comments tab
    if (this.activeTab === 'Comments') {
      this.fetchComments();
    }
  },
};
</script>

<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>