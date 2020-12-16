# Membuat Dictionary

data_diri = {
    "nama": "Fedrian Indra Sasri",
    "Umur": 22,
    "hobi": ["coding", "membaca", "nonton", "rebahan"],
    "menikah": False,
    "sosmed": {
        "facebook": "fedrian.indra",
        "instagram": "fedrian.indra.sasri",
        "twitter": "fedrianindrassr"
    }

}

# akses dictionary data_diri
print("Nama saya adalah %s" % data_diri["nama"])
print("Instagram : %s" % data_diri["sosmed"]["instagram"])

# dengan Perulangan
print("\n")
for key, val in data_diri.items():
    # print(data_diri[key])
    print("%s : %s" % (key, val))
