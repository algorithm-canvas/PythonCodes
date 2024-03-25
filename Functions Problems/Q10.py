# Create a recursive function to calculate the factorial of a number

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * (n - 1)

print(factorial(5))