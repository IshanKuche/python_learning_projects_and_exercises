def get_sentence():
    while True:
        sentence = input("Enter a Sentence: ").lower().split()
        if sentence:
            sentence = set(sentence)
            return sentence

def check_common_words(sen_1,sen_2):
    return sen_1 & sen_2

def unique_words(sen_1,sen_2):
    s1_unique = sen_1 - sen_2
    s2_unique = sen_2 - sen_1
    return s1_unique,s2_unique

def main():
    sentence_1 = get_sentence()
    sentence_2 = get_sentence()
    print(f"Common words in Sentence 1 and Sentence 2 is/are : {", ".join(check_common_words(sentence_1,sentence_2))}")
    s1_unique,s2_unique = unique_words(sentence_1,sentence_2)
    print(f"Unique words in Sentence 1 is/are : {", ".join(s1_unique)}")
    print(f"Unique words in Sentence 2 is/are : {", ".join(s2_unique)}")      

if __name__ == "__main__":
    main()