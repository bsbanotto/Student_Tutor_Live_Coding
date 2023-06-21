#!/usr/bin/env python3
import warnings
warnings.filterwarnings('ignore')
import MySQLdb
import pandas as pd

# To run this, you'll have to create a user/password pair and grant them the
# appropriate permissions

user = 'bsbanotto'
password = 'MySQLpwd'

conn = MySQLdb.connect(host='localhost', port=3306, user=user, password=password)

# Create database to use
cursor = conn.cursor()
cursor.execute("CREATE DATABASE if NOT EXISTS LiveCoding;")
cursor.execute("USE LiveCoding;")
cursor.close()

# Add tables to the database
cursor = conn.cursor()
cursor.execute("\
CREATE TABLE IF NOT EXISTS Authors (\
    author_id INTEGER PRIMARY KEY,\
    author_name TEXT,\
    birth_date DATE,\
    country TEXT\
);\
CREATE TABLE IF NOT EXISTS Books (\
    book_id INTEGER PRIMARY KEY,\
    title TEXT,\
    publication_year INTEGER,\
    price REAL,\
    author_id INTEGER,\
    FOREIGN KEY (author_id) REFERENCES Authors (author_id)\
);\
CREATE TABLE IF NOT EXISTS Customers (\
    customer_id INTEGER PRIMARY KEY,\
    first_name TEXT,\
    last_name TEXT,\
    email TEXT,\
    address TEXT\
);\
CREATE TABLE IF NOT EXISTS Orders (\
    order_id INTEGER PRIMARY KEY,\
    customer_id INTEGER,\
    order_date DATE,\
    total_amount REAL,\
    FOREIGN KEY (customer_id) REFERENCES Customers (customer_id)\
);\
CREATE TABLE IF NOT EXISTS Order_Items (\
    order_item_id INTEGER PRIMARY KEY,\
    order_id INTEGER,\
    book_id INTEGER,\
    quantity INTEGER,\
    unit_price REAL,\
    FOREIGN KEY (order_id) REFERENCES Orders (order_id),\
    FOREIGN KEY (book_id) REFERENCES Books (book_id)\
);\
")
cursor.close()

# Fill the tables with information
cursor = conn.cursor()
cursor.execute("\
-- Inserting data into Authors table\
INSERT INTO Authors (author_id, author_name, birth_date, country)\
VALUES\
    (1, 'J.K. Rowling', '1965-07-31', 'United Kingdom'),\
    (2, 'George Orwell', '1903-06-25', 'United Kingdom'),\
    (3, 'Jane Austen', '1775-12-16', 'United Kingdom'),\
    (4, 'Ernest Hemingway', '1899-07-21', 'United States'),\
    (5, 'Fyodor Dostoevsky', '1821-11-11', 'Russia');\
-- Inserting data into Books table\
INSERT INTO Books (book_id, title, publication_year, price, author_id)\
VALUES\
    (1, 'Harry Potter and the...', 1997, 20.99, 1),\
    (2, '1984', 1949, 15.99, 2),\
    (3, 'Pride and Prejudice', 1813, 12.50, 3),\
    (4, 'The Old Man and the Sea', 1952, 10.99, 4),\
    (5, 'Crime and Punishment', 1866, 18.75, 5);\
-- Inserting data into Customers table\
INSERT INTO Customers (customer_id, first_name, last_name, email, address)\
VALUES\
    (1, 'John', 'Smith', 'john.smith@example.com', '123 Main St, Anytown, USA'),\
    (2, 'Jane', 'Doe', 'jane.doe@example.com', '456 Elm St, Otherville, USA'),\
    (3, 'David', 'Johnson', 'david.johnson@example.com', '789 Oak St, Somewhere, USA');\
-- Inserting data into Orders table\
INSERT INTO Orders (order_id, customer_id, order_date, total_amount)\
VALUES\
    (1, 1, '2023-04-15', 41.98),\
    (2, 2, '2023-04-16', 28.99),\
    (3, 3, '2023-04-18', 12.50);\
-- Inserting data into Order_Items table\
INSERT INTO Order_Items (order_item_id, order_id, book_id, quantity, unit_price)\
VALUES\
    (1, 1, 1, 2, 20.99),\
    (2, 1, 4, 1, 10.99),\
    (3, 2, 3, 1, 12.50),\
    (4, 3, 5, 1, 18.75);\
")

# View all of the tables in the database
tables = pd.read_sql('SHOW TABLES;', conn)
tables

# View the Authors Table
Authors = pd.read_sql('SELECT * FROM Authors;', conn)
Authors

# Add an author to the Authors table (Ray Bradbury, born 1920-08-22, in the United States)
# cursor = conn.cursor()
# cursor.execute("INSERT INTO Authors (author_id, author_name, birth_date, country) VALUES (6, 'Ray Bradbury', '1920-08-22', 'United States');")
# cursor.close()

# Add a book to the Books table (6, Animal Farm, 1945, 15.50, 2)
cursor = conn.cursor()
cursor.execute("INSERT INTO Books (book_id, title, publication_year, price, author_id) VALUES (6, 'Animal Farm', 1945, 15.50, 2);")
cursor.close()

# View the Authors Table
Authors = pd.read_sql('SELECT * FROM Authors;', conn)
Authors

# Remove an author from the Authors table
cursor = conn.cursor()
cursor.execute("DELETE FROM Authors WHERE author_id = 6;")
cursor.close()

# View the Authors Table
Authors = pd.read_sql('SELECT * FROM Authors;', conn)
Authors

# Describe the Authors Table
Authors_desc = pd.read_sql('DESCRIBE Authors', conn)
Authors_desc

# View the Books table
Books = pd.read_sql('SELECT * FROM Books ORDER BY author_id;', conn)
Books

# Describe the Books table
Books_desc = pd.read_sql('DESCRIBE Books', conn)
Books_desc

# Join the Authors and Books table
All = pd.read_sql('SELECT *\
                  FROM Authors\
                  JOIN Books ON Books.author_id = Authors.author_id;', conn)
All

# Join the Authors and Books table where price > $12.00
All = pd.read_sql('SELECT *\
                  FROM Authors\
                  JOIN Books ON Books.author_id = Authors.author_id\
                  WHERE Books.price > 12.00;', conn)
All

conn.close()