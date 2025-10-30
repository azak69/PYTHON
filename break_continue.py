secret = 8

while True
    tebak = int(input("Tebak angka antara 1 sampai 10: "))

    if tebak == secret:
        print("Selamat! Tebakan Anda benar.")
        break
    else:
        print("Tebakan Anda salah. Coba lagi.")
        continue

# Program Tebak Angka Sederhana

for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(f"Angka ganjil : {i}")

# Program Menampilkan Angka Ganjil