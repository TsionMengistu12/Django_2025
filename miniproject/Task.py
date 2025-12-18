class Task:
    # 
    def __init__(self, tasks, task_id, title, completed=False):
        self.tasks = []
        self.id = task_id
        self.title = title
        self.completed = completed

    # Adds tasks
    def add_to_do(self, id, name, status):
        self.task.append(id)
        self.task.append(name)
        self.task.append(status)

    # Returns all tasks
    def view_to_do(self):
        return self.task
    
    # Changes the title and completion status
    def update_to_do(self,change_id, new_name, new_status):
        self.task[change_id] = str(new_name), new_status

    # Delete task
    def delete_to_do(self, delete_id):
        if str(delete_id) in self.task:
            del self.task[str(delete_id)]

