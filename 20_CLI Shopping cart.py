

def add_items(cart):
    item = get_user_input("Enter item and quantity(item quantity): ").split()
    cart.append(item)

def remove_item(cart):
    if not cart:
        print("cart is empty!")
    view_cart(cart)    
    number = get_user_input("Enter which item to remove(by number): ").strip()
    if not number.isdigit():
        return
    number = int(number)
    if number<1 or number>len(cart):
        print("Enter correct number")
    else:
        number = number -1
        cart.pop(number)    

def total_items(cart):
    total_quantity = 0
    for item,quantity in cart:
        item = len(cart)
        quantity = int(quantity)
        total_quantity += quantity
    print(f"Total number of items:{item},total quantity of items:{total_quantity}")       


def view_cart(cart):
    if not cart:
        print("cart is empty!")
    for i,item in enumerate(cart,1):
            print(f"{i}. {item[0]}: {item[1]}")    

def get_user_input(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Invalid")

def quit_shopping():
    print("THANK YOU FOR SHOPPING WITH US") 

def action_list():
    print("1. add item")
    print("2. remove item")
    print("3. view item")
    print("4. see total")
    print("5. quit")
    action = get_user_input("Enter what to do: ")
    return action

def do_shopping(choice,cart):
    if choice == "1":
        add_items(cart)
    elif choice == "2":
        remove_item(cart)
    elif choice == "3":
        view_cart(cart) 
    elif choice == "4":
        total_items(cart)
    elif choice == "5":
        quit_shopping()
    else:
        print("Invalid Choice")    


def main():
    cart = []
    while True:
        action_choice = action_list()
        shopping_cart = do_shopping(action_choice,cart)
        if action_choice == "5":
            break
    if shopping_cart:    
        print(shopping_cart)    

if __name__ == "__main__":
    main()