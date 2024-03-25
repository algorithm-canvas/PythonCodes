m = 10
n = 20
def check():
    global n
    m = 45
    n = 56

check()
print(m)
print(n)    