import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="toko_mainan"
)

cursor = db.cursor()
sql = """CREATE TABLE customer(
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    address VARCHAR(255)
)
"""
cursor.execute(sql)

print("Table berhasil dibuat")
