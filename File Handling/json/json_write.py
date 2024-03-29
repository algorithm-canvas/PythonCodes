import json

data = {"name": "jhon", "age": 30, "city": "New York"}
with open("output.json","w") as json_file:
    json.dump(data, json_file, indent=4)