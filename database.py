import sqlite3

# connect database
conn = sqlite3.connect("sample.db")
cur = conn.cursor()

# fresh start
cur.execute("DROP TABLE IF EXISTS sales")
cur.execute("DROP TABLE IF EXISTS customers")
cur.execute("DROP TABLE IF EXISTS products")

# customer table
cur.execute(
    """
    CREATE TABLE customers(
        customer_id INTEGER PRIMARY KEY,
        name TEXT,
        email TEXT,
        join_date DATE,
        country TEXT
    )
    """
)

# products table
cur.execute(
    """
    CREATE TABLE products(
        product_id INTEGER PRIMARY KEY,
        name TEXT,
        category TEXT,
        price REAL,
        cost REAL
    )
    """
)

# sales table
cur.execute(
    """
    CREATE TABLE sales(
        sale_id INTEGER PRIMARY KEY,
        customer_id INTEGER,
        product_id INTEGER,
        quantity INTEGER,
        discount REAL,
        original_price REAL,
        discount_price REAL,
        sale_date DATE,
        FOREIGN KEY(customer_id) REFERENCES customers(customer_id)
        FOREIGN KEY(product_id) REFERENCES products(product_id)
    )
    """
)

# sample customers
customers = [
    (1, "Alice", "alice@corp.com", "2025-01-10", "USA"),
    (2, "Akash", "akash@techx.com", "2025-02-20", "India"),
    (3, "Sunny", "isunny@innosoft.com", "2025-03-15", "Germany"),
    (4, "Luna", "beta@ltd.com", "2025-04-05", "France"),
    (5, "Derek", "derek@inc.com", "2025-05-12", "Thailand")
]
cur.executemany("INSERT INTO customers VALUES (?, ?, ?, ?, ?)", customers)

# sample products
products = [
    (1, "Laptop", "Electronics", 89000, 10000),
    (2, "Phone", "Electronics", 16000, 5000),
    (3, "Chair", "Furniture", 2200, 800),
    (4, "Desk", "Furniture", 2500, 1500),
    (5, "Headphones", "Electronics", 1500, 150)
]
cur.executemany("INSERT INTO products VALUES (?, ?, ?, ?, ?)", products)

# sample sales
sales = [
    (1, 1, 1, 5, 10, 89000, 80100, "2025-03-10"),
    (2, 2, 2, 10, 5, 16000, 15200, "2025-04-15"),
    (3, 3, 3, 20, 0, 2200, 2200, "2025-06-12"),
    (4, 4, 4, 7, 2, 2500, 2450, "2025-07-01"),
    (5, 5, 5, 15, 8, 1500, 1380, "2025-08-20"),
    (6, 1, 2, 3, 5, 16000, 15200, "2025-09-05"),
    (7, 2, 3, 4, 0, 2200, 2200, "2025-01-25"),
    (8, 3, 1, 2, 12, 89000, 78320, "2025-02-18"),
    (9, 4, 5, 6, 3, 1500, 1455, "2025-05-22"),
    (10, 5, 4, 1, 0, 2500, 2500, "2025-06-30")
]
cur.executemany("INSERT INTO sales VALUES (?, ?, ?, ?, ?, ?, ?, ?)", sales)

# close database
conn.commit()
conn.close()
print("Database created successfully !!!")