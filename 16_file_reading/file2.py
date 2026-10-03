import json

json_file_path = "output.json"

try:
    with open(file=json_file_path, mode="r") as file:

        content = json.load(file)
        print(content)
        print(content["name"])

except FileNotFoundError:
    print("That file does not exist!")

except PermissionError:
    print("You do not have permission to read that file!")



