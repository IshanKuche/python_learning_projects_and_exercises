user_score = int(input("Enter your score: "))
if user_score >= 90:
    print(f"you got 'A+' grade at {user_score} marks.")
elif 89 >= user_score >= 80:
    print(f"you got 'A' grade at {user_score} marks.")
elif 79 >= user_score >= 70:
    print(f"you got 'B+' grade at {user_score} marks.")
elif 69 >= user_score >= 60:
    print(f"you got 'B' grade at {user_score} marks.")
elif 59 >= user_score >= 50:
    print(f"you got 'C' grade at {user_score} marks.")
elif 49 >= user_score >= 36:
    print(f"you got 'D' grade at {user_score} marks.") 
else:
    print(f"you FAILED at {user_score} marks.")
        