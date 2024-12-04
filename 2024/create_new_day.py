import os
import shutil


def create_day_folder(day_number):
    folder_name = f"day_{day_number}"
    os.makedirs(folder_name, exist_ok=True)

    files_to_create = [
        f"{folder_name}/example_in.txt",
        f"{folder_name}/input.txt",
    ]

    for file_path in files_to_create:
        with open(file_path, "w") as file:
            file.write("")  # Create an empty file

    # Copy the template file to the new .py file
    template_file = "./day_template"
    destination_file = f"{folder_name}/{folder_name}.py"
    shutil.copy(template_file, destination_file)


def main():
    day_number = int(input("Enter the day number to create a folder for: "))
    create_day_folder(day_number)


if __name__ == "__main__":
    main()
