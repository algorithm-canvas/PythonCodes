# Keep asking the user for input until they inter a num b/w 1 to 10

while True:
    num = int(input("Enter a value b/w 1 to 10: "))
    if 1<= num <=10:
        print("Thanks")
        break
    else:
        print("Invalid Value")


