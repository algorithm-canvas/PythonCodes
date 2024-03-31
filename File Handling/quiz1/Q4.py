file_path = "example.txt"
try:
    with open(file_path,"r") as file:
        for line in file:
            print(line.rstrip("\n"))
except FileNotFoundError:
    print(f"File '{file_path}' not found.")