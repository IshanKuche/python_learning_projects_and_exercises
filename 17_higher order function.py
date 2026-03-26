def get_prompt(prompt):
    return input(prompt)

def apply_operation(operation,operand_1,operand_2):
     operand_1 = float(operand_1)
     operand_2 = float(operand_2)
     operation_result = operation(operand_1,operand_2)
     return operation_result

def do_operation(operator):
    operation_menu = {
            "+": addition,
            "-": subtraction,
            "*": multiplication,
            "/": division
        }
    if operator in operation_menu:
        operation = operation_menu[operator]
        return operation 
           
addition = lambda a,b : a + b
subtraction = lambda a,b : a - b
multiplication = lambda a,b : a * b
division = lambda a,b : a / b

operand_1 = get_prompt("Enter a number: ")
operator =  get_prompt("Enter a Operator: ")
operand_2 = get_prompt("Enter another number: ")
operation_op = do_operation(operator)
result = apply_operation(operation_op,operand_1,operand_2)
print(result)

