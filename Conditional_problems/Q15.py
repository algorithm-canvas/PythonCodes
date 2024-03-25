m = True
n = False
o = True

if not m or n:
    print("m")
elif not m or not n and o:
    print("n")
elif not m or n or not n and m:
    print("o")
else:
    print("p")