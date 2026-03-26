def grand_total(total):
    grand_sum = sum(price[1] for price in total)
    return grand_sum

def list_calculation(input_list):
    total = []
    for prod,price,quant in input_list:
        total_price = price*quant
        total.append((prod,total_price))
    return total     
    
def formatted_table(list,price):
    print("="*60)
    print("TOTAL BILL")
    print("="*60)
    print(f"{'Item':<12} {'rate':<8} {'quantity':<12} {'price':<8}")
    print("="*60)
    for item,rate,quant in list:
        print(f"{item:<12} {rate:<10} {quant:<10} {rate*quant:<8}")
    print("="*60)
    print(f"TOTAL PRICE : {price}")
    print("="*60)


def main():
    shop_list = [("laptop",50000,1),("4K Monitor",35000,2),("mouse",1500,4),("headphones",500,9),("keyboard",2500,5)]
    total = list_calculation(shop_list)
    final_price = grand_total(total)
    formatted_table(shop_list,final_price)

if __name__ == "__main__":
    main()    