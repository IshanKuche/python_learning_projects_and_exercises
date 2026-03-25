def get_user_num(num_list):
    while True:
        num = input("Enter a num(q to quit): ").strip()
        if num.lower() == "q":
            return 
        try:
            num = int(num) 
        except ValueError as e:
            print(f"Error: {e}")
        else:
            num_list.append(num)    

def sort_list(num_list):
    ascend = sorted(num_list)
    descend = sorted(num_list,reverse=True)
    return ascend,descend

def display_list(og,asc,desc):
    print(f"Original list: {og}")
    print(f"Ascending list: {asc}")
    print(f"Descending list: {desc}")

def main():
    num_list = []
    get_user_num(num_list)
    if not num_list:
        print("List is Empty")
        return
    ascend,descend = sort_list(num_list)
    display_list(num_list,ascend,descend)


if __name__ == "__main__":
    main()    