task = []

def user_prompt(prompt):
    while True:
        value = input(prompt)
        if value.strip():
            return value
        return "invalid input"

def display_options():
    print("WELCOME TO TASK MANAGER")
    print("1. Add task")
    print("2. View task")
    print("3. Mark task as done")
    print("4. Quit")

def get_choice():
    while True:
        choice = user_prompt("Enter you choice: ")
        if choice.strip():         
            return choice
        else:
            continue
        

def task_manager(task):
    match task:
        case "1": result = add_task()
        case "2": result = view_task()
        case "3": result = mark_task()
        case "4": result = quit_manager()
        case _: result = "Invalid Choice"
    return result    
    
def add_task():
    while True:
        user_task = user_prompt("Enter your task(Q to quit): ")
        if user_task == "q":
            break
        task.append(user_task)
    return task
    

def view_task():
    if task:
        return task
    else:
        return "There is currently no task"
    
def check_empty_task():
    if not task:
        return "no task available"
    
def mark_task():
    if check_empty_task():
        return "empty"
    print(view_task())
    while True:
        task_number = user_prompt("Which task is done/want to remove(q to quit): ")
        if task_number == "q":
            break
        task_number = int(task_number)
        task_number -= len(task)
        task.pop(task_number)
    return task    

def quit_manager():
    message = "THANK YOU FOR USING TASK MANAGER"
    return message
    
def main():
    while True:
        display_options()
        user_choice = get_choice()
        task_response = task_manager(user_choice)
        print(task_response)
        if user_choice == "4":
            break

if __name__ == "__main__":
    main()
