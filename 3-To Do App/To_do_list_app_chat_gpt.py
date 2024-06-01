# Define the main function to start the program
def start_program():
    # Initialize an empty list to store tasks
    tasks = []
    
    # Start an infinite loop to continuously prompt the user for commands
    while True:
        # Prompt the user to enter a command and strip any leading/trailing whitespace
        command = input("Choose a command (Add/View/Remove/Exit): ").strip().lower()

        # Call the appropriate function based on the user's command
        if command == "add":
            add_task(tasks)
        elif command == "view":
            view_tasks(tasks)
        elif command == "remove":
            remove_task(tasks)
        elif command == "exit":
            print("Exiting the program.")
            break
        else:
            print("Please choose between these four commands: 'Add', 'View', 'Remove', 'Exit'")

# Define the function to add a task
def add_task(tasks):
    # Prompt the user to enter a task and strip any leading/trailing whitespace
    task = input("Enter the task to add: ").strip()
    
    # Check if the task is not empty
    if task:
        # Add the task to the list of tasks
        tasks.append(task)
        print(f"Task '{task}' added.")
    else:
        print("Task cannot be empty.")

# Define the function to view tasks
def view_tasks(tasks):
    # Check if there are no tasks to view
    if not tasks:
        print("There are no tasks to view.")
    else:
        # Print all tasks in the list
        print("Here are your tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

# Define the function to remove a task
def remove_task(tasks):
    # Check if there are no tasks to remove
    if not tasks:
        print("There are no tasks to remove.")
        return

    # Prompt the user to enter the task to remove and strip any leading/trailing whitespace
    task_to_remove = input("Enter the task name to remove: ").strip()
    
    # Check if the task exists in the list
    if task_to_remove in tasks:
        # Remove the task from the list
        tasks.remove(task_to_remove)
        print(f"Task '{task_to_remove}' removed.")
    else:
        print(f"There is no task with the name '{task_to_remove}'.")

# If this script is run directly, start the program
if __name__ == "__main__":
    start_program()
