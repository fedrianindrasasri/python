# Global Variabel menyimpan data buku
buku = []


# FUngsi untuk menampilkan semua data
def show():
    if len(buku) <= 0:
        print("Belum Ada Data Buku")
    else:
        for indeks in range(len(buku)):
            print("[%d] %s " % (indeks, buku[indeks]))

# Fungsi untuk insert data


def insert_data():
    buku_baru = raw_input("Judul Buku Baru : ")
    buku.append(buku_baru)

# Fungsi untuk edit data


def edit_data():
    show()
    indeks = input("Inputkan ID Buku : ")
    if (indeks > len(buku)):
        print("ID Salah")
    else:
        judul_baru = raw_input("Judul Buku Baru : ")
        buku[indeks] = judul_baru

# Fungsi Untuk Menghapus Data


def delete_data():
    show()
    indeks = input("Inputkan ID Buku : ")
    if (indeks > len(buku)):
        print("ID Salah")
    else:
        buku.remove(buku[indeks])


def show_menu():
    print("\n")
    print(" ------------- Menu --------------")
    print("[1] Show Data")
    print("[2] Insert Data")
    print("[3] Edit Data")
    print("[4] Delete Data")
    print("[5] Exit")

    menu = input("PILIH MENU : ")
    print("\n")

    if (menu == 1):
        show()
    elif (menu == 2):
        insert_data()
    elif (menu == 3):
        edit_data()
    elif (menu == 4):
        delete_data()
    elif (menu == 5):
        exit()
    else:
        print("Salah Pilih")


if __name__ == "__main__":
    while(True):
        show_menu()
