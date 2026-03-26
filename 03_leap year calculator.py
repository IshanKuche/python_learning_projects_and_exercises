user_year = int(input("Enter an Year: "))
if (user_year%4 == 0 and user_year%100 != 0) or (user_year % 400 == 0):
    print(f"{user_year} is a leap year!")
else:
    print(f"{user_year} is not a leap year.")
    