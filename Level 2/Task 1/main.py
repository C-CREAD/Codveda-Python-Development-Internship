"""
Created By: Shingai Dzinotyiweyi

Task 1: To-Do List Application
Build a simple command-line to-do list application.
Users should be able to add, delete, mark as done, and list tasks.

Objectives:
✅ - Implement the ability to add, view, and delete tasks.
✅ - Store the tasks in a file (either CSV or JSON format).
✅ - Mark tasks as completed.
✅ - Implement basic error handling (e.g., trying to delete a task that doesn't exist).
"""
import datetime
import csv
from tabulate import tabulate

print("---------------To-Do List Application--------------------\n")

field_names = ['Task_No.', 'Title', 'Description', 'Date_Created', 'Is_Completed']

# Create .csv file for reading and writing
try:
    with open("tasks.csv", newline="") as read_file:
        print("File Exists.\n\n")
except FileNotFoundError:
    print("File does not exist. Creating new .csv file.")
    with open("tasks.csv", "a+", newline="", encoding="utf-8") as write_file:
        write = csv.DictWriter(write_file, fieldnames=field_names, delimiter=',')
        write.writeheader()


def get_task_number():
    """
    Get the task number of a row by reading the .csv file
    """
    try:
        with open("tasks.csv", "r", newline="", encoding="utf-8") as read_file:
            reader = list(csv.DictReader(read_file, delimiter=','))
            if len(reader) == 0:
                return 1
            else:
                return int(reader[-1]['Task_No.']) + 1

    except (FileNotFoundError, ValueError, IndexError):
        return 1


def add_task():
    """
    Requests the user to enter a new task
    """
    print("Enter the following task details:\n")
    task_number = get_task_number()
    title = input("Title: ").strip()
    description = input("Description: ").strip()
    date_created = datetime.datetime.today().date()
    task_completed = False

    if title and description:
        with open("tasks.csv", "a+", newline="", encoding="utf-8") as write_file:
            write = csv.DictWriter(write_file, fieldnames=field_names, delimiter=',')
            write.writerow({'Task_No.': task_number,
                            'Title': title,
                            'Description': description,
                            'Date_Created': date_created,
                            'Is_Completed': task_completed})

            print("Task added.\n")
    else:
        print("Please enter a valid title and description!\n")


def view_tasks():
    """
    View all tasks from the .csv file.
    """
    try:
        with open("tasks.csv", "r", newline="", encoding="utf-8") as read_file:
            reader = list(csv.DictReader(read_file, delimiter=','))

            if not reader:
                print("No tasks found. Add a task first!\n")
                return

            task_table = tabulate(reader, headers="keys", tablefmt='grid')
            print("\n" + task_table + "\n")
    except FileNotFoundError:
        print("Tasks file not found.\n")


def complete_task():
    """
    Marks a selected task as complete from the .csv file.
    """
    view_tasks()

    try:
        task_number = int(input("Enter the task number to mark as complete: "))
    except ValueError:
        print("Please enter a valid task number.\n")
        return

    found = False

    with open("tasks.csv", "r", newline="", encoding="utf-8") as read_file:
        reader = list(csv.DictReader(read_file, delimiter=','))

    for task in reader:
        if int(task['Task_No.']) == task_number:
            task['Is_Completed'] = True
            found = True
            break

    if not found:
        print(f"Task No. {task_number} not found or does not exist.\n")
        return

    # Updates the .csv file
    with open("tasks.csv", "w", newline="", encoding="utf-8") as write_file:
        write = csv.DictWriter(write_file, fieldnames=field_names, delimiter=',')
        write.writeheader()
        write.writerows(reader)

    print(f"Task No. {task_number} is completed.\n")


def delete_task():
    """
    Deletes a task from the .csv file
    """
    view_tasks()

    try:
        task_number = int(input("Enter the task number to delete: "))
    except ValueError:
        print("Please enter a valid task number.\n")
        return

    found = False

    with open("tasks.csv", "r", newline="", encoding="utf-8") as read_file:
        reader = list(csv.DictReader(read_file, delimiter=','))

    new_reader = []
    for task in reader:
        if int(task['Task_No.']) != task_number:
            new_reader.append(task)
        else:
            found = True

    if not found:
        print(f"Task No. {task_number} not found or does not exist.\n")
        return

    # Updates the .csv file
    with open("tasks.csv", "w", newline="", encoding="utf-8") as write_file:
        write = csv.DictWriter(write_file, fieldnames=field_names, delimiter=',')
        write.writeheader()
        write.writerows(new_reader)

    print(f"Task No. {task_number} is deleted.\n")


