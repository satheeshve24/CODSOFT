import json
from datetime import datetime


def display_menu():
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Mark Task as Done")
    print("4. Remove Task")
    print("5. Sort Tasks by Due Date")
    print("6. Exit")

def view_todo_list(todo_list):
    if not todo_list:
        print("Your to-do list is empty.")
    else:
        print("To-Do List:")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task['task']} - Due: {task['due_date'] if task['due_date'] else 'No Due Date'}")


def add_task(todo_list):
    task = input("Enter the task: ")
    due_date = input("Enter due date (optional, leave blank if none): ")
    if due_date:
        try:
            due_date = datetime.strptime(due_date, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
            return
    else:
        due_date = None
    todo_list.append({"task": task, "due_date": due_date})
    print("Task added successfully.")


def mark_task_done(todo_list):
    view_todo_list(todo_list)
    index = int(input("Enter the task number to mark as done: ")) - 1
    if 0 <= index < len(todo_list):
        print(f"Task '{todo_list[index]['task']}' marked as done.")
        todo_list.pop(index)
    else:
        print("Invalid task number.")


def remove_task(todo_list):
    view_todo_list(todo_list)
    index = int(input("Enter the task number to remove: ")) - 1
    if 0 <= index < len(todo_list):
        print(f"Task '{todo_list[index]['task']}' removed.")
        todo_list.pop(index)
    else:
        print("Invalid task number.")


def sort_tasks(todo_list):
    todo_list.sort(key=lambda x: x['due_date'] if x['due_date'] else datetime.max.date())

def save_tasks(todo_list):
    with open("todo_list.json", "w") as file:
        json.dump(todo_list, file)
    print("Tasks saved to file.")


def load_tasks():
    try:
        with open("todo_list.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

todo_list = load_tasks()
while True:
    display_menu()
    choice = input("Enter your choice: ")
    if choice == "1":
        view_todo_list(todo_list)
    elif choice == "2":
        add_task(todo_list)
    elif choice == "3":
        mark_task_done(todo_list)
    elif choice == "4":
        remove_task(todo_list)
    elif choice == "5":
        sort_tasks(todo_list)
        print("Tasks sorted by due date.")
    elif choice == "6":
        save_tasks(todo_list)
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
