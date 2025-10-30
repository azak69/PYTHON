nama = ["Jokowi", "Prabowo", "Ganjar", "Anies", "Sandiaga"]
print(nama[2])  # Output: Ganjar
print(nama[1])  # Output: Prabowo
print(nama[0])  # Output: Jokowi

# Program Akses Elemen List Sederhana

nama = ["Jokowi", "Prabowo", "Ganjar", "Anies", "Sandiaga"]
print(nama)
nama[3] = "Ridwan Kamil"
print(nama)

# Program Mengubah Elemen List Sederhana

nama = ["Jokowi", "Prabowo", "Ganjar", "Anies", "Sandiaga"]
print(nama)
nama.append("Ahmad Dhani") # Menambahkan elemen di akhir list
print(nama)
nama.insert(2, "Sri Mulyani") # Menambahkan elemen di indeks tertentu
print(nama)

# Program Menambahkan Elemen List Sederhana

nama.remove("Sandiaga") # Menghapus berdasarkan nilai
print(nama)
nama.pop() # Menghapus elemen terakhir
print(nama)
del nama[1] # Menghapus berdasarkan indeks dengan del
print(nama)

# Program Menghapus Elemen List Sederhana

nama = ["Jokowi", "Prabowo", "Ganjar", "Anies", "Sandiaga"]
umur = [61, 60, 54, 50, 49]
data_gabungan = nama + umur
print(data_gabungan)

# Program Menggabungkan Dua List Sederhana

nama = ["Jokowi", "Prabowo", "Ganjar", "Anies", "Sandiaga"]
for n in nama:
    print(f"Nama calon presiden: {n}")
for i in range(0, len(nama)):
    print(f"Calon presiden ke-{i} adalah {nama[i]}")

# Program Iterasi Elemen List Sederhana

if "Jokowi" in nama:
    print("Jokowi ada dalam daftar calon presiden.")
else:
    print("Jokowi tidak ada dalam daftar calon presiden.")

# Program Pengecekan Keberadaan Elemen List Sederhana


