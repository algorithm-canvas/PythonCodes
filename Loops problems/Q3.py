# print the multiplication table of the given number till 10 but skip the 5th iteration

num = 2

for i in range(1, 11):
    if i == 5:
        continue

    print(num, 'x', i, '=', i*num)