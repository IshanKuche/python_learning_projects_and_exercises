def get_sentence():
    sentence = input("Enter a sentence: ").split()
    return sentence

def get_first_3_characters(sentence):
    return sentence[:3]

def get_last_3_characters(sentence):
    return sentence[-3:]

def get_second_word(sentence):
    return sentence[::2]

def reverse_word(sentence):
    return sentence[::-1]

def display_result(og,first,last,alternate,reverse):
    print(f"Original sentence: {" ".join(og)}")
    print(f"First three words in sentence: {" ".join(first)}")
    print(f"last three words in sentence: {" ".join(last)}")
    print(f"every second words in sentence: {" ".join(alternate)}")
    print(f"reverse of original sentence: {" ".join(reverse)}")

def main():
    store = get_sentence()
    first_3 = get_first_3_characters(store)
    last_3 = get_last_3_characters(store)
    alternate_words = get_second_word(store)
    reverse_sentence = reverse_word(store)
    display_result(store,first_3,last_3,alternate_words,reverse_sentence)

if __name__ == "__main__":
    main()    