import json
from Tasks import Task

class Todo:
    def __init__(self, file = "todos.json"):
        self.file = file
        self.tasks = []

        
    # saving tasks on a json file
    def save_task(self):
        with open(self.file, "w") as f:
            json.dump([Task.to_dict()], f, indent=4)


    # --- CRUD operations ---
    
    # Adds tasks
    def add_to_do(self, title):
        new_id = 1 if not self.tasks else self.tasks[-1].id + 1
        task = Task(new_id, title)
        self.tasks.append(task)
        
    # Returns all tasks
    def view_to_do(self):
        return self.tasks
    
    # Changes the title and completion status
    def update_to_do(self,change_id, new_title= None, new_status=None):
        change_task = self.tasks[change_id - 1] 

        if not change_task:
            return False

        if new_title is not None:
            change_task.title = new_title
        if new_status is not None:
            change_task.status = new_status

        self.save_task()
        return True

    # Delete task
    def delete_to_do(self, delete_id):
        delete_task = self.tasks[delete_id - 1]
        
        if not delete_task:
            return False
        
        self.tasks.remove(delete_task)
        self.save_task()

        return True


    