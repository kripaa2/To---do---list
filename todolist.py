# Function to display the menu
def show_menu():
    print("\n--- To-Do List Menu ---")
    print("1. View To-Do List")
    print("2. Add a Task")
    print("3. Mark a Task as Completed")
    print("4. Delete a Task")
    print("5. Exit")

# to view the to-do list
def view_tasks(tasks):
    if not tasks:
        print("\nYour to-do list is empty!")
    else:
        print("\n--- Your To-Do List ---")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

# to add a task
def add_task(tasks):
    task = input("\nEnter the task: ")
    tasks.append(task)
    print(f"Task '{task}' added to the list!")

#to mark a task as completed
def complete_task(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("\nEnter the task number to mark as completed: "))
        if 1 <= task_num <= len(tasks):
            completed_task = tasks.pop(task_num - 1)
            print(f"Task '{completed_task}' marked as completed!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

#to delete a task
def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("\nEnter the task number to delete: "))
        if 1 <= task_num <= len(tasks):
            deleted_task = tasks.pop(task_num - 1)
            print(f"Task '{deleted_task}' deleted!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

# Main function
def main():
    tasks = []
    while True:
        show_menu()
        choice = input("\nEnter your choice (1-5): ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("\nExiting the To-Do List. Goodbye!")
            break
        else:
            print("\nInvalid choice! Please try again.")

# Run the program
if __name__ == "__main__":
    main()