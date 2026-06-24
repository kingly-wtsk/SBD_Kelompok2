# TUGAS UAS SISTEM BASIS DATA
Database Relasional, NoSQL, dan Vektor Database


Proyek ini merupakan Tugas Akhir UAS Mata Kuliah Basis Data yang mengimplementasikan tiga arsitektur database berbeda (Relational, NoSQL, dan Vector) untuk mengoptimalkan platform pariwisata cerdas.

## 🚀 Teknologi yang Digunakan
- **MySQL Server:** Mengelola data transaksional (User, Bookings, Payments) dengan kepatuhan prinsip ACID.
- **MongoDB:** Mengelola katalog destinasi wisata berskema dinamis (*schema-less*) menggunakan teknik dokumen bersarang (*embedded*).
- **Pinecone Vector Database:** Membangun fitur pencarian semantik cerdas (*AI Similarity Search*) berbasis *Cosine Similarity* menggunakan Python.

## 📁 Struktur Repository
- `/mysql` : Script DDL, DML, dan query CRUD Relasional.
- `/mongodb` : Script inisialisasi koleksi dan operasi CRUD NoSQL.
- `/vektor_pinecone` : Kode implementasi Vector Embedding dan Similarity Search.
- `/docs` : Laporan proyek format PDF dan Slide Presentasi.
