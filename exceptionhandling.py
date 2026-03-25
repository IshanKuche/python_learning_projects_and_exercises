def safe_calculator():
    while True:
        try:
            num1 = float(input("Enter first number (or 'quit'): "))
            num2 = float(input("Enter second number: "))
            operation = input("Operation (+, -, *, /): ")
            
            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                result = num1 / num2
            else:
                raise ValueError("Invalid operation")
                
        except ValueError as e:
            if "could not convert" in str(e):
                print("Please enter valid numbers!")
            else:
                print(f"Error: {e}")
        except ZeroDivisionError:
            print("Cannot divide by zero!")
        else:
            print(f"Result: {result}")
        finally:
            print("-" * 30)

safe_calculator()            