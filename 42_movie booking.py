def main_menu():
    print("1.Available Movies")
    print("2.Time Slots")
    print("3.Seat arrangement")
    print("4.Show Ticket Prices")
    print("5.Book Tickets")
    print("6.Exit")

def choose_options():
    option = user_prompt("Enter your options: ")  
    return option

def show_movies(data):
    for name,info in data.items():
        for price,time in info.items():
            print(f"{name:<10}| ticket price: {price} available slots: {time[0]}, {time[1]}, {time[2]} PM")
             
def select_time_slot(data):
    for name,info in data.items():
       for _,time in info.items():
           print(f"Available Time Slots for {name}:{time[0]}PM,{time[1]}PM, {time[2]}PM")          
    
def Book_tickets():
    pass

def show_seat_arrangements():
    pass

def user_prompt(prompt):
    while True:
        value = input(prompt)
        if value.strip():
            return value
        return "invalid input"


def exit_booking():
    print("="*100)
    print("THANK YOU FOR USING OUR BOOKING SYSTEM")
    print("="*100)



def main():
    seats=[["A1","A2","A3","A4","A5"],
           ["B1","B2","B3","B4","B5"],
           ["C1","C2","C3","C4","C5"],
           ["D1","D2","D3","D4","D5"],
           ["E1","E2","E3","E4","E5"]
        ]
    
    movie_info={"Dhurandar":{"$200":["7","8","12"]},
                "avengers":{"$800":["6","4","10"]},
                "bokunopico":{"$670":["6","7","9"]}
                }
    main_menu()
    option = choose_options()
    show_movies(movie_info)
    select_time_slot(movie_info)

if __name__  == "__main__":
    main()