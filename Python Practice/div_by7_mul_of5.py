num = int(input())

if num < 2700 and num > 1500:
    print("Valid Range")
if num % 7 == 0 and num % 5 == 0:
    print("Number is valid")
else:
    print("Invalid Number")