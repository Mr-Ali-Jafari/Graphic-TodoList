class TodoItem:
    def __init__(self, task, completed=False):
        self.task = task
        self.completed = completed

class TodoList:
    def __init__(self):
        self.items = []

    def add_item(self, task):
        self.items.append(TodoItem(task))

    def remove_item(self, index):
        if 0 <= index < len(self.items):
            del self.items[index]

    def toggle_completed(self, index):
        if 0 <= index < len(self.items):
            self.items[index].completed = not self.items[index].completed

    def get_items(self):
        return self.items
