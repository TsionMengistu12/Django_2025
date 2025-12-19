import json
import os

try:
    from Tasks import Task
except ImportError:
    # Allow importing when miniproject is treated as a package
    from .Tasks import Task


class Todo:
    def __init__(self, file="todos.json"):
        self.file = file
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        if not os.path.exists(self.file):
            self.tasks = []
            return

        if os.path.getsize(self.file) == 0:
            self.tasks = []
            return

        try:
            with open(self.file, "r") as f:
                data = json.load(f)
        except json.JSONDecodeError:
            # Treat malformed JSON as empty to avoid crashing the app
            self.tasks = []
            return

        self.tasks = [Task.from_dict(item) for item in data]


    # saving tasks on a json file
    def save_task(self):
        with open(self.file, "w") as f:
            json.dump([t.to_dict() for t in self.tasks], f, indent=4)

    # --- CRUD operations ---
    
    # Adds tasks
    def add_to_do(self, title):
        new_id = 1 if not self.tasks else self.tasks[-1].id + 1
        task = Task(new_id, title)
        self.tasks.append(task)
        
    # Returns all tasks
    def view_to_do(self):
        return self.tasks

    def update_to_do(self, change_id, new_title=None, new_status=None):
        change_task = self._find_task(change_id)
        if not change_task:
            return False

        if new_title is not None:
            change_task.title = new_title
        if new_status is not None:
            change_task.completed = new_status

        self.save_task()
        return True

    def delete_to_do(self, delete_id):
        for idx, task in enumerate(self.tasks):
            if task.id == delete_id:
                self.tasks.pop(idx)
                self.save_task()
                return True
        return False

    def _find_task(self, task_id):
        return next((task for task in self.tasks if task.id == task_id), None)


    