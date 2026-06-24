-- CREATE DATABASE
CREATE DATABASE smart_tourism_sulut;
USE smart_tourism_sulut;

-- CREATE TABLES (DDL)
CREATE TABLE categories (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT
);

CREATE TABLE destinations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    category_id INT,
    name VARCHAR(150) NOT NULL,
    location VARCHAR(255) NOT NULL,
    price_ticket DECIMAL(10,2) NOT NULL,
    description TEXT,
    FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE SET NULL
);

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    role ENUM('admin', 'tourist') DEFAULT 'tourist'
);

CREATE TABLE bookings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    destination_id INT,
    booking_date DATE NOT NULL,
    quantity INT NOT NULL,
    total_price DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (destination_id) REFERENCES destinations(id) ON DELETE CASCADE
);

CREATE TABLE payments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    booking_id INT UNIQUE,
    payment_method VARCHAR(50) NOT NULL,
    amount DECIMAL(10,2) NOT NULL,
    status ENUM('pending', 'success', 'failed') DEFAULT 'pending',
    paid_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (booking_id) REFERENCES bookings(id) ON DELETE CASCADE
);

CREATE TABLE reviews (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    destination_id INT,
    rating INT CHECK (rating BETWEEN 1 AND 5),
    comment TEXT,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (destination_id) REFERENCES destinations(id) ON DELETE CASCADE
);

-- OPERASI CRUD (DML)
-- 1. Create (Insert)
INSERT INTO categories (name, description) VALUES ('Wisata Alam & Bahari', 'Destinasi keindahan alam pantai dan laut');
INSERT INTO destinations (category_id, name, location, price_ticket, description) VALUES (1, 'Pantai Paal', 'Minahasa Utara, Sulawesi Utara', 20000.00, 'Pantai pasir putih eksotis');

-- 2. Read (Select)
SELECT d.name, d.location, d.price_ticket, c.name AS category_name 
FROM destinations d
LEFT JOIN categories c ON d.category_id = c.id;

-- 3. Update
UPDATE destinations SET price_ticket = 25000.00 WHERE name = 'Pantai Paal';

-- 4. Delete
DELETE FROM destinations WHERE name = 'Pantai Paal';