# counting positive numbers

number = [1, 2, -3, 4, -5, 6, -7, 8, 9, 10]
positive_num_cnt = 0
for num in number:
    if num > 0:
        positive_num_cnt += 1

        print("Positive Numbers are: ",positive_num_cnt)
