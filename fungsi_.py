# membuat fungsi luas segitiga

def luas_segitiga(alas, tinggi):
    luas = (alas * tinggi) / 2
    print("Luas Segitiga = %f" % luas)


# memanggi fungsi diatas
luas_segitiga(5, 6)


def luas_persegi_panjang(panjang, lebar):
    luas_per = panjang * lebar
    return luas_per


print("Luas Persegi = %f" % luas_persegi_panjang(5, 4))
