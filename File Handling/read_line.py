with open("example.txt", "r") as file:
    line = file.readline()
    while line:
        print(line, end="")
        line = file.readline()

# for loop
with open("example.txt", "r") as file:
    lines = file.readline()
for line in lines:    
        print(line, end="")
        line = file.readline()