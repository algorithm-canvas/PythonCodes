def calculation(num1, num2):
    #Find product
    product = num1*num2

    #now check if product is > 1000
    if(product > 1000):
        return product
    else:
        sum = num1 + num2
        return sum

result = calculation(20, 3000)
print(result)        