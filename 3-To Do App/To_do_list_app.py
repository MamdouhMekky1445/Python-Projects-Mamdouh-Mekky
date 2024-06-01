# Initialize an empty list to store tasks
todo_tasks = []

# Start an infinite loop to continuously prompt the user for commands
while True:
    # Prompt the user to enter a command and strip any leading/trailing whitespace
    user_input_command = input("Please choose between these four commands: 'Add', 'View', 'Remove', 'Exit': ").strip()

    # Check if the command is 'add' (case insensitive)
    if user_input_command.lower() == 'add':
        # Prompt the user to enter a task and strip any leading/trailing whitespace
        task = input("Enter the task to add: ").strip()
        # Check if the task is not empty
        if task:
            # Add the task to the list of tasks
            todo_tasks.append(task)
            print('Task is successfully added.')
        else:
            print("Task cannot be empty.")
    
    # Check if the command is 'view' (case insensitive)
    elif user_input_command.lower() == 'view':
        # Check if there are no tasks to view
        if not todo_tasks:
            print("There are no tasks to view.")
        else:
            # Print all tasks in the list
            print('Your tasks:')
            for task in todo_tasks:
                print(task)
    
    # Check if the command is 'remove' (case insensitive)
    elif user_input_command.lower() == 'remove':
        # Check if there are no tasks to remove
        if not todo_tasks:
            print("There are no tasks to remove.")
        else:
            # Prompt the user to enter the task to remove and strip any leading/trailing whitespace
            task_to_remove = input("Enter the task to remove: ").strip()
            # Check if the task exists in the list
            if task_to_remove in todo_tasks:
                # Remove the task from the list
                todo_tasks.remove(task_to_remove)
                print("The task is removed successfully.")
            else:
                print(f"There is no task with the name '{task_to_remove}'.")
    
    # Check if the command is 'exit' (case insensitive)
    elif user_input_command.lower() == 'exit':
        # Print a message and break the loop to exit the program
        print("Exiting the program.")
        break
    
    # If the command is not recognized, prompt the user again
    else:
        print("Please choose between these four commands: 'Add', 'View', 'Remove', 'Exit'.")
