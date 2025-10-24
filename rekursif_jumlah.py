def jumlah(n):
    if n == 1:        # base case
        return 1
    else:
        return n + jumlah(n-1)

print(jumlah(5))      # output: 15

# Program Rekursif Jumlah Sederhana