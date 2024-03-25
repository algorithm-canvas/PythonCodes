# Check if all elements in a list are unique, if duplicate is found exit the loop and print duplicate

items = ["apple", "banana", "apple", "mango"]

uni_item = set()

for item in items:
    if item in uni_item:
        print("Duplicate: ", item)
        break
    uni_item.add(item) 
