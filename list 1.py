def collect_names(my_list):
    while True:
        name = input("Enter a name(done to quit): ").strip()
        if name.lower() == "done":
            return
        if name:
            my_list.append(name)

def display_name(name_list):
    for i in range(len(name_list)):
        print(f"{i+1}: {name_list[i].title()}")            

def main():
    name_list = []
    collect_names(name_list)
    if not name_list:
        print("There is no names in list")
        return    
    display_name(name_list)

if __name__ == "__main__":
    main()