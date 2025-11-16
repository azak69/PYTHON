a = 10
b = 3

print("Penjumlahan:", a + b)        # Menjumlahkan a dan b
print("Pengurangan:", a - b)        # Mengurangi b dari a
print("Perkalian:", a * b)          # Mengalikan a dengan b
print("Pembagian:", a / b)          # Membagi a dengan b (hasil float)
print("Pembagian bulat:", a // b)    # Membagi a dengan b (hasil bulat)
print("Modulus:", a % b)            # Sisa bagi a dengan b
print("Pangkat:", a ** b)            # a pangkat b

x = 5
print("Nilai awal x:", x)
x += 3  # x = x + 3
print("Setelah x += 3:", x)
x -= 2  # x = x - 2
print("Setelah x -= 2:", x)
x *= 4  # x = x * 4
print("Setelah x *= 4:", x)
x /= 2  # x = x / 2
print("Setelah x /= 2:", x)
x %= 3  # x = x % 3
print("Setelah x %= 3:", x)
x **= 2  # x = x ** 2
print("Setelah x **= 2:", x)

a = 7
b = 4

print("a > b:", a > b)    # True karena a lebih besar dari b
print("a < b:", a < b)    # False karena a tidak lebih kecil dari b
print("a >= b:", a >= b)  # True karena a lebih besar atau sama dengan b
print("a <= b:", a <= b)  # False karena a tidak lebih kecil atau sama dengan b
print("a == b:", a == b)  # False karena a tidak sama dengan b
print("a != b:", a != b)  # True karena a tidak sama dengan b

angka = 20
print(angka >10 and angka <30)  # True karena kedua kondisi benar
print(angka <10 or angka <30)   # True karena salah satu kondisi benar

positif = True
print(not positif)  # False karena negasi dari True adalah False

nama1 = "joko"
nama2 = "widodo"
data = nama1 + " " + nama2
print(data)  # Menggabungkan dua string dengan operator +
print(nama1 * 3)  # Mengulang string nama1 sebanyak 3 kali
print("jo" in nama1)  # True karena "jo" ada dalam nama1
print("do" not in nama1)  # True karena "do" tidak ada dalam nama1

# urutan prioritas operator: (), **, *, /, //, %, +, -, <, <=, >, >=, ==, !=, not, and, or