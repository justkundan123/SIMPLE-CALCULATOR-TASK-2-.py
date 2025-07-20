import json

class TodoList:
    def __init__(self, filename='todo_list.json'):
        self.filename = filename
        self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.filename, 'r') as file:
                self.tasks = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.tasks = []

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file)

    def add_task(self, task):
        self.tasks.append({'task': task, 'completed': False})
        self.save_tasks()
        print(f'Task "{task}" added.')

    def update_task(self, task_index, new_task):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]['task'] = new_task
            self.save_tasks()
            print(f'Task updated to "{new_task}".')
        else:
            print("Invalid task index.")

    def complete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]['completed'] = True
            self.save_tasks()
            print(f'Task "{self.tasks[task_index]["task"]}" marked as completed.')
        else:
            print("Invalid task index.")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        for index, task in enumerate(self.tasks):
            status = "✔️" if task['completed'] else "❌"
            print(f"{index + 1}. [{status}] {task['task']}")

def main():
    todo_list = TodoList()
    
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. Update Task")
        print("3. Complete Task")
        print("4. List Tasks")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")
        
        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.list_tasks()
            task_index = int(input("Enter the task number to update: ")) - 1
            new_task = input("Enter the new task: ")
            todo_list.update_task(task_index, new_task)
        elif choice == '3':
            todo_list.list_tasks()
            task_index = int(input("Enter the task number to complete: ")) - 1
            todo_list.complete_task(task_index)
        elif choice == '4':
            todo_list.list_tasks()
        elif choice == '5':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
