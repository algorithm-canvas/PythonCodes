new_lines = ["additional line 1\n", "additional line 2\n"]
with open("output.txt", "a") as file:
    file.writelines(new_lines)