from Todo import Todo

def display_menu():
    print("""\n TODO APP
          \n 1. Add Todo
          \n 2. View Todos
          \n 3. update Todo
          \n 4. Delete Todo
          \n 5. Exit""")
    
def main():
    manager = Todo()

    while True:
        display_menu()
        choice = int(input("Choose an option: "))

        if choice == 1:
            title = input("Enter the task: ")
            manager.add_to_do(title)
            print("Task added successfully. ")

        elif choice == 2:
            tasks = manager.view_to_do()

            if not tasks:
                print("No tasks found. ")
            
            for task in tasks:
                status = "completed" if task.completed else "Not completed"
                print(f"{task.id}. {task.title} [{status}]")

        elif choice == 3:
            task_id = int(input("Enter task ID: "))
            new_title = input("New title: ")
            completed_input = input("Mark completed? (y/n/skip): ")

            completed = None
            if completed_input.lower() == "y":
                completed = True
            elif completed_input.lower() == "n":
                completed = False

            updated = manager.update_to_do( 
                                task_id, 
                                new_title if new_title else None,
                                completed)
            print(" Task updated" if updated else "Task not found ")

        elif choice == 4:
            task_id = int(input("Enter task ID to delete: "))
            deleted = manager.delete_to_do(task_id)
            print(" Task successfully deleted " if deleted else " Task not found")

        elif choice == 5:
            print("Good BYE!!!")
            break

        else:
            print("invalid option")
