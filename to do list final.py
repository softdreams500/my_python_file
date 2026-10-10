tasks = []
while True:
    choice =input("choose: add / remove / view / exit: ")
    if choice == "add":
        new_task = input("add new task: ")
        tasks.append(new_task)
        print("task added")
    elif choice == "remove":
        removed_task = input("type task to remove: ")
        if removed_task in tasks:
            tasks.remove(removed_task)
            print("task removed")
        else:
            print("task not found")
    elif choice == "view":
        print(tasks)
    elif choice in ("exit", "exist"):
        break
    else:
        print("please enter a valid choice")
