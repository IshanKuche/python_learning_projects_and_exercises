
stack = []

def stack_operation(operation):
    match operation:
        case "1": store = push_operation()
        case "2": store = pop_operation()
        case "3": store = quit_operation()
        case _: store = "Invalid Choice"
    return store    

def quit_operation():
    return "Thank you for using stack simulator"   

def push_operation():
    n = user_input("Enter what you want to push: ")
    stack.append(n)
    return stack

def pop_operation():
    if not stack:
        return "stack is empty"
    pop_value = stack.pop()
    return pop_value,stack

def user_input(prompt):
    while True:
          value = input(prompt)

          if not value:
              continue
          return value
        
def operation_list():
    print("1. Push")
    print("2. Pop")
    print("3. Quit")

operation_list()       
user_operation = user_input("Enter which Operation to perform: ")
op = stack_operation(user_operation)
print(op)



