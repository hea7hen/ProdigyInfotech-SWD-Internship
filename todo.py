tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added!")

def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print(f"Task '{task}' removed!")
    else:
        print("Task not found.")

def view_tasks():
    if tasks:
        print("\nTo-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    else:
        print("No tasks added yet!")

while True:
    print("\n1. Add Task\n2. Remove Task\n3. View Tasks\n4. Exit")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        task = input("Enter task: ")
        add_task(task)
    elif choice == "2":
        task = input("Enter task to remove: ")
        remove_task(task)
    elif choice == "3":
        view_tasks()
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice, please try again.")
