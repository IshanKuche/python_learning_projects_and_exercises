def get_user_response(prompt):
    while True:
        name = input(prompt).strip()
        if name:
            return name
        else:
            print("Try Again!!!")

def store_data(friend_info,name,color):
        friend_info[name] = color

def print_info(friend_info):
    for name,color in friend_info.items():
         print(f"{name.title()} Favourite color is {color}.")
    

def main():
    friend_info = {}

    while(len(friend_info)<3):
        friend_name = get_user_response("Enter your friend name: ")
        fav_color = get_user_response("Enter your favourite color: ")
        store_data(friend_info,friend_name,fav_color)

    print_info(friend_info)



if __name__ == "__main__":
    main()