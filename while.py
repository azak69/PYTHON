password_true = "etcode99"
percobaan = 0
max_percobaan = 3

while percobaan < max_percobaan:
    password_input = input("Masukkan password: ")

    if password_input == password_true:
        print("Akses diterima.")
        break
    else:
        percobaan += 1
        print(f"Password salah. Percobaan ke-{percobaan} dari {max_percobaan}.")

else:
    print("Akses ditolak. Terlalu banyak percobaan gagal.")