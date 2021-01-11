import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="toko_mainan"
)

cursor = db.cursor()
sql = "INSERT INTO customer (name, address) VALUES (%s, %s)"
values = [
    ("Fedrian", "Pekanbaru"),
    ("Indra", "Bangkinang"),
    ("Sasri", "Siak"),
    ("Faiz", "Bengkalis"),
]

for val in values:
    cursor.execute(sql, val)
    db.commit()

print("{} data ditambahkan".format(len(values)))
