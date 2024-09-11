import tkinter as tk
from tkinter import ttk
import random

class TodoView(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Stylish Animated Todo List")
        self.geometry("400x600")
        self.configure(bg="#f0f0f0")

        self.colors = ["#FF6B6B", "#4ECDC4", "#45B7D1", "#FFA07A", "#98D8C8"]
        self.create_styles()
        self.create_widgets()

    def create_styles(self):
        self.style = ttk.Style()
        self.style.theme_use("clam")

        self.style.configure("TEntry", foreground="#333333", background="#ffffff", fieldbackground="#ffffff", borderwidth=0)
        self.style.map("TEntry", foreground=[('focus', '#000000')], fieldbackground=[('focus', '#ffffff')])

        self.style.configure("TButton", foreground="#ffffff", background="#4CAF50", font=("Arial", 12, "bold"), borderwidth=0)
        self.style.map("TButton", background=[('active', '#45a049')])

        self.style.configure("Delete.TButton", foreground="#ffffff", background="#f44336", font=("Arial", 10), borderwidth=0)
        self.style.map("Delete.TButton", background=[('active', '#d32f2f')])

        self.style.configure("TCheckbutton", background="#ffffff")

    def create_widgets(self):
        header_frame = tk.Frame(self, bg="#4CAF50", height=60)
        header_frame.pack(fill=tk.X)

        title_label = tk.Label(header_frame, text="My Todo List", font=("Arial", 18, "bold"), bg="#4CAF50", fg="#ffffff")
        title_label.pack(pady=10)

        input_frame = tk.Frame(self, bg="#f0f0f0", pady=20)
        input_frame.pack(fill=tk.X)

        self.task_entry = ttk.Entry(input_frame, font=("Arial", 14), width=25, style="TEntry")
        self.task_entry.pack(side=tk.LEFT, padx=(20, 10))

        self.add_button = ttk.Button(input_frame, text="Add Task", command=self.controller.add_task, style="TButton")
        self.add_button.pack(side=tk.LEFT)

        self.task_frame = tk.Frame(self, bg="#f0f0f0")
        self.task_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        self.task_canvas = tk.Canvas(self.task_frame, bg="#f0f0f0", highlightthickness=0)
        self.task_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar = ttk.Scrollbar(self.task_frame, orient=tk.VERTICAL, command=self.task_canvas.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.task_canvas.configure(yscrollcommand=self.scrollbar.set)
        self.task_canvas.bind('<Configure>', lambda e: self.task_canvas.configure(scrollregion=self.task_canvas.bbox("all")))

        self.inner_frame = tk.Frame(self.task_canvas, bg="#f0f0f0")
        self.task_canvas.create_window((0, 0), window=self.inner_frame, anchor="nw")

    def update_task_list(self, tasks):
        for widget in self.inner_frame.winfo_children():
            widget.destroy()

        for i, task in enumerate(tasks):
            task_color = random.choice(self.colors)
            task_frame = tk.Frame(self.inner_frame, bg=task_color, padx=10, pady=5)
            task_frame.pack(fill=tk.X, padx=5, pady=5)

            check_var = tk.BooleanVar(value=task.completed)
            checkbox = ttk.Checkbutton(task_frame, variable=check_var, command=lambda idx=i: self.controller.toggle_task(idx), style="TCheckbutton")
            checkbox.pack(side=tk.LEFT)

            task_label = tk.Label(task_frame, text=task.task, font=("Arial", 12), bg=task_color, fg="#ffffff")
            task_label.pack(side=tk.LEFT, padx=5)

            delete_button = ttk.Button(task_frame, text="Delete", command=lambda idx=i: self.controller.remove_task(idx), style="Delete.TButton")
            delete_button.pack(side=tk.RIGHT)

            self.animate_task_entry(task_frame)

    def animate_task_entry(self, widget):
        start_y = self.winfo_height()
        end_y = widget.winfo_y()
        duration = 500  # Animation duration in milliseconds
        steps = 20

        def animate_step(step):
            if step < steps:
                y = start_y - (start_y - end_y) * step / steps
                widget.place(y=y)
                self.after(duration // steps, animate_step, step + 1)
            else:
                widget.place_forget()
                widget.pack(fill=tk.X, padx=5, pady=5)

        widget.place(y=start_y)
        animate_step(0)

    def get_task_input(self):
        return self.task_entry.get()

    def clear_task_input(self):
        self.task_entry.delete(0, tk.END)

    def show_error(self, message):
        tk.messagebox.showerror("Error", message)
