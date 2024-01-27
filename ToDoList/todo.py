class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False, "in_progress":False})
        print(f"Task '{task}' added to the to-do list.")

    def view_tasks(self):
        if not self.tasks:
            print("Your to-do list is empty.")
        else:
            print("To-Do List:")
            for index, task in enumerate(self.tasks, start=1):
                if task["completed"]:
                   status = "Done" 
                elif task["in_progress"]:
                    status = "In progress"
                else:
                    status = "Not Started"

                print(f"{index}. {task['task']} - {status}")

    def mark_completed(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            task = self.tasks[task_index - 1]
            task["completed"] = True
            print(f"Task '{task['task']}' marked as completed.")
        else:
            print("Invalid task index.")

    def start_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            task = self.tasks[task_index - 1]
            task["in_progress"]= True
            print(f"Task '{task['task']}' started")
        else:
            print("Invalid task index")

    def delete_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            deleted_task = self.tasks.pop(task_index - 1)
            print(f"Task '{deleted_task['task']}' deleted.")
        else:
            print("Invalid task index.")

def main():
    todo_list = TodoList()

    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Start a Task")
        print("4. Mark a Task as Completed")
        print("5. Delete Task")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == "2":
            todo_list.view_tasks()
        elif choice == "3":
            todo_list.view_tasks()
            task_index = int(input("Enter the task index to mark as completed: "))
            todo_list.start_task(task_index)
        elif choice == "4":
            todo_list.view_tasks()
            task_index = int(input("Enter the task index to delete: "))
            todo_list.mark_completed(task_index)
        elif choice == "5":
            todo_list.view_tasks()
            task_index = int(input("Enter the task index to delete: "))
            todo_list.delete_task(task_index)
        elif choice == "6":
            print("Exiting the To-Do List Application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
