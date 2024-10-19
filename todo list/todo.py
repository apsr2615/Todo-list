def display_menu():
    print("To-Do List Application")
    print("1. view todo list")
    print("2. add task")
    print("3. remove task")
    print("4. exit")

def view_tasks(tasks):
    if not tasks:
        print("todo list is empty")
    else:
        print("your tasks")
        for i,tasks in enumerate(tasks,start=1):
             print(f"{i}.{tasks2}")   

def add_tasks(tasks):
    a=input("enter the task:")
    tasks.append(a)
    print(f"'{tasks}' has been added to ur list")

def rem_tasks(tasks):
    view_tasks(tasks)
    try:
        tsk_num=int(input("enter the number of the task to remove:"))
        if 1<=tsk_num<=len(tasks):
            remd_tsk=tasks.pop(tsk_num-1)
            print(f"'{remd_tsk}' has been remd from the tasks")
        else:
            print("invalid number")
    except ValueError:
        print("enter valid number")

def todo_app():
    tasks=[]
    while True:
        display_menu()
        b=input("choose a number from 1 to 4:")
        if b=='1':
            view_tasks(tasks)
        elif b=='2':
            add_tasks(tasks)
        elif b=='3':
            rem_tasks(tasks)
        elif b=='4':
            print("exit the App...good bye!!")
            break
        else:
            print("invalid choice,pls enter a valid option!")    

todo_app()         


