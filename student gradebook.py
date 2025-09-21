gradebook = {}
while True:
    choice = input("choose:add / view / exist: ")
    if choice == "add":
        name = input("enter name: ")
        grade = input("enter grade: ")
        gradebook[name] = grade
        print(f"student added {name} with grade {grade}")
    elif choice == "view":
        name = input("Enter student name to view: ")
        if name in gradebook:
            print(f"{name} grade is {gradebook[name]}")
        else:
            print("Student not found!")
    elif choice == "exist":
        break
    else:
        print("please enter a valid choice")



