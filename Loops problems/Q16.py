list1 = [[1,2], [3,4], [5,6]]
list2 = [item for sublist in list1 for item in sublist]
print(list2)