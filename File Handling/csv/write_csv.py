import csv

data = [["name","age"],["john",30],["alice",25],["bob",35]]
with open("output.csv", "w", newline="") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerows(data)