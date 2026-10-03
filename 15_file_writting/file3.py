import csv
from os import write

employees1 = [["Name", "Age", "Job"],
              ["Nethum2", 22, "SE"],
              ["Nethum2", 23, "DA"],
              ["Nethum3", 24, "GD"]]



csv_file_path = "output.csv"

try:
    with open(file=csv_file_path, mode="w", newline="") as file:

        writer = csv.writer(file)
        for row in employees1:
            writer.writerow(row)

        print(f"csv file '{csv_file_path}' has been created.")

except FileExistsError:
    print("That file already exists.")



