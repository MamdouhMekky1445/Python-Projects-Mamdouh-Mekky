import tkinter as tk
from tkinter import filedialog, messagebox

class TextEditor:
    """
    A simple text editor class using tkinter.
    
    Attributes:
        root (tk.Tk): The root window of the application.
        text_area (tk.Text): The text widget for the editor.
        menu (tk.Menu): The menu bar of the application.
    """
    def __init__(self, root):
        """
        Initialize the text editor with a root window and set up the GUI components.
        
        Args:
            root (tk.Tk): The root window of the application.
        """
        self.root = root
        self.root.title("Simple Text Editor")
        self.root.geometry("800x600")

        # Create a text area widget
        self.text_area = tk.Text(self.root, undo=True)
        self.text_area.pack(fill=tk.BOTH, expand=1)

        # Create a menu bar
        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)

        # File menu
        file_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.exit_editor)

        # Edit menu
        edit_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Undo", command=self.text_area.edit_undo)
        edit_menu.add_command(label="Redo", command=self.text_area.edit_redo)

    def new_file(self):
        """
        Create a new file. Prompt the user to save the current file before creating a new one.
        """
        if messagebox.askokcancel("New", "Do you want to save the current file before creating a new one?"):
            self.save_file()
        self.text_area.delete(1.0, tk.END)

    def open_file(self):
        """
        Open an existing file. Use a file dialog to select the file and display its content in the text area.
        """
        file_path = filedialog.askopenfilename(defaultextension=".txt",
                                               filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.INSERT, content)
                self.root.title(f"Simple Text Editor - {file_path}")

    def save_file(self):
        """
        Save the current file. Use a file dialog to select the location and save the content of the text area.
        """
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, "w") as file:
                content = self.text_area.get(1.0, tk.END)
                file.write(content)
                self.root.title(f"Simple Text Editor - {file_path}")

    def exit_editor(self):
        """
        Exit the text editor. Prompt the user to save the current file before exiting.
        """
        if messagebox.askokcancel("Quit", "Do you want to save the current file before exiting?"):
            self.save_file()
        self.root.destroy()

if __name__ == "__main__":
    # Create the main window
    root = tk.Tk()
    # Initialize the text editor with the main window
    editor = TextEditor(root)
    # Run the application
    root.mainloop()
