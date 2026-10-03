
employees1 = ["ABC", "EFG", "HIJ"]


txt_data = "I like gaming."
txt_file_path = "output.txt"

try:
    with open(file=txt_file_path, mode="a") as file:

        file.write(txt_data + "\n")

        for employee in employees1:
            file.write(employee+ "\n")


        print(f"txt file '{txt_file_path}' has been created.")

except FileExistsError:
    print("That file already exists.")



