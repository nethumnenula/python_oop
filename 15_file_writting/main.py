

txt_data = "I like gaming."
txt_file_path = "output.txt"

with open(file=txt_file_path, mode="w") as file:
    file.write(txt_data)
    print(f"txt file '{txt_file_path}' has been created.")
