from pathlib import Path
import os

def create_file():
    try:
        file_name = input("Enter the file name you want to create:")
        path = Path(file_name)
        if not path.exists():
            with open(path,"w") as f:
                data = input("Enter the data you want too write in the file:")
                f.write(data)
            print("File is created successfully.")
        else:
            print("File already exists.")
    except Exception as error:
        print(f"An error occured as {error}")




def read_file():
    try:
        file_name = input("Enter the file name you want to read:")
        path = Path(file_name)
        if path.exists():
            with open(path,"r") as f:
                data = f.read()
            print(f"File content is: \n{data}")
        else:
            print("File does not exist.")
    except Exception as error:
        print(f"An error occured as {error}")




def update_file():
    try:
        file_name = input("Enter the file name you want to update:")
        path = Path(file_name)
        if path.exists():
            print("\n")
            print("Options:")
            print("1. Rename the file")
            print("2. Append new data to the file")
            print("3. Overwrite the file")
            print("\n")

            selection = int(input("Select what you want to do with the file: "))

            if selection == 1:
                new_name = input("Enter the new name for the file:")
                new_path = Path(new_name)
                if not new_path.exists():
                    path.rename(new_path)
                    print("File is renamed successfully.")
                else:
                 print("File with this name already exists.")

            elif selection == 2:
                with open(path,"a") as f:
                    new_data = input("Enter the new data you want to append:")
                    f.write(" \n" + new_data)
                print("New data is appended successfully.") 

            elif selection == 3:
                with open(path,"w") as f:
                    new_data = input("Enter the new data you want to overwrite:")
                    f.write(new_data)
                print("Overwrite is done successfully.")
    except Exception as error:
        print(f"An error occured as {error}")



                
def delete_file():
    try:
        file_name = input("Enter the file name you want to delete:")
        path = Path(file_name)

        if path.exists():
            path.unlink()
            print("File is deleted successfully.")
        else:
            print("No such file exists.")
    except Exception as error:
        print(f"An error occured as {error}")






print("             ~~~~WELCOME TO FILE HUB~~~~         ")
print("This is a program where you can create,read,update and delete a file(CURD Operations)")


while True:
    print("\nChoose the operation you want to perform:")
    print("1. Create a file                2. Read a file")
    print("3. Update a file                4. Delete a file")
    print("\n")


    operation = int(input("Enter your choice (1-4): "))

    if operation == 1:
        create_file()
    if  operation == 2:
        read_file()
    if operation == 3:
        update_file()
    if operation == 4:
        delete_file()



    