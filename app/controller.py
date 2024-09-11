class TodoController:
    def __init__(self, model):
        self.model = model
        self.view = None

    def set_view(self, view):
        self.view = view

    def add_task(self):
        task = self.view.get_task_input()
        if task:
            self.model.add_item(task)
            self.view.clear_task_input()
            self.update_view()
        else:
            self.view.show_error("Task cannot be empty!")

    def remove_task(self, index):
        self.model.remove_item(index)
        self.update_view()

    def toggle_task(self, index):
        self.model.toggle_completed(index)
        self.update_view()

    def update_view(self):
        tasks = self.model.get_items()
        self.view.update_task_list(tasks)
