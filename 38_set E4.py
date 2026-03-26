
def display_options():
    print("1. Add Tag")
    print("2. Remove Tag")
    print("3. View all Tags")

def get_option():
    while True:
        option = input("Enter a option(q to quit): ")
        if option in "123qQ":
            return option
        else:
            print("Invalid Option")
        

def display_all_tags(default_tags):
    for tag in default_tags:
        print(f"$$${tag}$$$")

def add_tag(tags):
        tag = input("Enter a tag: ").strip()
        if tag:
            tags.add(tag.title())
        else:
            print("Please enter a tag.")    

def remove_tag(tags):
    tag = input("Enter a tag to remove: ").strip()
    tag = tag.title()
    if tag in tags:
        tags.discard(tag)
    else:
        print(f"{tag} does not exist in tag list.")             

def main():
    default_tags = {"Founder","Executive","Admin","captain","Member"}
    while True:
        display_options()
        option = get_option()
        if option == "1":
            add_tag(default_tags)
        if option == "2":
            remove_tag(default_tags)
        if option == "3":
            display_all_tags(default_tags)
        if option.lower() == "q":
            display_all_tags(default_tags)
            return    

if __name__ == "__main__":
    main()