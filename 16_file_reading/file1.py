

txt_file_path = "output.txt"

try:
    with open(file=txt_file_path, mode="r") as file:
        content = file.read()
        print(content)

except FileNotFoundError:
    print("That file does not exist!")

except PermissionError:
    print("You do not have permission to read that file!")



