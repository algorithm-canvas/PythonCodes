def area(length, width, unit="cm"):
    a = length*width
    print(f"The area is {area} {unit}^2")
    return area

area(5.0,3.0)

# lambda function => one line anonymous function
# recursive functions => they called by themself to solve a problem
# Generator function => returns an iterator, useeful for large sequence of Data