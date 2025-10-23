def fibonacci(n):
    if n == 0:        # base case 1
        return 0
    elif n == 1:      # base case 2
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-1)

print(fibonacci(3))