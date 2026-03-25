import string


def reverse_string(string):
    """
    Docstring for reverse_string
    
    :param string: Takes a string as parameter and returns a reversed string
    """
    return string[::-1]


def is_palindrome(string):
    """
    Docstring for is_palindrome
    
    :param string: Takes string as parameter and returns if the string is palindrome or not with proper print statement
    """
    local_string = string
    first_letter,last_letter = 0, len(local_string)-1
    palindrome = True

    while first_letter < last_letter:
        if local_string[first_letter] != local_string[last_letter]:
            palindrome = False
            break
        first_letter += 1
        last_letter -= 1

    if palindrome:
        return f"{string} is a palindrome"
    else:
        return f"{string} is not a palindrome"        
           


def count_vowels(string):
    """
    Docstring for count_vowels
    
    :param string: Takes input as string and returns total number of vowels in string
    """
    vowels = 0
    for char in string:
        if char in "AEIOUaeiou":
            vowels += 1
    return vowels        

user_string = input("Enter a String: ")
result1 = reverse_string(user_string)
result2 = is_palindrome(user_string)
result3 = count_vowels(user_string)
print(f"Reverse of {user_string} is {result1}, {result2}, it has {result3} vowel/s in it.")