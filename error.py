# SyntaxError
# NameError
# ValueError
# TypeError
# IndexError
# KeyError
# ZeroDivisionError
print("=== KALKULATOR SEDERHANA ===")

try:
    a = int(input("Angka Pertama : "))
    b = int(input("Angka Kedua : "))
    hasil = a / b
    print(f"Hasil : {hasil}")
except ValueError:
    print("Tolong masukkan angka!")
except TypeError:
    print("Tolong masukkan angka!")
except ZeroDivisionError:
    print("Tidak bisa dibagi nol!")
except:
    print("Terjadi Kesalahan!")

print("=== PROGRAM SELESAI! ===")

try:
    a = int(input("Masukkan angka : "))
except ValueError:
    print("Tolong masukkan angka!")
else:
    print(f"Angka yang Anda masukkan : {a}")
    if a > 0:
        print("Angka positif")
    elif a < 0:
        print("Angka negatif")
    else:
        print("Angka nol")
finally:
    print("Program Selesai!")

# Program Penanganan Error Sederhana