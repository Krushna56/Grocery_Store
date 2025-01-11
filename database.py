import sqlite3
from datetime import datetime

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('grocery_store.db')
        self.cursor = self.conn.cursor()
        self.create_tables()
    
    def create_tables(self):
        # Create products table
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                price REAL NOT NULL,
                quantity INTEGER NOT NULL,
                category TEXT NOT NULL
            )
        ''')
        
        # Create sales table
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS sales (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                product_id INTEGER,
                quantity INTEGER,
                total_price REAL,
                date TEXT,
                FOREIGN KEY (product_id) REFERENCES products (id)
            )
        ''')
        
        self.conn.commit()
    
    def add_product(self, name, price, quantity, category):
        self.cursor.execute('''
            INSERT INTO products (name, price, quantity, category)
            VALUES (?, ?, ?, ?)
        ''', (name, price, quantity, category))
        self.conn.commit()
    
    def update_product(self, id, name, price, quantity, category):
        self.cursor.execute('''
            UPDATE products
            SET name = ?, price = ?, quantity = ?, category = ?
            WHERE id = ?
        ''', (name, price, quantity, category, id))
        self.conn.commit()
    
    def delete_product(self, id):
        self.cursor.execute('DELETE FROM products WHERE id = ?', (id,))
        self.conn.commit()
    
    def get_all_products(self):
        self.cursor.execute('SELECT * FROM products')
        return self.cursor.fetchall()
    
    def get_product(self, id):
        self.cursor.execute('SELECT * FROM products WHERE id = ?', (id,))
        return self.cursor.fetchone()
    
    def record_sale(self, product_id, quantity):
        product = self.get_product(product_id)
        if product and product[3] >= quantity:
            total_price = product[2] * quantity
            date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            
            # Record the sale
            self.cursor.execute('''
                INSERT INTO sales (product_id, quantity, total_price, date)
                VALUES (?, ?, ?, ?)
            ''', (product_id, quantity, total_price, date))
            
            # Update product quantity
            new_quantity = product[3] - quantity
            self.cursor.execute('''
                UPDATE products
                SET quantity = ?
                WHERE id = ?
            ''', (new_quantity, product_id))
            
            self.conn.commit()
            return True
        return False
    
    def get_sales_report(self):
        self.cursor.execute('''
            SELECT 
                products.name,
                sales.quantity,
                sales.total_price,
                sales.date
            FROM sales
            JOIN products ON sales.product_id = products.id
        ''')
        return self.cursor.fetchall()
    
    def close(self):
        self.conn.close()