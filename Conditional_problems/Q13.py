try:
    x = int(input("num: "))
    y = 10/x
    print(f"Res: {y}")
except ValueError:
    print("II")
except ZeroDivisionError:
    print("zeo")