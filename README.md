# TODO_LIST

import os

# File to store tasks
TASKS_FILE = 'tasks.txt'

# Load tasks from file
def load_tasks():
    tasks = []
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            for line in file:
                task, status = line.strip().split(',')
                tasks.append({'task': task, 'completed': status == 'True'})
    return tasks

# Save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        for task in tasks:
            file.write(f"{task['task']},{task['completed']}\n")

# Add a new task
def add_task():
    task = input("Enter a new task: ")
    tasks = load_tasks()
    tasks.append({'task': task, 'completed': False})
    save_tasks(tasks)
    print(f"Task '{task}' added successfully!")

# View all tasks
def view_tasks():
    tasks = load_tasks()
    if tasks:
        print("\n--- To-Do List ---")
        for idx, task in enumerate(tasks, start=1):
            status = "Completed" if task['completed'] else "Pending"
            print(f"{idx}. {task['task']} - {status}")
    else:
        print("No tasks found.")

# Update an existing task
def update_task():
    tasks = load_tasks()
    view_tasks()
    task_number = int(input("Enter the task number to update: ")) - 1
    if 0 <= task_number < len(tasks):
        new_task = input("Enter the updated task: ")
        tasks[task_number]['task'] = new_task
        save_tasks(tasks)
        print("Task updated successfully!")
    else:
        print("Invalid task number.")

# Delete a task
def delete_task():
    tasks = load_tasks()
    view_tasks()
    task_number = int(input("Enter the task number to delete: ")) - 1
    if 0 <= task_number < len(tasks):
        deleted_task = tasks.pop(task_number)
        save_tasks(tasks)
        print(f"Task '{deleted_task['task']}' deleted successfully!")
    else:
        print("Invalid task number.")

# Mark a task as completed
def mark_task_complete():
    tasks = load_tasks()
    view_tasks()
    task_number = int(input("Enter the task number to mark as complete: ")) - 1
    if 0 <= task_number < len(tasks):
        tasks[task_number]['completed'] = True
        save_tasks(tasks)
        print(f"Task '{tasks[task_number]['task']}' marked as completed!")
    else:
        print("Invalid task number.")

# Main program loop
def main():
    while True:
        print("\n--- To-Do List App ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task as Completed")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            update_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            mark_task_complete()
        elif choice == '6':
            print("Exiting To-Do List App.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
