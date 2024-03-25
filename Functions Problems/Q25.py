def fun1(a,b):
    return(a*a) + (b*b)
def fun2(a,b):
    return a*b

res = fun1(fun2(2,3),3)
print(res)