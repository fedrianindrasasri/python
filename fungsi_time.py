import time

print("Peluncuran roket")
raw_input("Tekan [Enter] untuk memulai")

for i in range(10, 0, -1):
    time.sleep(1)
    print(str(i))

print("Roket Meluncur")
