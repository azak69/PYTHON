def fungsi_sapa(nama):
    print(f"Halo, {nama}!")

fungsi_sapa("Andi")
fungsi_sapa("Budi")

# Program Fungsi Sederhana

def luas_lingkaran(radius):
    phi = 3.14
    luas = phi * radius * radius
    return luas

hasil_luas = luas_lingkaran(7)
print(f"Luas lingkaran dengan radius 7 adalah {hasil_luas}")

# Program Fungsi dengan Return Value

def terimkasih(nama, makasih="terima kasih"):
    print(f"{makasih}, {nama}!")

terimkasih("Siti")
terimkasih("Ani", "Thanks a lot")

# Program Fungsi dengan Argumen Default

def profil(nama, umur, kota="Jogja", pekerjaan="Pelajar"):
    print(f"Nama: {nama.title()}, Umur: {umur}, Kota: {kota}, Pekerjaan: {pekerjaan}")

profil("budi", 21)
profil("susi", 25, kota="Jakarta", pekerjaan="Programmer")
profil("andi", 30, pekerjaan="Designer")

# Program Fungsi dengan Argumen Nama

nama = "Joko"
def nama():
    print("Nama saya : ", nama)

def ubah_nama():
    global nama
    nama = "Putra"
    print("Nama saya diubah menjadi : ", nama)

ubah_nama()
nama()

# Program Fungsi dan Variabel Global

def cetak_list(*data):
    for item in data:
        print(item)

cetak_list(1,2,3,4,5)
cetak_list("Saya", "Aku", "Gue", "Nyong")

# Program Fungsi list dengan Argumen Tak Terbatas

def cetak_dict(**isi):
    for key, value in isi.items():
        print(f"{key} : {value}")

cetak_dict(nama="Saya", nama2="Aku", nama3="Gue")
cetak_dict(umur=20, umur2=22, umur3=25)

# Program Fungsi dictionary dengan Argumen Tak Terbatas
