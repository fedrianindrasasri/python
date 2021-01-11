print("Selamat datang di Program Biodata")
print("="*50)

# r, w, or r+, a
file_bio = open("biodata.txt", "r+")
teks = file_bio.read()

print(teks)

# ambil inputan dari user
nama = input("Masukkan Nama Anda: ")
umur = input("Masukkan Umur Anda: ")
alamat = input("Masukkan Alamat Anda: ")

# format teks
teks = "\nNama: {}\nUmur: {}\nAlamat: {}\n---".format(nama, umur, alamat)

# buka file untuk ditulis


#tulis teks ke file'
file_bio.write(teks)

file_bio.close()
