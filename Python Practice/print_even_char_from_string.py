userInput = input("")
str1 = str(userInput)
size = (len(str1))

for i in range(0, size-1, 2):
    print(i, userInput[i])