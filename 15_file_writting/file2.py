import json

employees1 = {"name": "ABC",
              "age": "EFG",
              "position": "HIJ"}



json_file_path = "output.json"

try:
    with open(file=json_file_path, mode="w") as file:

        json.dump(employees1, file, indent=4)

        print(f"json file '{json_file_path}' has been created.")

except FileExistsError:
    print("That file already exists.")



