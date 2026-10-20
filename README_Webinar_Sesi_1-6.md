# Studi Kasus Webinar Informatika Sesi 1--6

Dokumentasi ini merangkum enam studi kasus implementasi yang
dikembangkan berdasarkan materi webinar Informatics Practitioner Lecture
Series. Setiap studi kasus menghubungkan materi pemateri dengan contoh
penerapan sederhana menggunakan pemrograman atau visualisasi.

## Daftar Isi

1.  [Sesi 1 --- Analitik Data dan Machine
    Learning](#sesi-1--analitik-data-dan-machine-learning)
2.  [Sesi 2 --- High Performance Computing untuk Prediksi
    Banjir](#sesi-2--high-performance-computing-untuk-prediksi-banjir)
3.  [Sesi 3 --- Geographic Information
    System](#sesi-3--geographic-information-system)
4.  [Sesi 4 --- Introduction to Machine
    Learning](#sesi-4--introduction-to-machine-learning)
5.  [Sesi 5 --- Interaksi Manusia dan Komputer serta Visualisasi
    Data](#sesi-5--interaksi-manusia-dan-komputer-serta-visualisasi-data)
6.  [Sesi 6 --- Pemantauan Deforestasi dengan
    AI](#sesi-6--pemantauan-deforestasi-dengan-ai)

------------------------------------------------------------------------

## Sesi 1 --- Analitik Data dan Machine Learning

**Studi kasus:** Prediksi Keterlambatan Pembayaran Invoice Menggunakan
Machine Learning

Studi kasus ini terinspirasi dari materi tentang pemanfaatan analitik
data dan AI untuk mengubah data transaksi menjadi informasi yang
membantu pengambilan keputusan. Contoh kasusnya adalah perusahaan fiktif
PT Maju Bersama yang ingin mengetahui faktor yang berkaitan dengan
keterlambatan pembayaran invoice.

**Implementasi:** - Bahasa: Python. - Pustaka: Pandas dan
scikit-learn. - Metode: Random Forest untuk mengklasifikasikan
kemungkinan keterlambatan pembayaran. - Data: dataset transaksi buatan
atau dataset publik yang sesuai, setelah disesuaikan dengan tujuan studi
kasus. - Evaluasi: accuracy, precision, dan recall.

**Hasil yang diharapkan:** Model menghasilkan prediksi keterlambatan
pembayaran yang dapat menjadi bahan analisis awal. Prediksi bukan
pengganti pemeriksaan dan keputusan manusia.

**Berkas yang disarankan:** `prediksi_invoice.ipynb` atau
`prediksi_invoice.py`, dataset yang digunakan, dan `README.md`.

------------------------------------------------------------------------

## Sesi 2 --- High Performance Computing untuk Prediksi Banjir

**Studi kasus:** Simulasi Risiko Banjir Berdasarkan Curah Hujan dan
Tinggi Air

Materi High Performance Computing (HPC) membahas penggunaan kemampuan
komputasi untuk membantu menyelesaikan persoalan yang membutuhkan
pemrosesan data besar atau perhitungan intensif. Salah satu contoh
penerapannya adalah analisis risiko banjir.

**Implementasi:** - Bahasa: Python. - Data: data simulasi curah hujan
dan tinggi air untuk beberapa lokasi. - Proses: mengelompokkan kondisi
menjadi risiko rendah, sedang, atau tinggi berdasarkan ambang batas
sederhana. - Berkas utama: `prediksi_banjir.py`.

**Hasil yang diharapkan:** Program menampilkan perkiraan kategori risiko
dari data simulasi. Implementasi ini merupakan demonstrasi sederhana,
bukan sistem peringatan banjir operasional; penggunaan nyata memerlukan
data terukur dan validasi ahli.

------------------------------------------------------------------------

## Sesi 3 --- Geographic Information System

**Studi kasus:** Pemetaan Lokasi Fasilitas Umum di Kota Bengkulu
Menggunakan Python

Geographic Information System (GIS) digunakan untuk menyimpan, mengolah,
dan menampilkan informasi yang memiliki lokasi geografis. Studi kasus
ini menampilkan beberapa titik fasilitas umum pada peta interaktif.

**Implementasi:** - Bahasa: Python. - Pustaka: Folium. - Proses: membuat
peta, menambahkan penanda lokasi, lalu menyimpan hasil sebagai HTML. -
Berkas utama: `peta_bengkulu.py`. - Keluaran: `peta_bengkulu.html`.

**Hasil yang diharapkan:** Pengguna dapat membuka peta interaktif
melalui browser dan melihat titik lokasi yang ditampilkan. Koordinat
contoh perlu diverifikasi sebelum digunakan sebagai informasi lokasi
sebenarnya.

------------------------------------------------------------------------

## Sesi 4 --- Introduction to Machine Learning

**Studi kasus:** Prediksi Nilai Mahasiswa Berdasarkan Jam Belajar

Studi kasus ini memperkenalkan konsep dasar machine learning melalui
hubungan antara jumlah jam belajar dan nilai mahasiswa. Model
mempelajari pola sederhana dari data contoh, kemudian memperkirakan
nilai untuk jumlah jam belajar tertentu.

**Implementasi:** - Bahasa: Python. - Pustaka: scikit-learn dan
Matplotlib. - Metode: Linear Regression. - Data contoh: jam belajar 1--6
jam dengan nilai 50, 55, 65, 70, 80, dan 85. - Pengujian contoh:
memprediksi nilai untuk 7 jam belajar dan menampilkan grafik.

**Berkas yang disarankan:** `prediksi_nilai.ipynb` atau
`prediksi_nilai.py`.

**Hasil yang diharapkan:** Program menghasilkan estimasi nilai dan
grafik hubungan jam belajar dengan nilai. Data ini hanya contoh kecil
untuk pembelajaran, bukan alat untuk menentukan nilai mahasiswa
sebenarnya.

------------------------------------------------------------------------

## Sesi 5 --- Interaksi Manusia dan Komputer serta Visualisasi Data

**Studi kasus:** Dashboard Nilai Mahasiswa yang Interaktif

Studi kasus ini menerapkan prinsip Interaksi Manusia dan Komputer (IMK)
dan visualisasi data untuk menyajikan informasi nilai mahasiswa secara
lebih mudah dibaca. Dashboard menampilkan ringkasan nilai dan grafik
sehingga pengguna dapat memahami data dengan cepat.

**Implementasi:** - Teknologi: HTML, CSS, JavaScript, dan Chart.js. -
Data contoh: nilai beberapa mahasiswa. - Fitur: grafik batang, filter
mahasiswa, jumlah mahasiswa, nilai rata-rata, dan nilai tertinggi. -
Berkas: `index.html`, `style.css`, dan `script.js`.

**Hasil yang diharapkan:** Dashboard dapat dibuka di browser dan
membantu pengguna mengeksplorasi data. Antarmuka dibuat sederhana,
konsisten, dan mudah digunakan. Proyek dapat dipublikasikan melalui
GitHub Pages.

------------------------------------------------------------------------

## Sesi 6 --- Pemantauan Deforestasi dengan AI

**Studi kasus:** Klasifikasi Penyebab Deforestasi Menggunakan Citra
Satelit dan Machine Learning

Studi kasus ini mengangkat pemanfaatan AI dan citra satelit untuk
membantu pemantauan deforestasi. Model klasifikasi gambar digunakan
untuk mengenali kategori penyebab perubahan tutupan hutan berdasarkan
citra berlabel.

**Implementasi:** - Bahasa: Python. - Pustaka: PyTorch dan
torchvision. - Metode: Convolutional Neural Network (CNN), misalnya
ResNet18. - Data: dataset ForestNet atau dataset citra berlabel lain
yang sesuai. - Proses: menyiapkan data gambar, membagi data latih dan
pengujian, melatih model, lalu mengevaluasi hasil klasifikasi. - Berkas
yang disarankan: `main.py`, `requirements.txt`, dan `README.md`; model
hasil pelatihan dapat disimpan sebagai `model_deforestasi.pth`.

**Hasil yang diharapkan:** Model menghasilkan prediksi kelas pada citra
uji. Akurasi dan keterbatasan model perlu dilaporkan; hasil AI sebaiknya
digunakan sebagai bantuan pemantauan, bukan satu-satunya dasar keputusan
lingkungan.

------------------------------------------------------------------------

## Teknologi yang Digunakan

  -----------------------------------------------------------------------
  Sesi                    Teknologi utama         Fokus
  ----------------------- ----------------------- -----------------------
  1                       Python, Pandas,         Analitik transaksi dan
                          scikit-learn            prediksi keterlambatan

  2                       Python                  Simulasi risiko banjir
                                                  dan konsep HPC

  3                       Python, Folium          Peta lokasi interaktif

  4                       Python, scikit-learn,   Regresi dan prediksi
                          Matplotlib              nilai

  5                       HTML, CSS, JavaScript,  Dashboard dan
                          Chart.js                visualisasi data

  6                       Python, PyTorch,        Klasifikasi citra untuk
                          torchvision             pemantauan deforestasi
  -----------------------------------------------------------------------

## Cara Menjalankan

Langkah menjalankan setiap proyek dapat berbeda sesuai berkas dan
dependensinya:

1.  Buka folder proyek yang ingin dijalankan.
2.  Baca petunjuk pada folder atau notebook terkait.
3.  Untuk proyek Python, siapkan Python dan instal pustaka yang
    diperlukan.
4.  Untuk dashboard sesi 5, buka `index.html` menggunakan browser.
5.  Untuk proyek yang menggunakan dataset, pastikan dataset tersedia di
    lokasi yang sesuai dan ikuti ketentuan lisensinya.

## Catatan

-   Data simulasi atau data contoh digunakan hanya untuk pembelajaran.
-   Jika memakai dataset publik, cantumkan sumber dataset dan patuhi
    lisensinya.
-   Hasil implementasi bergantung pada kualitas data, metode, dan
    pengujian.
-   Studi kasus ini merupakan implementasi pembelajaran yang
    terinspirasi dari materi webinar, bukan reproduksi penuh sistem
    industri.
