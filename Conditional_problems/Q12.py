try:
    x = int(input("num: "))
    if x > 0:
        if x % 2 == 0:
            print("A")
        else:
            print("B")
    elif x < 0:
        print("C")
    else:
        print("D")
except ValueError:
    print("E") 