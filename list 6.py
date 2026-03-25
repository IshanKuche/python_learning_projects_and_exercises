def display_task(tasks):
    for serial,task in enumerate(tasks):
        print(f"{serial+1}: {task}")    

def pick_task_number(task):
    while True: 
        number = input("Enter a number: ").strip()
        try:
            number = int(number)
            return number      
        except ValueError:
            print("ERROR: Invalid input")
        

def show_task_details(num,tasks):
    for serial,task in enumerate(tasks):
        if serial + 1 == num:
            print(f"{serial + 1}: {task}")
    return 
    

def validate_task(num,task):
    try:
        if 0 < num <= len(task):
            return True
        else: 
            raise ValueError("Task serial is not in list")
    except ValueError as e:
        print(f"ERROR: {e}")

def main():
    task = ["eat","bath","sleep","write","drink","dump"]
    display_task(task)
    while True:
        num = pick_task_number(task)
        status = validate_task(num,task)
        if status:
            show_task_details(num,task)
            return
        

if __name__ == "__main__":
    main()