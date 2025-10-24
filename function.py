def cetak_list(*data):
    for item in data:
        print(item)

cetak_list(1,2,3,4,5)
cetak_list("Saya", "Aku", "Gue", "Nyong")

def cetak_dict(**isi):
    for key, value in isi.items():
        print(f"{key} : {value}")

cetak_dict(nama="Saya", nama2="Aku", nama3="Gue")
cetak_dict(umur=20, umur2=22, umur3=25)

# Program Fungsi dengan Argumen Tak Terbatas
