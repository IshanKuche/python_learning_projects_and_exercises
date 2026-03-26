operand_1 = float(input("Enter a number: "))
operator = input("Enter a operator to perform calculation: ")
operand_2 = float(input("Enter another number: "))

match operator:
    case "+":
        print(f"{operand_1} + {operand_2} is {operand_1 + operand_2:.2f}")
    case "-":
        print(f"{operand_1} - {operand_2} is {operand_1 - operand_2:.2f}")
    case "*":
        print(f"{operand_1} * {operand_2} is {operand_1 * operand_2:.2f}")
    case "/":
        if operand_2 == 0:
            print("Cannot divide by 0")
        else:
            print(f"{operand_1} / {operand_2} is {operand_1 / operand_2:.2f}")   
    case _:             
        print(f"{operator} is invalid!")