# mode file
# r = Baca
# w = Tulis
# a = Tambah
# x = Buat baru

# print("== Simpan Data Nilai ==")
# file = open("contoh.txt", "w")

# while True:
#     nama = input("Masukkan Nama Siswa : ")
#     if nama == "":
#         break
    
#     nilai = input("Masukkan Nilai Siswa : ")
    
#     file.write(f"Nama : {nama}, Nilai : {nilai} \n")
#     print(f"Data {nama} berhasil ditambahkan!")
#     print("Tekan Enter tanpa input untuk selesai!")

# file.close()
# print("== Program Selesai ==")  # Membuka file untuk 

print("== Menampilkan Data Nilai ==")
try:
    with open("contoh.txt", "r") as file:

        for line in file:
            data = line.strip().split(",")
            print(f"{data[0]} : {data[1]}")
except FileNotFoundError:
    print("File tidak ditemukan.")

print("== Program Selesai ==")