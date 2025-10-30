hobi = {"membaca", "menulis", "berkebun"}
print(hobi)

hobi.add("bersepeda") # menambahkan elemen baru
print(hobi)

hobi.remove("menulis") # menghapus elemen
print(hobi)

for e in hobi:
    print(f"Saya suka {e}") # mengiterasi elemen set