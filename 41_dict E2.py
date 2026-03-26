def get_user_response(prompt):
    while True:
        name = input(prompt).strip()
        if name:
            return name
        else:
            print("Try Again!!!")

def check_for_country(data,country):
    return data.get(country)
    
def give_info(country,capital):
    if capital:
        print(f"capital of {country} is {capital}")
    else:
        print("Country not found")


def main():
    country_capitals = {"India":"New delhi", "Japan":"Tokyo","England":"London", "USA":"Washington dc", "Russia":"Moscow"}
    country = get_user_response("Enter a country name: ").title()
    capital = check_for_country(country_capitals,country)       
    give_info(country,capital)


if __name__ == "__main__":
    main()