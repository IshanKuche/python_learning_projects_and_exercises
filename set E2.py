def get_help(valid_command):
    for i,command in enumerate(valid_command,start=1):
        print(f"{i}. {command}")

def quit_action():
    print("=-"*20)
    print("THANK YOU FOR USING COMMAND VALIDATOR")
            

def get_command():
    return input("Enter a command: ").strip()

def validate_and_perform_command(valid_command,command):
    if command in valid_command:
        print(f"Executing: {command}")
    else:
        print("Unknown command")
    

def main():
    valid_command = {"add", "remove", "view", "help", "quit"}
    while True:
        command = get_command()
        if command.lower() == "help":
            get_help(valid_command)
        elif command.lower() == "quit":
            quit_action()
            return
        else:
            validate_and_perform_command(valid_command,command)
        

if __name__ == "__main__":
    main()