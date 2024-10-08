

Nama: [Ali Al Uraydhi]
Kelas: [PBP A]

Aplikasi ini adalah sistem inventaris sederhana yang memungkinkan pengguna untuk menambah, melihat, dan mengelola item dalam inventaris.

Manfaat Penggunaan JavaScript dalam Pengembangan Aplikasi Web

JavaScript memberikan beberapa manfaat penting dalam pengembangan aplikasi web:

1. Interaktivitas: JavaScript memungkinkan pembuatan elemen interaktif pada halaman web, seperti formulir dinamis, animasi, dan pembaruan konten tanpa perlu me-refresh halaman.

2. Pengalaman Pengguna yang Lebih Baik: Dengan JavaScript, kita dapat membuat aplikasi web yang responsif dan cepat, meningkatkan pengalaman pengguna secara keseluruhan.

3. Pengembangan Sisi Klien: JavaScript memungkinkan logika aplikasi dijalankan di sisi klien, mengurangi beban server dan mempercepat respons aplikasi.

4. Kompatibilitas Lintas Platform: JavaScript berjalan di semua browser modern, memastikan konsistensi fungsionalitas di berbagai perangkat dan platform.

5. Ekosistem yang Kaya: JavaScript memiliki banyak library dan framework yang memudahkan pengembangan aplikasi web yang kompleks.

Fungsi `await` pada `fetch()`

Penggunaan `await` dengan `fetch()` memiliki fungsi penting:

1. Sinkronisasi Asinkron: `await` membuat kode asinkron terlihat seperti kode sinkron, membuatnya lebih mudah dibaca dan dipahami.

2. Menunggu Respons: `await` menunda eksekusi kode berikutnya sampai promise dari `fetch()` diselesaikan, memastikan bahwa kita memiliki respons sebelum melanjutkan.

Jika kita tidak menggunakan `await`:

1. Kode akan terus dieksekusi tanpa menunggu respons dari `fetch()`.
2. Kita harus menggunakan metode `.then()` untuk menangani respons, yang dapat menyebabkan "callback hell" jika ada banyak operasi asinkron berurutan.
3. Penanganan kesalahan menjadi lebih rumit karena kita perlu menggunakan `.catch()` untuk setiap promise.

Penggunaan Decorator `csrf_exempt`

Kita perlu menggunakan decorator `csrf_exempt` pada view yang akan digunakan untuk AJAX POST karena:

1. CSRF Protection: Django secara default mengaktifkan perlindungan CSRF untuk semua view yang menerima metode POST.

2. AJAX Requests: Permintaan AJAX yang dibuat oleh JavaScript sering kali tidak menyertakan token CSRF yang diperlukan.

3. Pengecualian untuk API: Untuk endpoint API yang diakses melalui AJAX, kita mungkin ingin menonaktifkan perlindungan CSRF untuk memudahkan akses.

Namun, penting untuk dicatat bahwa menonaktifkan perlindungan CSRF harus dilakukan dengan hati-hati dan hanya pada endpoint yang aman untuk melakukannya.

Pembersihan Data Input di Backend

Pembersihan data input dilakukan di backend (selain di frontend) karena beberapa alasan:

1. Keamanan: Frontend dapat dengan mudah dimanipulasi oleh pengguna. Pembersihan di backend memberikan lapisan keamanan tambahan.

2. Konsistensi: Backend dapat memastikan bahwa semua data yang masuk ke database telah dibersihkan, terlepas dari sumber inputnya (web, mobile app, API).

3. Validasi Kompleks: Beberapa validasi mungkin memerlukan akses ke database atau logika kompleks yang lebih baik ditangani di backend.

4. Pencegahan Bypass: Pengguna yang mahir dapat melewati validasi frontend, sehingga validasi backend menjadi penting.

Implementasi Checklist

Berikut adalah langkah-langkah implementasi checklist:

1. Membuat Fungsi untuk Mengambil Data JSON:
   - Buat fungsi baru di `views.py` untuk mengembalikan data dalam format JSON.
   - Gunakan `serializers` untuk mengubah objek model menjadi JSON.

2. Membuat Fungsi View Baru untuk Menambahkan Item:
   - Buat fungsi view baru di `views.py` yang menerima data POST.
   - Implementasikan logika untuk membuat objek baru dari data yang diterima.

3. Membuat Path `/create-ajax/` untuk Menambahkan Item Baru:
   - Tambahkan URL pattern baru di `urls.py` yang mengarah ke fungsi view yang baru dibuat.

4. Mengimplementasikan AJAX GET:
   - Buat fungsi JavaScript yang menggunakan `fetch()` untuk mengambil data dari server.
   - Perbarui halaman HTML dengan data yang diterima tanpa reload halaman.

5. Mengimplementasikan AJAX POST:
   - Buat form di HTML untuk input data item baru.
   - Implementasikan fungsi JavaScript yang mengirim data form menggunakan `fetch()` dengan metode POST.
   - Perbarui tabel item secara dinamis setelah item baru ditambahkan.

6. Melakukan Perintah `collectstatic`:
   - Jalankan perintah `python manage.py collectstatic` untuk mengumpulkan file statis.
   - Pastikan setting `STATIC_ROOT` dan `STATIC_URL` sudah dikonfigurasi dengan benar di `settings.py`.

Setiap langkah di atas memerlukan pemahaman tentang Django, JavaScript, dan AJAX. Pastikan untuk menguji setiap fitur setelah diimplementasikan untuk memastikan fungsionalitasnya.
