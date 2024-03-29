import os

try:
    file = open("example.txt","r")
except FileNotFoundError:
    print("File not found: ")
except PermissionError:
    print("Permission denied")
finally:
    file.close()