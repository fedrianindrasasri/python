total_belanja = input("Total belanja : Rp ")

bayar = total_belanja

if  total_belanja > 100000 :
    print("Kamu mendapatkan bonus minuman dingin")
    print("dan diskon 5 %")
    
    diskon = total_belanja * 5/100
    bayar = total_belanja - diskon
    

print("Total yang harus dibayar: Rp %s" %bayar)
print("Terima Kasih sudah berbelanja")
print("datang lagi ya.....");