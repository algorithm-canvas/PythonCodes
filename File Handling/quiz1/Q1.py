with open("data.txt","r") as file:
    data = [line.strip().split(",") for line in file]
print(data[1][2])     