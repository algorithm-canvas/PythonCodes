def givenn(numberList):
    print("Given list:",numberList)
    first_num = numberList[0]
    last_num = numberList[-1]

    if first_num == last_num:
        return True
    else:
        return False

num_x = [10, 20, 30, 40, 10]
print("result is: ",(givenn, num_x))
num_y = [47,65,35,90]
print("result is: ",(givenn, num_y))