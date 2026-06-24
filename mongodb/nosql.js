// INITIALIZATION & SEED DATA (CREATE MANY)
use smart_tourism_sulut_nosql;

db.destinations.drop();

db.destinations.insertMany([
  {
    "name": "Pulau Lembeh",
    "location": "Bitung, Sulawesi Utara",
    "category": "Wisata Alam & Bahari",
    "price_ticket": 25000,
    "facilities": ["Muck Diving Center", "Resort Tradisional", "Sewa Perahu Katinting"],
    "metadata": {
      "biota_unggulan": "Mimic Octopus, Pygmy Seahorse",
      "jenis_selam": "Muck Diving"
    },
    "reviews": [
      { "username": "Gerry_Maramis", "rating": 5, "comment": "Surga bagi fotografer makro bawah laut!", "created_at": new Date() }
    ]
  },
  {
    "name": "Danau Linow",
    "location": "Tomohon, Sulawesi Utara",
    "category": "Wisata Alam",
    "price_ticket": 35000,
    "facilities": ["Cafeteria Tepi Danau", "Spot Foto Belerang", "Area Parkir Aman"],
    "metadata": {
      "keunikan": "Danau yang dapat berubah menjadi 3 warna berbeda",
      "suhu_rata_rata": "20°C"
    },
    "reviews": []
  }
]);

// OPERASI CRUD (MONGOSH)
// 1. Create (Insert One)
db.destinations.insertOne({
  "name": "Pantai Paal",
  "location": "Minahasa Utara, Sulawesi Utara",
  "category": "Wisata Alam & Bahari",
  "price_ticket": 20000,
  "facilities": ["Gazebo Tepi Pantai", "Sewa Banana Boat"],
  "metadata": { "keunggulan": "Pasir putih halus", "status_wilayah": "KEK Likupang" },
  "reviews": []
});

// 2. Read All
db.destinations.find().pretty();

// 3. Read Specific
db.destinations.find({ "name": "Pantai Paal" }).pretty();

// 4. Update Field
db.destinations.updateOne({ "name": "Pantai Paal" }, { $set: { "price_ticket": 50000 } });

// 5. Update Array (Push Review)
db.destinations.updateOne({ "name": "Pulau Lembeh" }, { $push: { "reviews": { "username": "Wulan_K", "rating": 5, "comment": "Bawah lautnya mempesona!", "created_at": new Date() } } });

// 6. Delete One
db.destinations.deleteOne({ "name": "Pantai Paal" });