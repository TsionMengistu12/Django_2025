class Task:
    # 
    def __init__(self, task):
        self.task = []

    #Adding tasks
    def add_to_do(self, id, name, status):
        self.task.append(id)
        self.task.append(name)
        self.task.append(status)

    # returns all tasks
    def view_to_do(self):
        return self.task
    
    # changes the title and completion status
    def update_to_do(self,change_id, new_name, new_status):
        self.task[change_id] = str(new_name), new_status

    # delete task
    def delete_to_do(self, delete_id):
        self.task[delete_id]

