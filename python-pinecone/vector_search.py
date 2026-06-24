import os
from pinecone import Pinecone, ServerlessSpec
from sentence_transformers import SentenceTransformer

# 1. Inisialisasi API Key Pinecone
PINECONE_API_KEY = "pcsk_6ioGM2_Gd92Mznjxt14ZJe4XQ2BTCHt4UVykfjg1v9gguF3oWNcvg57U2fGJY3bcF7GBwx"
pc = Pinecone(api_key=PINECONE_API_KEY)

# 2. Load Model Embedding Multi-Bahasa (Support Bahasa Indonesia)
print("Sedang memuat model embedding multi-bahasa di laptop...")
model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')

# 3. Dataset Lengkap (50 Artikel)
articles = [
    {"id": "1", "title": "Perkembangan Artificial Intelligence", "desc": "Kecerdasan buatan kini mampu membantu dokter mendiagnosis penyakit kronis dengan akurasi tinggi melalui analisis citra medis."},
    {"id": "2", "title": "Tips Diet Sehat Tanpa Obat", "desc": "Mengonsumsi makanan tinggi serat seperti sayur dan buah serta rutin minum air putih dapat menurunkan berat badan secara alami."},
    {"id": "3", "title": "Metode Pembelajaran Blended Learning", "desc": "Kombinasi antara kelas tatap muka dan pembelajaran daring terbukti meningkatkan pemahaman mahasiswa di era digital."},
    {"id": "4", "title": "Latihan Fisik Kardio untuk Jantung", "desc": "Olahraga seperti lari pagi, berenang, dan bersepeda sangat baik untuk menjaga kesehatan kardiovaskular dan stamina tubuh."},
    {"id": "5", "title": "Keamanan Data di Era Cloud Computing", "desc": "Enkripsi end-to-end dan autentikasi dua faktor menjadi pilar utama dalam melindungi data sensitif di server awan."},
    {"id": "6", "title": "Pentingnya Sarapan Bagi Anak Sekolah", "desc": "Mengonsumsi makanan bergizi di pagi hari memberikan energi dan meningkatkan konsentrasi belajar anak di kelas."},
    {"id": "7", "title": "Kenaikan Tren Sepak Bola Wanita", "desc": "Kompetisi sepak bola wanita kini mendapatkan perhatian luas dan hak siar televisi yang setara dengan liga pria."},
    {"id": "8", "title": "Mengenal Teknologi Blockchain", "desc": "Sistem basis data terdesentralisasi ini tidak hanya digunakan untuk kripto, tetapi juga untuk transparansi rantai pasok global."},
    {"id": "9", "title": "Gejala Burnt Out pada Pekerja", "desc": "Stres kerja yang berkepanjangan dapat menyebabkan kelelahan mental, penurunan produktivitas, dan hilangnya motivasi diri."},
    {"id": "10", "title": "Manfaat Yoga untuk Kesehatan Mental", "desc": "Olahraga meditasi seperti yoga membantu mengurangi hormon kortisol, meredakan kecemasan, dan menenangkan pikiran."},
    {"id": "11", "title": "Beasiswa Kuliah di Luar Negeri", "desc": "Pemerintah menyediakan berbagai bantuan finansial bagi mahasiswa berprestasi yang ingin melanjutkan studi ke Eropa dan Amerika."},
    {"id": "12", "title": "Pengembangan Framework Web Modern", "desc": "Framework berbasis komponen memudahkan developer membangun antarmuka aplikasi web yang reaktif, cepat, dan interaktif."},
    {"id": "13", "title": "Bahaya Kurang Tidur Bagi Tubuh", "desc": "Sering begadang dapat melemahkan sistem imun, mengganggu fungsi otak, dan meningkatkan risiko obesitas."},
    {"id": "14", "title": "Strategi Pemasaran Digital UMKM", "desc": "Memanfaatkan media sosial dan optimasi SEO lokal membantu pelaku usaha kecil menjangkau pasar yang jauh lebih luas."},
    {"id": "15", "title": "Kurikulum Merdeka di Sekolah", "desc": "Sistem pendidikan baru ini memberikan kebebasan bagi siswa untuk memilih mata pelajaran sesuai dengan minat dan bakat mereka."},
    {"id": "16", "title": "Sejarah Olimpiade Modern", "desc": "Ajang olahraga terbesar di dunia ini menjadi simbol perdamaian dan persatuan antar negara yang diselenggarakan setiap empat tahun."},
    {"id": "17", "title": "Dasar-Dasar Machine Learning", "desc": "Algoritma komputer yang mempelajari pola dari data masa lalu untuk melakukan prediksi atau keputusan otomatis tanpa pemrograman eksplisit."},
    {"id": "18", "title": "Manfaat Infused Water", "desc": "Minuman air putih yang dicampur potongan buah segar membantu proses detoksifikasi racun di dalam tubuh secara alami."},
    {"id": "19", "title": "Pendidikan Inklusif Bagi Difabel", "desc": "Sekolah inklusi memastikan setiap anak berkebutuhan khusus mendapatkan hak dan fasilitas belajar yang setara dengan siswa lainnya."},
    {"id": "20", "title": "Teknik Dasar Bermain Basket", "desc": "Menguasai kemampuan dribbling, passing, dan shooting yang benar sangat krusial untuk memenangkan pertandingan bola basket."},
    {"id": "21", "title": "Keamanan Siber pada Internet of Things (IoT)", "desc": "Perangkat pintar di rumah rentan terhadap peretasan jika tidak dilengkapi dengan pembaruan firmware berkala dan password yang kuat."},
    {"id": "22", "title": "Penerapan Virtual Reality dalam Industri Game", "desc": "Teknologi VR memberikan pengalaman bermain yang imersif, membuat pemain merasa benar-benar berada di dalam dunia simulasi tersebut."},
    {"id": "23", "title": "Masa Depan Kendaraan Listrik Otomatis", "desc": "Mobil listrik yang dilengkapi dengan sistem self-driving diprediksi akan mengurangi angka kecelakaan lalu lintas akibat kelalaian manusia."},
    {"id": "24", "title": "Komputasi Kuantum dan Kecepatan Data", "desc": "Quantum computing menggunakan prinsip fisika kuantum untuk memecahkan masalah matematika kompleks jutaan kali lebih cepat dari superkomputer biasa."},
    {"id": "25", "title": "Evolusi Jaringan Seluler 5G ke 6G", "desc": "Pengembangan teknologi 6G menjanjikan kecepatan internet terabit per detik dengan latensi mikrodetik untuk mendukung komunikasi holografis."},
    {"id": "26", "title": "Pentingnya Menjaga Kesehatan Mata", "desc": "Menatap layar gawai terlalu lama dapat menyebabkan mata lelah. Terapkan aturan 20-20-20 untuk menjaga fleksibilitas otot mata."},
    {"id": "27", "title": "Manfaat Pola Makan Intermittent Fasting", "desc": "Metode puasa berkala ini efektif untuk membakar lemak tubuh, memperbaiki sensitivitas insulin, dan mendukung regenerasi sel."},
    {"id": "28", "title": "Bahaya Konsumsi Gula Berlebih", "desc": "Terlalu banyak mengonsumsi makanan dan minuman manis dapat memicu diabetes tipe 2, obesitas, serta kerusakan pada gigi."},
    {"id": "29", "title": "Pentingnya Vaksinasi bagi Imunitas Anak", "desc": "Pemberian imunisasi dasar secara lengkap melindungi balita dari berbagai penyakit menular berbahaya seperti campak dan polio."},
    {"id": "30", "title": "Cara Mengatasi Insomnia Akut", "desc": "Menciptakan suasana kamar yang tenang, menghindari kafein di malam hari, dan mematikan lampu dapat membantu memperbaiki kualitas tidur."},
    {"id": "31", "title": "Pentingnya Literasi Digital Sejak Dini", "desc": "Mengajarkan anak-anak cara memilah informasi valid dan hoaks di internet sangat penting agar mereka bijak dalam berselancar di dunia maya."},
    {"id": "32", "title": "Penerapan Gamifikasi dalam Kelas", "desc": "Mengubah materi pelajaran menjadi elemen permainan terbukti meningkatkan motivasi dan keterlibatan aktif siswa saat belajar."},
    {"id": "33", "title": "Manfaat Menguasai Bahasa Asing", "desc": "Bisa berbahasa internasional seperti Inggris atau Mandarin membuka peluang karier yang lebih luas dan mempermudah studi global."},
    {"id": "34", "title": "Pendidikan Karakter di Sekolah Dasar", "desc": "Selain nilai akademik, penanaman nilai kejujuran, disiplin, dan toleransi menjadi fondasi utama dalam membentuk kepribadian anak."},
    {"id": "35", "title": "Tips Lolos Ujian Ujian Masuk PTN", "desc": "Konsistensi dalam berlatih soal-soal tahun lalu (try out) serta manajemen waktu yang baik adalah kunci sukses menembus kampus impian."},
    {"id": "36", "title": "Pentingnya Pemanasan Sebelum Olahraga", "desc": "Melakukan peregangan dinamis sebelum latihan fisik berguna untuk meningkatkan suhu tubuh dan mencegah cedera otot yang parah."},
    {"id": "37", "title": "Teknik Lari Jarak Jauh (Maraton)", "desc": "Pelari maraton harus menjaga ritme langkah, mengatur pola napas, dan memastikan hidrasi tubuh terjaga sepanjang lintasan."},
    {"id": "38", "title": "Manfaat Latihan Beban bagi Lansia", "desc": "Latihan beban dengan intensitas disesuaikan membantu menjaga kepadatan tulang dan mencegah pengeroposan sendi pada usia tua."},
    {"id": "39", "title": "Popularitas Olahraga Bulu Tangkis", "desc": "Bulu tangkis membutuhkan refleks cepat, kelincahan kaki, dan kekuatan smes yang akurat untuk mematikan pergerakan lawan di lapangan."},
    {"id": "40", "title": "Pertumbuhan Ekosistem Esport Global", "desc": "Game kompetitif kini telah diakui sebagai cabang olahraga resmi yang menawarkan hadiah turnamen hingga jutaan dolar."},
    {"id": "41", "title": "Pentingnya Investasi Sejak Muda", "desc": "Menyisihkan uang untuk saham atau reksa dana sejak dini memanfaatkan efek compounding interest demi kebebasan finansial di masa depan."},
    {"id": "42", "title": "Tips Mengelola Gaji Bulanan", "desc": "Gunakan rumus 50-30-20, yaitu setengah pendapatan untuk kebutuhan pokok, tiga puluh persen keinginan, dan sisanya untuk tabungan darurat."},
    {"id": "43", "title": "Mengenal Inflasi dan Dampaknya", "desc": "Kenaikan harga barang secara umum menyebabkan daya beli mata uang menurun, sehingga pengelolaan aset harus lebih cermat."},
    {"id": "44", "title": "Keuntungan Bisnis Franchise", "desc": "Membuka waralaba meminimalkan risiko gagal karena sistem operasional dan merek dagang sudah matang serta dikenal luas oleh konsumen."},
    {"id": "45", "title": "Mengenal Sistem Paylater dan Risikonya", "desc": "Fitur belanja sekarang bayar nanti menawarkan kemudahan, namun jika tidak kontrol dapat menjebak pengguna dalam lilitan utang."},
    {"id": "46", "title": "Dampak Buruk Sampah Plastik di Laut", "desc": "Mikroplastik yang tertelan oleh ikan dapat merusak ekosistem laut dan berisiko masuk ke dalam rantai makanan manusia."},
    {"id": "47", "title": "Pemanfaatan Energi Surya", "desc": "Panel surya mengubah sinar matahari menjadi listrik ramah lingkungan, menjadi solusi alternatif untuk mengurangi ketergantungan pada batu bara."},
    {"id": "48", "title": "Gerakan Zero Waste di Rumah Tangga", "desc": "Mengurangi penggunaan plastik sekali pakai dan mengolah sampah organik menjadi kompos dapat menekan volume sampah di TPA."},
    {"id": "49", "title": "Pentingnya Reboisasi Hutan Gundul", "desc": "Menanam kembali pohon di lahan kritis berfungsi mencegah bencana tanah longsor, banjir bandang, serta menjaga ketersediaan air tanah."},
    {"id": "50", "title": "Fenomena Pemanasan Global", "desc": "Meningkatnya gas rumah kaca memicu kenaikan suhu bumi, mencairnya es kutub, dan perubahan cuaca ekstrem di berbagai belahan dunia."}
]

