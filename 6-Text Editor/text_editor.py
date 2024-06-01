import tkinter as tk
from tkinter import filedialog

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not file_path:
        return
    text_area.delete(1.0, tk.END)
    with open(file_path, "r") as input_file:
        text = input_file.read()
        text_area.insert(tk.END, text)
    window.title(f"Almadrasa text editor by Mamdouh Mekky - {file_path}")

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension="txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not file_path:
        return
    with open(file_path, "w") as output_file:
        text = text_area.get(1.0, tk.END)
        output_file.write(text)
    window.title(f"Almadrasa text editor by Mamdouh Mekky - {file_path}")

def delete_content():
    text_area.delete(1.0, tk.END)

def exit_prog():
    window.destroy()

window = tk.Tk()
window.title("Almadrasa text editor by Mamdouh Mekky")
window.rowconfigure(0, minsize=600)
window.columnconfigure(1, minsize=800)

text_area = tk.Text(window)
button_frame = tk.Frame(window, relief=tk.RAISED)
open_file_btn = tk.Button(button_frame, text="Open file", command=open_file)
save_file_btn = tk.Button(button_frame, text="Save as", command=save_file)
delete_content_btn = tk.Button(button_frame, text="Delete", command=delete_content)
exit_btn = tk.Button(button_frame, text="Exit", command=exit_prog)

text_area.grid(column=1, row=0, sticky='nsew', padx=5, pady=10)
button_frame.grid(column=0, row=0, sticky='ns', padx=5, pady=10)
open_file_btn.grid(column=0, row=0, sticky='ew', padx=5, pady=10)
save_file_btn.grid(column=0, row=1, sticky='ew', padx=5, pady=10)
delete_content_btn.grid(column=0, row=2, sticky='ew', padx=5, pady=10)
exit_btn.grid(column=0, row=3, sticky='ew', padx=5, pady=10)

window.mainloop()
