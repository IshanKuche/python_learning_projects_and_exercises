import statistics

user_list = []
def calculate_mean(N):
       return statistics.mean(N)

def calculate_median(N):
    return statistics.median(N)

def calculate_mode(N):
    return statistics.mode(N)


def enter_list():
    while True:
        user_input = input("Enter a number in list(Q to quit): ")
        if user_input in "Qq":
            return user_list
        user_input = float(user_input) 
        user_list.append(user_input)
        
        

calculation_data = enter_list()   
result1 = calculate_mean(calculation_data)
result2 = calculate_median(calculation_data)
result3 = calculate_mode(calculation_data)
print(f"Mean is: {result1:.2f} ,Median is: {result2:.2f} ,Mode is: {result3:.2f}")        