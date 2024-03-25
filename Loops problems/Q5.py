# Find the first non repeated character in a string

input_str = "teeteracdacd"

for char in input_str:
    print(char)
    if input_str.count(char) == 1:
        print("Result is: ", char)
        break