# todo_list.py

class ToDoList:
    def __init__(self):
        # Initialize an empty list to store tasks
        self.tasks = []

    def add_task(self, task):
        # Check if the task is not empty
        if task:
            # Add the task to the list of tasks
            self.tasks.append(task)
            return f"Task '{task}' added."
        else:
            return "Task cannot be empty."

    def view_tasks(self):
        # Check if there are no tasks to view
        if not self.tasks:
            return "There are no tasks to view."
        else:
            # Create a string representation of all tasks in the list
            task_list = "Here are your tasks:\n"
            for i, task in enumerate(self.tasks, start=1):
                task_list += f"{i}. {task}\n"
            return task_list

    def remove_task(self, task_to_remove):
        # Check if there are no tasks to remove
        if not self.tasks:
            return "There are no tasks to remove."

        # Check if the task exists in the list
        if task_to_remove in self.tasks:
            # Remove the task from the list
            self.tasks.remove(task_to_remove)
            return f"Task '{task_to_remove}' removed."
        else:
            return f"There is no task with the name '{task_to_remove}'."
