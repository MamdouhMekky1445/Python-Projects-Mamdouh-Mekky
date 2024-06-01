# todo_app.py

from todo_list import ToDoList

class ToDoApp:
    def __init__(self):
        # Initialize an instance of ToDoList
        self.todo_list = ToDoList()

    def start_program(self):
        # Start an infinite loop to continuously prompt the user for commands
        while True:
            # Prompt the user to enter a command and strip any leading/trailing whitespace
            command = input("Choose a command (Add/View/Remove/Exit): ").strip().lower()

            # Call the appropriate method based on the user's command
            if command == "add":
                self.add_task()
            elif command == "view":
                self.view_tasks()
            elif command == "remove":
                self.remove_task()
            elif command == "exit":
                print("Exiting the program.")
                break
            else:
                print("Please choose between these four commands: 'Add', 'View', 'Remove', 'Exit'")

    def add_task(self):
        # Prompt the user to enter a task and strip any leading/trailing whitespace
        task = input("Enter the task to add: ").strip()
        # Add the task to the ToDoList instance and print the result
        print(self.todo_list.add_task(task))

    def view_tasks(self):
        # View tasks from the ToDoList instance and print the result
        print(self.todo_list.view_tasks())

    def remove_task(self):
        # Prompt the user to enter the task to remove and strip any leading/trailing whitespace
        task_to_remove = input("Enter the task name to remove: ").strip()
        # Remove the task from the ToDoList instance and print the result
        print(self.todo_list.remove_task(task_to_remove))