def main_menu():
    """
    Displays the main menu for the user to select between:
    adding/viewing/deleting tasks and marking them as complete
    """
    while True:
        print("---------------To-Do Application--------------------")
        print("1. Add a task")
        print("2. View all tasks")
        print("3. Mark task as complete")
        print("4. Delete a task")
        print("5. Exit")
        print("------------------------------------------\n")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            complete_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Goodbye!\n")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.\n")


main_menu()

# import datetime
# import csv
# from tabulate import tabulate
#
# print("---------------To-Do List Application--------------------\n")
#
# field_names = ['Task_No.','Title', 'Description', 'Date_Created', 'Is_Completed']
#
# # Create .csv file for reading and writing
# try:
#     with open("tasks.csv",  newline="") as read_file:
#         print("File Exists.\n\n")
# except FileNotFoundError:
#     print("File does not exist. Creating new .csv file.")
#     with open("tasks.csv", "a+", newline="", encoding="utf-8") as write_file:
#         write = csv.DictWriter(write_file, fieldnames=field_names, delimiter=',')
#         write.writeheader()
#
# def get_task_number():
#     """
#     Get the task number of a row by reading the .csv file
#     """
#     try:
#         with open("tasks.csv", "r", newline="", encoding="utf-8") as read_file:
#             reader = list(csv.DictReader(read_file, delimiter=','))
#             if len(reader) == 0:
#                 return 1
#             else:
#                 return int(reader[-1]['Task_No.']) + 1
#
#     except (FileNotFoundError, ValueError, IndexError):
#         return 1
#
#
# def add_task():
#     """
#     Requests the user to enter a new task
#     """
#     print("Enter the following task details:\n")
#     task_number = get_task_number()
#     title = input("Title: ")
#     description = input("Description: ")
#     date_created = datetime.datetime.today().date()
#     task_completed = False
#
#     if title != "" and description != "":
#         with open("tasks.csv", "a+", newline="", encoding="utf-8") as write_file:
#             write = csv.DictWriter(write_file, fieldnames=field_names, delimiter=',')
#             write.writerow({'Task_No.': task_number,
#                             'Title': title,
#                             'Description': description,
#                             'Date_Created': date_created,
#                             'Is_Completed': task_completed})
#
#             print("Task added.\n")
#     else:
#         print("Please enter a valid title and description!\n")
#
#
# def view_tasks():
#     """
#     View all tasks from the .csv file.
#     """
#
#     with open("tasks.csv", "r+", newline="") as read_file:
#         reader = list(csv.reader(read_file, delimiter=','))
#         reader.pop(0)  # Remove row headers from list
#
#         task_table = tabulate(reader, headers=field_names, tablefmt='grid')
#         print(task_table)
#
#
# def complete_task():
#     """
#     Marks a selected task as complete from the .csv file.
#     """
#     view_tasks()
#     found = False
#     task_number = int(input("Enter the task number to mark as complete: "))
#
#     with open("tasks.csv", "r+", newline="") as read_file:
#         reader = list(csv.reader(read_file, delimiter=','))
#
#     for task in reader:
#         if int(task['Task_No.'] == task_number):
#             task['Is_Completed'] = True
#             found = True
#             break
#
#     if not found:
#         print(f"Task No. {task_number} not found or does not exist.\n")
#         return
#
#     # Updates the .csv file
#     with open("tasks.csv", "w+", newline="", encoding="utf-8") as write_file:
#         write = csv.DictWriter(write_file, fieldnames=field_names, delimiter=',')
#         write.writeheader()
#         write.writerows(reader)
#
#     print(f"Task No. {task_number} is completed.\n")
#
# def delete_task():
#     """
#     Deletes a task from the .csv file
#     """
#     view_tasks()
#     found = False
#     task_number = int(input("Enter the task number to mark as complete: "))
#
#     with open("tasks.csv", "r+", newline="") as read_file:
#         reader = list(csv.reader(read_file, delimiter=','))
#         print(reader)
#
#         new_reader = []
#         for task in reader:
#             if int(task['Task_No.']) != task_number:
#                 new_reader.append(task)
#             else:
#                 found = True
#
#         if not found:
#             print(f"Task No. {task_number} not found or does not exist.\n")
#             return
#
#         # Updates the .csv file
#         with open("tasks.csv", "w+", newline="", encoding="utf-8") as write_file:
#             write = csv.DictWriter(write_file, fieldnames=field_names, delimiter=',')
#             write.writeheader()
#             write.writerows(new_reader)
#
#         print(f"Task No. {task_number} is deleted.\n")
#
#
#
#
#
# # add_task()
#
# # complete_task()
#
# delete_task()