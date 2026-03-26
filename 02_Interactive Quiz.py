question = { "Question_1":("What is captial of India?" ,"Delhi"),
    "Question_2": ("What is currency of India called?" ,"Rupees"),
    "Question_3": ("Which is most popular programming language?" ,"Python"),
    "Question_4": ("Which is richest state of India?" ,"Maharashtra"),
    "Question_5": ("Which is best country in the world?" ,"India")
}

def store_question(question):
    quiz_question = []
    for _,(que,ans) in question.items():
        quiz_question.append(que)
    return quiz_question

def check_answer(question):
    answer = []
    answer_mapping = []
    for qno,(que,ans) in question.items():
        answer_mapping.append((qno,ans))
        answer.append(ans)
    return answer,answer_mapping    

def give_quiz(quiz):
    user_ans = []
    for item in quiz:
        print(item)
        temp_ans = get_prompt("Enter your Answer: ")
        user_ans.append(temp_ans)

    return user_ans    

def get_prompt(prompt):
    return input(prompt)

def check_quiz_answer(answer_of_quiz,answers):
    correct_answer = []
    for user, quiz in zip(answer_of_quiz,answers):
        if user == quiz:
            correct_answer.append((user,quiz))
        else:
            continue
    return correct_answer        
            


quiz = store_question(question)
answer_of_quiz = give_quiz(quiz)
answers,answer_map = check_answer(question)
result_of_quiz = check_quiz_answer(answer_of_quiz,answers)
user_score = len(result_of_quiz)
print(f"You got {user_score}/5.")
print("-"*100)
for _,(que,ans) in question.items():
    print(que)
print("-"*100)   
for ans in answer_map:
    print(f"{ans[0]} -> {ans[1]}")