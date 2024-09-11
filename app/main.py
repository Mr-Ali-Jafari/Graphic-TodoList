from model import TodoList
from view import TodoView
from controller import TodoController
import tkinter as tk

def main():
    todo_list = TodoList()
    controller = TodoController(todo_list)
    view = TodoView(controller)
    
    
    controller.set_view(view)
    view.mainloop()

if __name__ == "__main__":
    main()
