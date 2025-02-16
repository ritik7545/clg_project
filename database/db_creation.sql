-- Drop the existing database if it exists
DROP DATABASE IF EXISTS retail_sales_db;

-- Create the new database
CREATE DATABASE IF NOT EXISTS retail_sales_db;

-- Switch to the new database
USE retail_sales_db;

-- Create the t_shirts table
CREATE TABLE t_shirts (
    t_shirt_id INT AUTO_INCREMENT PRIMARY KEY,
    brand VARCHAR(50) NOT NULL,
    color VARCHAR(50) NOT NULL,
    size VARCHAR(10) NOT NULL,
    price DECIMAL(10,2) NOT NULL CHECK (price >= 0),
    stock_quantity INT NOT NULL CHECK (stock_quantity >= 0),
    UNIQUE KEY brand_color_size (brand, color, size)
);   

-- Insert data into the t_shirts table
INSERT INTO t_shirts (brand, color, size, price, stock_quantity) VALUES 
('Beauty', 'Red', 'M', 50.00, 3),
('Clothing', 'Blue', 'L', 500.00, 2),
('Electronics', 'Black', 'S', 30.00, 1),
('Clothing', 'White', 'M', 500.00, 1),
('Beauty', 'Red', 'XS', 50.00, 2),
('Beauty', 'Blue', 'S', 30.00, 1),
('Clothing', 'Black', 'M', 25.00, 2),
('Electronics', 'White', 'L', 25.00, 4),
('Electronics', 'Red', 'XS', 300.00, 2),
('Clothing', 'Blue', 'XL', 50.00, 4),
('Clothing', 'Black', 'S', 50.00, 2),
('Beauty', 'White', 'M', 25.00, 3),
('Electronics', 'Red', 'L', 500.00, 3),
('Clothing', 'Blue', 'XS', 30.00, 4),
('Electronics', 'Black', 'M', 500.00, 4),
('Clothing', 'White', 'L', 500.00, 3),
('Clothing', 'Red', 'XL', 25.00, 4),
('Electronics', 'Blue', 'S', 25.00, 2),
('Clothing', 'White', 'XS', 300.00, 3),
('Beauty', 'Red', 'L', 500.00, 1),
('Clothing', 'Blue', 'M', 50.00, 2),
('Clothing', 'White', 'XL', 300.00, 1),
('Beauty', 'Black', 'S', 25.00, 2),
('Electronics', 'Blue', 'L', 500.00, 2);

-- Create the discounts table
CREATE TABLE discounts (
    discount_id INT AUTO_INCREMENT PRIMARY KEY,
    t_shirt_id INT NOT NULL,
    pct_discount DECIMAL(5,2) NOT NULL CHECK (pct_discount BETWEEN 0 AND 100),
    FOREIGN KEY (t_shirt_id) REFERENCES t_shirts(t_shirt_id) ON DELETE CASCADE
);

-- Insert discount data
INSERT INTO discounts (t_shirt_id, pct_discount) VALUES 
(1, 10.00),
(2, 15.00),
(3, 20.00),
(4, 5.00),
(5, 25.00),
(6, 10.00),
(7, 30.00),
(8, 35.00),
(9, 40.00),
(10, 45.00);