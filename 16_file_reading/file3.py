import csv

csv_file_path = "output.csv"

try:
    with open(file=csv_file_path, mode="r") as file:

        content = csv.reader(file)
        for line in content:
            print(line)
            #print(line[0])

except FileNotFoundError:
    print("That file does not exist!")

except PermissionError:
    print("You do not have permission to read that file!")



