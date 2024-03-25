age = input("What is your age: ")
age_int = int(age)

day = "Wednesday"

price = 12 if age_int >= 18 else 8

if day == "Wednesday":
    price = price - 2

    print(price)



