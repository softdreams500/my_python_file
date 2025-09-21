tasks = []
while True:
    choice =input("choose: add / remove / view /exist: ")
    if choice == "add":
        new_task = input("add new task: ")
        tasks.append(new_task)
        print("task added")
    elif choice == "remove":
        removed_task = input("type task to remove: ")
        tasks.remove(removed_task)
        print("task removed")
    elif choice == "view":
        print(tasks)
    elif choice == "exist":
        break
    else:
        print("please enter a valid choice")
