import random
comp_num = random.randint(1,100)
count = 0
while True:
    user_num = int(input("Guess a number: "))
    count += 1 
    if user_num == comp_num:
       print(f"NUMBER FOUND!!! You took {count} guesses")
       break
    elif user_num != comp_num and user_num > comp_num:
        print("Your number is greater")
    elif user_num != comp_num and user_num < comp_num:
        print("Your number is smaller")
    else:
        print("Invalid Input")

