list = [[3,4,5,1], [12,6,1,2]]

value = list[0][0]
for row in range(0, len(list)):
    for column in range(0, len(list[row])):
        if value < list[row][column]:
            value = list[row][column]

print(value)            