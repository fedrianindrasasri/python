import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="toko_mainan"
)

cursor = db.cursor()
sql = "UPDATE customer SET name=%s, address=%s WHERE customer_id=%s"
val = ("Fedrian Indra", "Balam Km.3", 1)

cursor.execute(sql, val)
db.commit()

print("{} data diupdate".format(cursor.rowcount))
