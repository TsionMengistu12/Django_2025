class Task:
    
    def __init__(self, task_id, title, completed=False):
        self.id = task_id
        self.title = title
        self.completed = completed


    # serialization convert task into dictionary for JSON
    def to_dict(self):
        
        return {
            "id": self.id,
            "title": self.title,
            "completed": self.completed
        }
    
    # deserialization convert task from dictionary to task object
    def from_dict(data):

        return Task(
            task_id= data["id"],
            title= data["title"],
            completed= data["completed"]
                    )



    