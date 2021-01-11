import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="toko_mainan"
)

cursor = db.cursor()
sql = "SELECT * FROM customer"

cursor.execute(sql)

result = cursor.fetchall()
# jika ingin satu row pakai fetchone()

for data in result:
    print(data)
