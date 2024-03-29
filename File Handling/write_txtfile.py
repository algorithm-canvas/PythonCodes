with open("output.txt", "w") as file:
    file.write("This line is 1st line\n")
    file.write("This line is 2nd line\n")


# writeline method

lines = ["Line1\n", "Line2\n", "Line3\n"]
with open("output.txt", "w") as file:
    file.writelines(lines) 