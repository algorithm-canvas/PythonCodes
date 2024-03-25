age = input("What is your age: ")
age_int = int(age)

if age_int < 13:
    print("Child")
elif age_int < 19:
    print("Teenager")
elif age_int < 59:
    print("Adult")
else:
    print("Senior")
