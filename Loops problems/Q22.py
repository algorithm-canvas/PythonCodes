length = 10
current_num = 0
next_num = 1
count = 0
if length <= 0:
    print("Please provide number greater than zero")
elif length == 1:
    print(current_num)
else:
    while count < length:
        print(current_num, end=' ')
        sum = current_num + next_num
        current_num = next_num
        next_num = sum
        count = count + 1