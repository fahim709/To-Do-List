def main():
    tasks = []

    while True:
        print('\n...To Do List...')
        print('1. Add task')
        print('2. Delete task')
        print('3. View tasks')
        print('4. Exit')

        choice = input("Enter your choice: ")

        if choice == '1':
            try:
                num_tasks = int(input('How many tasks do you want to add? '))
                for i in range(num_tasks):
                    task = input(f'Enter task {i + 1}: ')
                    tasks.append({"task": task, "done": False})
                    print("Task added.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == '2':
            print("\nCurrent Tasks:")
            for index, task in enumerate(tasks):
                print(f"{index + 1}. {task['task']}")

            try:
                task_num = int(input('Enter the number of the task you want to delete: '))
                if 1 <= task_num <= len(tasks):
                    removed = tasks.pop(task_num - 1)
                    print(f"Task '{removed['task']}' deleted.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == '3':
            if not tasks:
                print("No tasks available.")
            else:
                print("\nTasks:")
                for index, task in enumerate(tasks):
                    print(f"{index + 1}. {task['task']}")

        elif choice == '4':
            print("Exiting the To Do List.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

