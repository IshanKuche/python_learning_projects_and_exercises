def display_schedule(schedule):
    for day, subjects in enumerate(schedule, start=1):
        print(f"Day {day}:")
        for subject in subjects:
            print(f"  - {subject}")

def validate_days_and_slot():
    while True:
        try:
            change = input("Enter day(1-3) and slot(1-3) to change: ").strip().split()
            if len(change) == 2 and (1<=int(change[0])<=3) and (1<=int(change[1])<=3):
                return int(change[0]),int(change[1])
            else:
                print("Invalid input")   
        except (ValueError,AttributeError):
            print("ERROR: Invalid Input")

def display_change(day,slot,schedule,sub):
    schedule[day-1][slot-1] = sub
    display_schedule(schedule)


def change_subject():
    while True:
        sub = input("Enter a subject to change: ").strip()
        if sub:
            return sub
        print("Subject cannot be empty.")

def main():
    schedule = [["Maths","English","Science"],["Programming","Drawing","Maths"],["Sports","Science","English"]]
    display_schedule(schedule)
    day,slot = validate_days_and_slot()
    sub = change_subject()
    display_change(day,slot,schedule,sub)


if __name__ == "__main__":
    main()