#This is a to-do application with many features such as:
# Add new Tasks ✅
# View lists of tasks ✅
# Mark tasks as completed ✅
# Delete tasks ✅
# Edit tasks ✅
# Show counts: total, remaining, completed ✅
# Clear all / clear completed tasks ✅
# Save tasks in localStorage so they persist after refresh 🫸

print("Welcome to your To-do list!")
print("\n Create new task - 1")
print(" View existing tasks list - 2")
print(" Delete task - 3")
print(" Edit task - 4")
print(" Mark a task completed - 5")
print(" Delete completed tasks - 6")
print(" Delete all tasks - 7")

tasks = []
a=1

def show_tasks():
    print(f"Your to-do list: \n")
    completed = 0
    for i in range(len(tasks)):
        if "Completed" in tasks[i]:
            completed += 1
        print(f"{i}. {tasks[i]}")
    print(f"Number of completed tasks - {completed}")
    print(f"Total tasks - {len(tasks)}")
    print(f"Tasks remaining - {len(tasks) - completed}")

while a>0:
    cmd = int(input("---> "))
    if cmd<1 or cmd > 7:
        print("Perhaps the function you're trying to access is not yet supported by this application, try again!")
    if cmd == 1:
        new_task = input("Enter new task:")
        tasks.append(new_task)
    elif cmd == 2:
        show_tasks()
    elif cmd == 3:
        show_tasks()
        s_no = int(input("Enter the serial number of the task you want to delete: "))
        if s_no < 0 or s_no > len(tasks)-1:
            print("Task doesn't exist!")
        else:
            del(tasks[s_no])
            print("Task has been deleted!, Your new list is as follows:")

        show_tasks()
    elif cmd == 4:
        show_tasks()
        s_no = int(input("Enter the serial number of the task that you want to edit:"))
        if s_no < 0 or s_no > len(tasks)-1:
            print("Task doesn't exist!")
        else:
            edited_task = input("Enter the edited task: ")
            tasks[s_no] = edited_task
        print("Your new list is as follows:")
        show_tasks()
    elif cmd == 5:
        s_no = int(input("Enter the serial number of the task that you want to mark completed:"))
        if s_no < 0 or s_no > len(tasks)-1:
            print("Task doesn't exist!")
        else:
            tasks[s_no] += " (Completed)"
            print("Task marked completed!")
    elif cmd == 6:
        completed = 0
        for i in range(len(tasks)-1,-1,-1):
            if "Completed" in tasks[i]:
                del(tasks[i])
        print("Deleted all completed tasks!")
    elif cmd == 7:
        for i in range(len(tasks)-1,-1,-1):
            del(tasks[i])
    else:
        print("Perhaps the function you're trying to access is not yet supported by this application, try again!")