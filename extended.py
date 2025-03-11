import json
from datetime import datetime

def show_menu():
    """
    Displays the main menu for the to-do list program.
    """
    print("\n--- To-Do List Menu ---")
    print("1. View To-Do List")
    print("2. Add a Task")
    print("3. Edit a Task")
    print("4. Mark a Task as Completed")
    print("5. Delete a Task")
    print("6. Search Tasks")
    print("7. Sort Tasks")
    print("8. Exit")


def view_tasks(tasks):
    """
    Displays the current to-do list or a message if the list is empty.
    """
    if not tasks:
        print("\nYour to-do list is empty!")
    else:
        print("\n--- Your To-Do List ---")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task['task']} (Priority: {task['priority']}, Due: {task['due_date']}, Completed: {'Yes' if task['completed'] else 'No'})")


def get_task_number(tasks, prompt):
    """
    Helper function to get a valid task number from the user.
    """
    while True:
        try:
            task_num = int(input(prompt))
            if 1 <= task_num <= len(tasks):
                return task_num
            else:
                print("Invalid task number! Please enter a number between 1 and", len(tasks))
        except ValueError:
            print("Invalid input! Please enter a valid number.")


def add_task(tasks):
    """
    Adds a new task to the to-do list with priority and due date.
    """
    task_name = input("\nEnter the task: ").strip()
    if not task_name:
        print("You must enter a valid task!")
        return

    priority = input("Enter the priority (High/Medium/Low): ").strip().capitalize()
    if priority not in ["High", "Medium", "Low"]:
        print("Invalid priority! Setting to Medium.")
        priority = "Medium"

    due_date = input("Enter the due date (YYYY-MM-DD): ").strip()
    try:
        due_date = datetime.strptime(due_date, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format! Setting due date to today.")
        due_date = datetime.today().date()

    task = {
        "task": task_name,
        "priority": priority,
        "due_date": due_date,
        "completed": False
    }
    tasks.append(task)
    print(f"Task '{task_name}' added to the list!")


def edit_task(tasks):
    """
    Edit an existing task.
    """
    if tasks:
        view_tasks(tasks)
        task_num = get_task_number(tasks, "\nEnter the task number to edit: ")

        task = tasks[task_num - 1]
        print(f"Editing task: {task['task']}")

        task_name = input("Enter new task description (leave blank to keep current): ").strip()
        if task_name:
            task["task"] = task_name

        priority = input(f"Enter new priority (High/Medium/Low) [Current: {task['priority']}]: ").strip().capitalize()
        if priority in ["High", "Medium", "Low"]:
            task["priority"] = priority

        due_date = input(f"Enter new due date (YYYY-MM-DD) [Current: {task['due_date']}]: ").strip()
        if due_date:
            try:
                task["due_date"] = datetime.strptime(due_date, "%Y-%m-%d").date()
            except ValueError:
                print("Invalid date format! Keeping the current date.")

        print(f"Task updated: {task['task']}")
    else:
        print("\nYour to-do list is empty!")


def complete_task(tasks):
    """
    Marks a task as completed by removing it from the list.
    """
    if tasks:
        view_tasks(tasks)
        task_num = get_task_number(tasks, "\nEnter the task number to mark as completed: ")
        task = tasks[task_num - 1]
        task["completed"] = True
        print(f"Task '{task['task']}' marked as completed!")
    else:
        print("\nYour to-do list is empty!")


def delete_task(tasks):
    """
    Deletes a task from the to-do list.
    """
    if tasks:
        view_tasks(tasks)
        task_num = get_task_number(tasks, "\nEnter the task number to delete: ")
        deleted_task = tasks.pop(task_num - 1)
        print(f"Task '{deleted_task['task']}' deleted!")
    else:
        print("\nYour to-do list is empty!")


def search_tasks(tasks):
    """
    Allows the user to search for tasks by a keyword.
    """
    keyword = input("\nEnter keyword to search: ").strip().lower()
    results = [task for task in tasks if keyword in task['task'].lower()]
    if results:
        print("\n--- Search Results ---")
        for task in results:
            print(f"{task['task']} (Priority: {task['priority']}, Due: {task['due_date']}, Completed: {'Yes' if task['completed'] else 'No'})")
    else:
        print("No tasks found with that keyword!")


def sort_tasks(tasks):
    """
    Allows the user to sort tasks by priority or due date.
    """
    print("\nSort by:")
    print("1. Priority")
    print("2. Due Date")
    choice = input("Enter your choice: ")

    if choice == "1":
        tasks.sort(key=lambda x: x['priority'], reverse=True)
        print("Tasks sorted by priority!")
    elif choice == "2":
        tasks.sort(key=lambda x: x['due_date'])
        print("Tasks sorted by due date!")
    else:
        print("Invalid choice!")


def save_tasks(tasks, filename="tasks.json"):
    """
    Save the tasks to a file so they persist.
    """
    with open(filename, 'w') as file:
        json.dump(tasks, file, default=str)
    print("Tasks saved!")


def load_tasks(filename="tasks.json"):
    """
    Load tasks from a file.
    """
    try:
        with open(filename, 'r') as file:
            tasks = json.load(file)
            # Convert string dates back to datetime objects
            for task in tasks:
                task['due_date'] = datetime.strptime(task['due_date'], '%Y-%m-%d').date()
            return tasks
    except FileNotFoundError:
        return []


def main():
    """
    Main function that controls the flow of the to-do list program.
    """
    tasks = load_tasks()

    while True:
        show_menu()
        choice = input("\nEnter your choice (1-8): ").strip()

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            edit_task(tasks)
        elif choice == "4":
            complete_task(tasks)
        elif choice == "5":
            delete_task(tasks)
        elif choice == "6":
            search_tasks(tasks)
        elif choice == "7":
            sort_tasks(tasks)
        elif choice == "8":
            save_tasks(tasks)
            print("\nExiting the To-Do List. Goodbye!")
            break
        else:
            print("\nInvalid choice! Please try again.")


# Run the program
if __name__ == "__main__":
    main()
# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Try programiz.pro")