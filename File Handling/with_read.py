file_path = "example.txt"

with open(file_path, "r") as file:

    file_contents = file.read()

    print("File Content: ")
    print(file_contents)