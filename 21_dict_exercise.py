menu = {"mango": 50, "orange": 90, "apple": 230, "grapes":58}
cart = {}
bill_list = {}
for fruit,price in menu.items():
    print(f"{fruit}: ${price}/Kg")

while True:
    item = input("Enter what you want to buy(d for done): ").strip()
    if not item:
        print("please enter a item")
        continue
    if item.lower() == "d":
        break
    if menu.get(item):
        quantity = int(input("How much you want: "))
        cart[item] = quantity
        bill = menu.get(item,None) * quantity
        bill_list[item] = bill


total_bill = 0
for _,val in bill_list.items():
    total_bill += val

print("="*60)
print(f"{'TOTAL BILL':^}")
print("="*60)
print(f"{'ITEM':<10}{'QUANTITY':<10}{'RATE':<12}{'PRICE':<10}")
for fruit, quant in cart.items():
    print(f"{fruit:<10}{quant:<10}${menu[fruit]:<11} ${bill_list[fruit]:<10}")
print("="*60)
print(f"TOTAL BILL: ${total_bill} | THANK YOU FOR VISITING US")
print("="*60)