# 4. Membuat Index Pinecone Baru (Dimensi 384)
index_name = "pencarian-artikel-multibahasa"
if index_name not in pc.list_indexes().names():
    print(f"Membuat index baru '{index_name}' di Pinecone...")
    pc.create_index(
        name=index_name,
        dimension=384,  # Mengikuti dimensi model SentenceTransformer
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1")
    )

index = pc.Index(index_name)

# --- FUNGSI EMBEDDING ---
def get_embedding(text):
    embedding = model.encode(text)
    return embedding.tolist()

# --- PROSES UPLOAD ---
print("Sedang memproses embedding untuk 50 artikel dan mengunggah ke Pinecone...")
vectors_to_upsert = []
for art in articles:
    combined_text = f"{art['title']}. {art['desc']}"
    embedding = get_embedding(combined_text)
    
    vectors_to_upsert.append({
        "id": art["id"],
        "values": embedding,
        "metadata": {"title": art["title"], "desc": art["desc"]}
    })

# Unggah data ke Pinecone
index.upsert(vectors=vectors_to_upsert)
print("Seluruh data (50 artikel) berhasil disimpan ke Pinecone!\n")

# --- FUNGSI PENCARIAN ---
def search_article(query, top_k=1):
    query_embedding = get_embedding(query)
    results = index.query(
        vector=query_embedding,
        top_k=top_k,
        include_metadata=True
    )
    
    print(f"Keyword Pencarian: '{query}'")
    print("-" * 50)
    for match in results['matches']:
        print(f"Skor Kemiripan: {match['score']:.4f}")
        print(f"Judul: {match['metadata']['title']}")
        print(f"Deskripsi: {match['metadata']['desc']}")
        print()
    print("=" * 50 + "\n")

# --- PENGUJIAN OTOMATIS ---
test_queries = [
    "sumber daya alam yang tidak habis",        
    "cedera saat beraktivitas fisik",           
    "cara mengatur uang agar tidak boros",       
    "teknologi masa depan pengganti bensin",    
    "susah memejamkan mata di malam hari"       
]

for q in test_queries:
    search_article(q, top_k=1)