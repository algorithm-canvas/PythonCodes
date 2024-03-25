def transform_array(array):
    array.sort()
    sum_of_array = sum(array)
    array.append(sum_of_array)
    return array

transform_array([0,1.2,-2.4,3,4.2,1])
print(transform_array)