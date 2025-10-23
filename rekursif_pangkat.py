def pangkat(a, n):
    if n == 0:        # base case
        return 1
    else:
        return a * pangkat(a, n-1)

print(pangkat(2, 4))  # output: 16