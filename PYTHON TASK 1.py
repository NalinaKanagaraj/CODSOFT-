tasks = []
def display_menu():
    print("\nTo-Do List Application")
    print("1. View all tasks")
    print("2. Add a new task")
    print("3. Update a task")
    print("4. Delete a task")
    print("5. Exit")

def view_tasks():
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("\nYour tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
def add_task():
    task = input("Enter the new task: ")
    tasks.append(task)
    print(f"Task '{task}' added successfully.")
def update_task():
    view_tasks()
    if tasks:
        try:
            task_num = int(input("Enter the task number to update: "))
            if 1 <= task_num <= len(tasks):
                new_task = input("Enter the updated task: ")
                tasks[task_num - 1] = new_task
                print(f"Task {task_num} updated to '{new_task}'.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")
def delete_task():
    view_tasks()
    if tasks:
        try:
            task_num = int(input("Enter the task number to delete: "))
            if 1 <= task_num <= len(tasks):
                removed_task = tasks.pop(task_num - 1)
                print(f"Task '{removed_task}' deleted.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")
def main():
    while True:
        display_menu()
        choice = input("Choose an option (1-5): ")
       
        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            update_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
