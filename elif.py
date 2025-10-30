nilai = int(input("Masukkan nilai: "))

if nilai >= 90:
    print("A")

elif nilai >= 80:
    print("B")

elif nilai >= 70:
    print("C")

elif nilai >= 60:
    print("D")

else:
    print("E")

# Program Penilaian Sederhana

umur = int(input("Masukkan umur Anda: "))
punya_ktp = input("Apakah Anda memiliki KTP? (ya/tidak): ").lower()
if umur >= 17 and punya_ktp == "ya":
    print("Anda boleh memilih dalam pemilu.")
else:
    print("Anda tidak boleh memilih dalam pemilu.")

# Program Penentuan Nilai Sederhana