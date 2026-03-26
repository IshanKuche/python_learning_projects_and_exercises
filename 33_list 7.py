def get_score(scores):
    while True:
        score = input("enter your scores(q to quit): ").strip()
        if score.lower() == "q":
            return scores
        try:
            score = int(score)
        except ValueError:
            print("Error: Invalid score")   
        else: 
            scores.append(score)
        finally:
            print("score added!!!") 

def get_top_3_scores(marks):
    marks.sort(reverse = True)
    return marks[:3]

def main():
    scores = []
    get_score(scores)
    scores_copy = scores.copy()
    top_3 = get_top_3_scores(scores_copy)
    print(scores)
    print(scores_copy)
    print(top_3)

if __name__ == "__main__":
    main()