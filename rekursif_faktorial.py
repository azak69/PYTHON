def faktorial(n):
    if n == 1:        # base case
        return 1
    else:
        return n * faktorial(n-1)

print(faktorial(5))   # output: 120