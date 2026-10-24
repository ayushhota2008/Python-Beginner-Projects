contacts = {}


def load():
    try:
        with open("contacts.txt", "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                name, phone = line.split(":")
                contacts[name] = phone
    except FileNotFoundError:
        pass


def is_valid(phone):
    count = 0
    all_digit = True
    start_with_zero = False
    for i in phone:
        if count == 0 and i == "0":
            start_with_zero = True
        if not ("0" <= i <= "9"):
            all_digit = False

        count += 1
    if count == 10 and all_digit and not start_with_zero:
        return True
    return False


def save():
    with open("contacts.txt", "w") as f:
        for name, phone in contacts.items():
            f.write(f"{name}:{phone}\n")


def add():
    name = input("Enter name:").strip().title()

    if name == "":
        print("Name cannot be empty!")
        return

    if ":" in name:
        print("Name cannot contain ':'")
        return

    phone = input("Enter mobile number:")

    if name in contacts:
        print(f"{name} already exixts!")
        return

    if is_valid(phone):
        contacts[name] = phone
        print(f"New contact {name} added successfully.")
        save()
    else:
        print(f"Invalid number!")


def view():
    if not contacts:
        print("No contacts exists.")
    else:
        print("View contacts-")
        for name, phone in contacts.items():
            print(f"{name} : {phone}")


def search():
    if not contacts:
        print("No contacts exists.")
        return

    S_name = input("Enter name to search:").strip().title()
    found = False
    for name, phone in contacts.items():
        if S_name == name:
            print(f"{name} : {phone}")
            found = True
    if not found:
        print(f"{S_name} not found!")


def delete():
    if not contacts:
        print("No contacts to delete!")
        return

    del_name = input("Enter name to delete:").strip().title()
    if del_name in contacts:
        del contacts[del_name]
        print(f"{del_name} deleted.")
        save()
    else:
        print(f"{del_name} not found.")


print("------CONTACT BOOK------")
load()


while True:
    print("Choose option:")
    print("1.Add contacts")
    print("2.View contacts")
    print("3.Search contacts")
    print("4.Delete contacts")
    print("5.Exit")

    try:
        option = int(input("Enter the option: "))
    except ValueError:
        print("Please enter the option.")
        continue

    if option == 1:
        add()
    elif option == 2:
        view()
    elif option == 3:
        search()
    elif option == 4:
        delete()
    elif option == 5:
        break
    else:
        print("Please choose the valid option!")
