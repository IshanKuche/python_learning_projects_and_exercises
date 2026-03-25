def get_user_input(prompt):
    return input(prompt)


def create_my_list(my_list):
    while True:
        value = get_user_input("Enter a number to append in list(q to quit): ")

        if value.lower() == "q":
            return my_list
        try:
            value = int(value)
            
        except (ValueError,TypeError) as e:
            print("Invalid input in list")
            print(f"Error: {e}")
        else:    
            my_list.append(value)
            

def take_my_list(my_list):
        if my_list:
            return count_items(my_list),get_average(my_list),get_max(my_list),get_min(my_list)
        else:
            return None   
    
def formatting_result(count_num,avg_num,max_num,min_num):
    print(f"In your list total count of number is {count_num},Average value of list is {avg_num:.2f},Highest number is {max_num} and Lowest number is {min_num}")     
      

def count_items(my_list):
    return len(my_list)

def get_average(my_list):
    return sum(my_list)/len(my_list)


def get_max(my_list):
    return max(my_list)

def get_min(my_list):
    return min(my_list)

def main():
    my_list = []
    create_my_list(my_list)
    result = take_my_list(my_list)
    if result is None:
        print("List is empty") 
        return
    count_num,avg_num,max_num,min_num = result
    formatting_result(count_num,avg_num,max_num,min_num)

if __name__ == "__main__":
    main()    