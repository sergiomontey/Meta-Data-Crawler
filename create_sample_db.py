#!/usr/bin/env python3
"""
Create sample test database for the Metadata Crawler
This creates a realistic sample database with multiple tables and relationships
"""

import sqlite3
import os

def create_sample_database():
    """Create a sample database with realistic schema"""
    
    db_path = "sample_data.db"
    
    # Remove existing database
    if os.path.exists(db_path):
        os.remove(db_path)
    
    # Create connection
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Create Customers table
    cursor.execute('''
        CREATE TABLE customers (
            customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            phone TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Create Products table
    cursor.execute('''
        CREATE TABLE products (
            product_id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_name TEXT NOT NULL,
            description TEXT,
            category TEXT,
            price REAL NOT NULL,
            stock_quantity INTEGER DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Create Orders table
    cursor.execute('''
        CREATE TABLE orders (
            order_id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER NOT NULL,
            order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            total_amount REAL NOT NULL,
            status TEXT CHECK(status IN ('pending', 'processing', 'shipped', 'delivered', 'cancelled')),
            shipping_address TEXT,
            FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
        )
    ''')
    
    # Create Order Items table
    cursor.execute('''
        CREATE TABLE order_items (
            order_item_id INTEGER PRIMARY KEY AUTOINCREMENT,
            order_id INTEGER NOT NULL,
            product_id INTEGER NOT NULL,
            quantity INTEGER NOT NULL,
            unit_price REAL NOT NULL,
            subtotal REAL NOT NULL,
            FOREIGN KEY (order_id) REFERENCES orders(order_id),
            FOREIGN KEY (product_id) REFERENCES products(product_id)
        )
    ''')
    
    # Create Reviews table
    cursor.execute('''
        CREATE TABLE reviews (
            review_id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_id INTEGER NOT NULL,
            customer_id INTEGER NOT NULL,
            rating INTEGER CHECK(rating BETWEEN 1 AND 5),
            review_text TEXT,
            review_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (product_id) REFERENCES products(product_id),
            FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
        )
    ''')
    
    # Insert sample data
    cursor.executemany('''
        INSERT INTO customers (first_name, last_name, email, phone)
        VALUES (?, ?, ?, ?)
    ''', [
        ('John', 'Doe', 'john.doe@email.com', '555-0101'),
        ('Jane', 'Smith', 'jane.smith@email.com', '555-0102'),
        ('Bob', 'Johnson', 'bob.johnson@email.com', '555-0103'),
        ('Alice', 'Williams', 'alice.williams@email.com', '555-0104'),
        ('Charlie', 'Brown', 'charlie.brown@email.com', '555-0105')
    ])
    
    cursor.executemany('''
        INSERT INTO products (product_name, description, category, price, stock_quantity)
        VALUES (?, ?, ?, ?, ?)
    ''', [
        ('Laptop Pro 15', 'High-performance laptop', 'Electronics', 1299.99, 50),
        ('Wireless Mouse', 'Ergonomic wireless mouse', 'Electronics', 29.99, 200),
        ('USB-C Cable', 'Fast charging cable', 'Accessories', 19.99, 500),
        ('Laptop Bag', 'Durable laptop carrying bag', 'Accessories', 49.99, 100),
        ('External SSD 1TB', 'Portable storage device', 'Electronics', 149.99, 75)
    ])
    
    cursor.executemany('''
        INSERT INTO orders (customer_id, total_amount, status, shipping_address)
        VALUES (?, ?, ?, ?)
    ''', [
        (1, 1329.98, 'delivered', '123 Main St, City, State 12345'),
        (2, 199.98, 'shipped', '456 Oak Ave, Town, State 67890'),
        (3, 49.99, 'processing', '789 Pine Rd, Village, State 11111'),
        (1, 29.99, 'delivered', '123 Main St, City, State 12345'),
        (4, 1499.97, 'pending', '321 Elm St, Borough, State 22222')
    ])
    
    cursor.executemany('''
        INSERT INTO order_items (order_id, product_id, quantity, unit_price, subtotal)
        VALUES (?, ?, ?, ?, ?)
    ''', [
        (1, 1, 1, 1299.99, 1299.99),
        (1, 3, 1, 19.99, 19.99),
        (2, 5, 1, 149.99, 149.99),
        (2, 4, 1, 49.99, 49.99),
        (3, 4, 1, 49.99, 49.99),
        (4, 2, 1, 29.99, 29.99),
        (5, 1, 1, 1299.99, 1299.99),
        (5, 2, 2, 29.99, 59.98),
        (5, 5, 1, 149.99, 149.99)
    ])
    
    cursor.executemany('''
        INSERT INTO reviews (product_id, customer_id, rating, review_text)
        VALUES (?, ?, ?, ?)
    ''', [
        (1, 1, 5, 'Excellent laptop, very fast!'),
        (1, 3, 4, 'Great performance, slightly heavy'),
        (2, 1, 5, 'Perfect mouse, very comfortable'),
        (5, 2, 5, 'Super fast storage device'),
        (4, 3, 4, 'Good quality bag, fits my laptop perfectly')
    ])
    
    # Create indexes for performance
    cursor.execute('CREATE INDEX idx_customer_email ON customers(email)')
    cursor.execute('CREATE INDEX idx_order_customer ON orders(customer_id)')
    cursor.execute('CREATE INDEX idx_order_items_order ON order_items(order_id)')
    cursor.execute('CREATE INDEX idx_reviews_product ON reviews(product_id)')
    
    conn.commit()
    conn.close()
    
    print(f"✓ Sample database created: {db_path}")
    print("  Tables: customers, products, orders, order_items, reviews")
    print("  Relationships: Foreign keys established")
    print("  Sample data: Populated with test records")

if __name__ == "__main__":
    create_sample_database()
