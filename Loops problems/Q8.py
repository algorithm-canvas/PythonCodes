# Check if a num is a prime or not

num = 28

is_Prime = True

if num > 1:
    for i in range(2, num):
        if (num % i)  == 0:
            is_Prime = False
            break
print(is_Prime)