tasks = []

def load():
    try:
         with open("task.txt","r") as f:
                for lines in f:
                    tasks.append(lines.strip())
    except FileNotFoundError:
        pass


def save():
    with open("task.txt","w") as f:
        for task in tasks:
            f.write(task + "\n")





def add():
    new_task = input("Enter your new task to add:")
    tasks.append(new_task)
    print("New task added sucessfully.")
    save()

def view():
    if not tasks:
        print("No task yet!")
    else:
        for a, task in enumerate(tasks, start=1):
            print(f"{a}){task}")


def update():
    print("Your task list:")
    if not tasks:
        print("No task to update!")
        return
    view()

    try:
        num_task = int(input("Enter task number to update:"))
    except ValueError:
        print("Please enter task number!")
        return

    if 1 <= num_task <= len(tasks):
        upd_task = input("Enter the new task:")
        tasks[num_task - 1] = upd_task
        print("Task updated successfully.")
        save()
    else:
        print("Invalid task number!")


def delete():
    print("Your task list:")
    if not tasks:
        print("No task to delete!")
        return
    view()

    try:
        dele = int(input("Enter the task number to delete:"))
    except ValueError:
        print("Please enter task number!")
        return

    if 1 <= dele <= len(tasks):
        delete_task = tasks.pop(dele - 1)
        print(f"Task {delete_task} deleted successfully")
        save()
    else:
        print("Invalid task numebr!")


load()

print("-----Welcome to Habit Fixer App-----")
print("Let's start your day with your tasks.")
if not tasks:
    try:
        total_tasks = int(input("How many task are there for today?:"))
    except ValueError:
        print("Invalid value!")
        total_tasks = 0


    for i in range(1, total_tasks + 1):
        name_tasks = input(f"Enter your task {i}:")
        tasks.append(name_tasks)
    save()

else:
    print(f"You haved {len(tasks)} saved tasks to complete.")

while True:
    print("Select the any option:")
    print("1.Add new task")
    print("2.View existing tasks")
    print("3.Update a task")
    print("4.Delete a task")
    print("5.Exit")

    try:
        option = int(input("Enter the option: "))
    except ValueError:
        print("Invalid option!!,please pick 1-5")
        continue

    if option == 1:
        add()

    elif option == 2:
        view()

    elif option == 3:
        update()

    elif option == 4:
        delete()

    elif option == 5:
        print("We hope you have completed your tasks :)")
        break

    else:
        print("Invalid value!!")
