import tkinter as tk
from tkinter import messagebox, filedialog

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x450")

        self.tasks = []

        self.task_entry = tk.Entry(root, width = 35)
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        self.task_listbox = tk.Listbox(root, width=45, height=15)
        self.task_listbox.pack(pady=10)

        self.delete_button = tk.Button(root, text="Delete Selected Task", command=self.delete_task)
        self.delete_button.pack(pady=5)

        self.save_button = tk.Button(root, text="Save To-Do", command=self.save_tasks)
        self.save_button.pack(pady=5)

        self.load_button = tk.Button(root, text="Load Tasks", command=self.load_tasks)
        self.load_button.pack(pady=5)

        

    

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Task cannot be empty")

    def delete_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            self.task_listbox.delete(index)
            del self.tasks[index]
        else:
            messagebox.showwarning("Selection Error", "Please select a task to delete")


    def save_tasks(self):
        filepath = filedialog.asksaveasfilename(defaultextension=".txt",
                                                filetypes=[("Text Files", "*.txt")])
        
        if filepath:
            with open(filepath, 'w') as file:
                for task in self.tasks:
                    file.write(task + '\n')

    def load_tasks(self):
        filepath = filedialog.askopenfilename(filetypes=[("Text Files", "*txt")])
        if filepath:
            with open(filepath, 'r') as file:
                self.tasks = [line.strip() for line in file.readlines()]
            self.task_listbox.delete(0, tk.END)
            for task in self.tasks:
                self.task_listbox.insert(tk.END, task)



if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()


