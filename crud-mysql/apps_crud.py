import mysql.connector
import os

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="toko_mainan"
)

def insertData(db):
    name = raw_input("Masukkan Nama: ")
    address = raw_input("Masukkan Alamat: ")
    val = (name, address)
    cursor = db.cursor()
    sql = ("INSERT INTO customer (name, address) VALUES(%s, %s)")
    cursor.execute(sql, val)
    db.commit()
    print("{} data ditambahkan".format(cursor.rowcount))

def showData(db):
    cursor = db.cursor()
    sql = "SELECT * FROM customer"
    cursor.execute(sql)
    result = cursor.fetchall()

    if(cursor.rowcount < 0):
        print("Data tidak ada")
    else:
        for data in result:
            print(data)

def updateData(db):
    cursor = db.cursor()
    showData(db)
    customer_id = input("pilih id customer > ")
    name = raw_input("Nama Baru: ")
    address = raw_input("Alamat Baru: ")

    sql = "UPDATE customer SET name=%s, address=%s WHERE customer_id=%s"
    val = (name, address, customer_id)
    cursor.execute(sql, val)
    db.commit()

    print("{} data diupdate".format(cursor.rowcount))

def deleteData(db):
    cursor = db.cursor()
    showData(db)
    customer_id = input("pilih id customer > ")

    sql = "DELETE FROM customer WHERE customer_id=%s"
    val = (customer_id,)
    cursor.execute(sql, val)
    db.commit()

    print("{} data dihapus".format(cursor.rowcount))

def searchData(db):
    cursor = db.cursor()
    keyword = raw_input("Kata Kunci >: ")
    sql = "SELECT * FROM customer WHERE name LIKE %s OR address LIKE %s"
    val = ("%{}%".format(keyword), "%{}%".format(keyword))
    cursor.execute(sql, val)
    result = cursor.fetchall()

    if(cursor.rowcount <= 0):
        print("Tidak ada data")
    else:
        for data in result:
            print(data)

def showMenu(db):
    print("=== APLIKASI DATABASE PYTHON ===")
    print("1. Insert Data")
    print("2. Tampilkan Data")
    print("3. Update Data")
    print("4. Hapus Data")
    print("5. Cari Data")
    print("0. Keluar")
    print("------------------")
    menu = input("Pilih menu> ")

    # os.system("clear")

    if(menu == 1):
        insertData(db)
    elif(menu == 2):
        showData(db)
    elif(menu == 3):
        updateData(db)
    elif(menu == 4):
        deleteData(db)
    elif(menu == 5):
        searchData(db)
    elif(menu == 0):
        exit()
    else:
        print("Menu Salah")

if __name__ == "__main__":
    while(True):
        showMenu(db)
