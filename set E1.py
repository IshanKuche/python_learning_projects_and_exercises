def get_words():
    while True:
        words = input("Enter 8 words (duplicates are recommended not necessary): ").split()
        if len(words) == 8:
            return words
        
def list_to_set(list_store):
    return set(list_store)        

def removed_duplicates(og_list,og_set):
    return len(og_list) - len(og_set)

def main():
    words_8 = get_words()
    set_store = list_to_set(words_8)
    duplicates = removed_duplicates(words_8,set_store)
    print(f"Total {duplicates} duplicates were removed.")

if __name__ == "__main__":
    main()