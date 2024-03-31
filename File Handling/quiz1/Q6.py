with open("example.txt", "r") as file1, open("output.txt", "r") as file2:
    content1 = file1.read()
    print("File 1 content:",content1)

    content2 = file2.read()
    print("File 2 content:",content2)
