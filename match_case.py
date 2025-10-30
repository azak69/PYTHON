hari = int(input("Masukkan nama hari : ")).lower()

match hari:
    case "senin" | "selasa" | "rabu" | "kamis" | "jumat":
        print("KERJA KERJA KARJA")
    case "sabtu" | "minggu":
        print("LIBUR BRO")
    case _:
        print("Nama hari tidak valid!")

# Program Penentuan Hari Kerja atau Libur