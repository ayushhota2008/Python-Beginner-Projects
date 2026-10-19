print("###################--Welcome to Calsi--###################")


def add():
    try:
        ele1 = float(input("Enter your first number:"))
        ele2 = float(input("Enter your second number:"))
        result = ele1 + ele2
        print(f"Sum of {ele1} and {ele2} is {result}")
    except ValueError:
        print("Invalid value!!")


def subs():
    try:
        ele1 = float(input("Enter your first number:"))
        ele2 = float(input("Enter your second number:"))
        subtract = ele1 - ele2
        print(f"Subtraction of {ele1} and {ele2} is {subtract}")
    except ValueError:
        print("Invalid value!!")


def multiplication():
    try:
        ele1 = float(input("Enter your first number:"))
        ele2 = float(input("Enter your second number:"))
        product = ele1 * ele2
        print(f"Multiplication of {ele1} and {ele2} is {product}")
    except ValueError:
        print("Invalid value!!")


def division():
    try:
        ele1 = float(input("Enter your first number:"))
        ele2 = float(input("Enter your second number:"))
        result = ele1 / ele2
        print(f"Division of {ele1} and {ele2} is {result}")
    except ZeroDivisionError:
        print("You cannot divide with zero")
    except ValueError:
        print("Please enter valid number!")


while True:
    print("Choose the operation-")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Division")
    print("4.Multiplication")
    print("5.Exit")

    try:
        user = int(input("Enter your operation:"))
    except ValueError:
        print("Enter correct value!!")
        continue

    if user == 1:
        add()

    elif user == 2:
        subs()

    elif user == 3:
        division()

    elif user == 4:
        multiplication()

    elif user == 5:
        print("Exiting....")
        print("Thanks for using Calsi :) ")
        break

    else:
        print("invalid choice,please pick 1 to 5")
