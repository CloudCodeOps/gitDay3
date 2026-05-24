# task_manager.py

tasks = []

def show_menu():
    print("\n--- Task Manager ---")
    print("1. Add Task")
   
    print("3. Delete Task")
    print("4. Exit")



def view_tasks():
    if not tasks:
        print("No tasks available.")
        return
    print("\nYour Tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

def delete_task():
    view_tasks()
    if tasks:
        try:
            num = int(input("Enter task number to delete: "))
            removed = tasks.pop(num - 1)
            print(f"Deleted: {removed}")
        except (ValueError, IndexError):
            print("Invalid choice.")

def main():
    while True:
        show_menu()
        choice = input("Choose option: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
