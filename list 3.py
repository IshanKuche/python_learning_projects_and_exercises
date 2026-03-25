def main():
    banned_users = ["max","alice","joe","ian","brom"]
    unban = remove_ban()
    conclusion = check_user(unban,banned_users)
    display_users(conclusion,banned_users) 

def display_users(unban,ban):
    print(unban)
    print("="*60)
    print("BANNED USERS")
    for user in ban:
        print(user,end=", ")    

def remove_ban():
    unban = input("Enter a username to unban: ").strip()
    return unban

def check_user(unban,banned_users):
    if unban in banned_users:
        banned_users.remove(unban)
        return f"{unban} removed from banned user"
    else:
        return f"{unban} doesn't exist"

if __name__ == "__main__":
    main()        