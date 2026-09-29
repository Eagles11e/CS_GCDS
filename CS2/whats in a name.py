########################################################################
# Name:        Ethan Lisker                                            #
#                                                                      #
# Assignment:  CS2 Functions - What's in a Name?                       #
#                                                                      #
# Description: A set of functions that manipulate and interrogate a    #
#              name or word entered by the user. A menu lets the user  #
#              choose which function to run. No string class methods   #
#              or global variables are used.                           #
#                                                                      #
# Bugs:        - none                                                  #
#                                                                      #
# Bonus:       - #12 Sorted array of characters                        #
#              - #13 Menu                                              #
#              - #15 Title/distinction check                           #
#              - #17 Own function: toggle case                         #
########################################################################

import random

def mylower(text):
    """
    Description: Converts every uppercase letter in a string to lowercase.
    Parameters:  text (str) - the string to convert
    Returns:     (str) a new string with all letters lowercase
    """    
    result = ""
    for char in text:
        if 'A' <= char <= 'Z':
            result = result + chr(ord(char) + 32)
        else:
            result = result + char 
    return result

def myupper(text):
    """
    Description: Converts every lowercase letter in a string to uppercase.
    Parameters:  text (str) - the string to convert
    Returns:     (str) a new string with all letters uppercase
    """
    result = ""
    for char in text:
        if 'a' <= char <= 'z':
            result = result + chr(ord(char) - 32)
        else:
            result = result + char
    return result

def myjoin(item_list, separator):
    """
    Description: Joins the items of a list into one string, placing the
                 separator between items (not after the last one).
    Parameters:  item_list (list) - items to join (converted with str())
                 separator (str)  - text placed between each item
    Returns:     (str) the combined string
    """    
    joined_string = ""
    
    for i in range(len(item_list)):
        joined_string = joined_string + str(item_list[i])
        # Skips the separator after the final item        
        if i < len(item_list) - 1:
            joined_string = joined_string + separator    
    return joined_string

def reverse_then_display(string):
    """
    Description: Reverses a string and displays it.
    Parameters:  string (str) - the text to reverse
    Returns:     nothing (prints the reversed text)
    """
    reversed_str = ""
    for char in string:
        # Putting each new character in front of the result reverses it
        reversed_str = char + reversed_str
    print(reversed_str)


def vowel_counter(userinfo):
    """
    Description: Counts the vowels (a, e, i, o, u) in a string,
                 ignoring case.
    Parameters:  userinfo (str) - the text to check
    Returns:     nothing (prints the vowel count)
    """
    userinfo = mylower(userinfo)   # lowercase so A and a both match
    vowelcounter = 0
    vowels = ("a", "e", "i", "o", "u")

    for char in userinfo:
        if char in vowels:
            vowelcounter += 1
    print(f"There are {vowelcounter} vowels in your name/word(s)")

def consonant_frequency(userinfo):
    """
    Description: Counts the consonants in a string, ignoring case.
                 Spaces, hyphens, digits, and other non-letters are
                 not counted.
    Parameters:  userinfo (str) - the text to check
    Returns:     nothing (prints the consonant count)
    """
    userinfo = mylower(userinfo)
    count = 0
    vowels = ("a", "e", "i", "o", "u")

    for char in userinfo:
        if 'a' <= char <= 'z' and char not in vowels:
            count += 1
    print(f"There are {count} consonants in your name/word(s)")

def get_middle_names(userinfo):
    """
    Description: Finds the middle name(s): every word between the first
                 and last word.
    Parameters:  userinfo (str) - the full name
    Returns:     (str) middle names separated by spaces, or "" if the
                 name has fewer than three words
    """
    words = split_words(userinfo)
    middle = []
    for i in range(1, len(words) - 1):
        middle.append(words[i])
    return myjoin(middle, " ")

def get_first_name(userinfo):
    """
    Description: Extracts the first name (all characters before the
                 first space) and displays it.
    Parameters:  userinfo (str) - the full name
    Returns:     nothing (prints the first name)
    """
    first = []
    for char in userinfo:
        if char == " ":
            break             
        first.append(char)

    print(f"Your first name is: {myjoin(first, '')}")

def scramble_name(userinfo):
    """
    Description: Mixes up the letters of the name. Spaces stay in place.
    Parameters:  userinfo (str) - the full name
    Returns:     (str) the scrambled name
    """
    letters = []
    for char in userinfo:
        if char != " ":
            letters.append(char)

    for i in range(len(letters) - 1, 0, -1):
        j = random.randint(0, i)
        temp = letters[i]
        letters[i] = letters[j]
        letters[j] = temp

    result = ""
    next_letter = 0
    for char in userinfo:
        if char == " ":
            result = result + " "
        else:
            result = result + letters[next_letter]
            next_letter += 1
    return result

def get_last_name(userinfo):
    """
    Description: Extracts the last name (the last word) and displays it.
                 Trailing spaces are ignored.
    Parameters:  userinfo (str) - the full name
    Returns:     nothing (prints the last name)
    """
    last = []
    new_word = False           # True after a space, until a letter appears

    for char in userinfo:
        if char == " ":
            new_word = True
        else:
            if new_word:
                last = []
                new_word = False
            last.append(char)

    print(f"Your last name is: {myjoin(last, '')}")

def check_for_hyphen(userinfo):
    """
    Description: Checks whether the LAST name contains a hyphen.
    Parameters:  userinfo (str) - the full name
    Returns:     (bool) True if the last name has a '-', else False
    """
    words = split_words(userinfo)
    if len(words) == 0:
        return False
    for char in words[len(words) - 1]:
        if char == '-':
            return True
    return False

def split_words(text):
    """
    Description: Splits text into a list of words on spaces. Extra,
                 leading, and trailing spaces are ignored.
    Parameters:  text (str) - the full name
    Returns:     (list) of word strings (empty list if no words)
    """
    words = []
    current = []
    for char in text:
        if char == " ":
            if len(current) > 0:
                words.append(myjoin(current, ""))
                current = []
        else:
            current.append(char)
    if len(current) > 0:
        words.append(myjoin(current, ""))
    return words

def first_name_is_palindrome(userinfo):
    """
    Description: Checks whether the first name reads the same forward
                 and backward, ignoring case.
    Parameters:  userinfo (str) - the full name
    Returns:     (bool) True if the first name is a palindrome
    """
    words = split_words(userinfo)
    if len(words) == 0:
        return False
    first = mylower(words[0])
    left = 0
    right = len(first) - 1
    while left < right:
        if first[left] != first[right]:
            return False
        left += 1
        right -= 1
    return True

def sorted_characters(userinfo):
    """
    Description: Returns the name as a sorted array of characters
                 (spaces removed), ordered by character code.
    Parameters:  userinfo (str) - the full name
    Returns:     (list) of single characters in sorted order
    """
    chars = []
    for char in userinfo:
        if char != " ":
            chars.append(char)

    for i in range(len(chars)):
        smallest = i
        for j in range(i + 1, len(chars)):
            if chars[j] < chars[smallest]:
                smallest = j
        temp = chars[i]
        chars[i] = chars[smallest]
        chars[smallest] = temp
    return chars

def make_initials(userinfo):
    """
    Description: Makes initials (first letter of each word, uppercase,
                 each followed by a period).
    Parameters:  userinfo (str) - the full name
    Returns:     (str) initials such as "E.L."
    """
    initials = ""
    for word in split_words(userinfo):
        initials = initials + myupper(word[0]) + "."
    return initials

def has_title(userinfo):
    """
    Description: Checks whether any word is a title or distinction such
                 as Dr., Sir, Esq, or Ph.d (ignores case and a trailing
                 comma).
    Parameters:  userinfo (str) - the full name
    Returns:     (bool) True if a title is found
    """
    titles = ("dr", "dr.", "sir", "esq", "esq.", "ph.d", "ph.d.",
              "mr", "mr.", "mrs", "mrs.", "ms", "ms.", "prof", "prof.")
    for word in split_words(userinfo):
        word = mylower(word)
        if len(word) > 0 and word[len(word) - 1] == ",":
            word = word[0:len(word) - 1]
        if word in titles:
            return True
    return False

def toggle_case(userinfo):
    """
    Description: Swaps the case of every letter. Non-letters unchanged.
    Parameters:  userinfo (str) - the text to convert
    Returns:     (str) the text with each letter's case flipped
    """
    result = ""
    for char in userinfo:
        if 'A' <= char <= 'Z':
            result = result + chr(ord(char) + 32)
        elif 'a' <= char <= 'z':
            result = result + chr(ord(char) - 32)
        else:
            result = result + char
    return result

def main():
    """
    Description: Program entry point. Asks for a name/word, then shows a
                 menu in a loop so every function can be tested.
    Parameters:  none
    Returns:     nothing
    """
    while True:
        userinfo = input("\nEnter name/word(s) you have chosen: ")
        if userinfo == int:
            print("Please enter a word or name")
            continue
        else:
            break
    #displays a menu and loops so if the answer isnt applicable or function is finished it is possible to repeat
    while True:
        userinput = input("""\nPick which function to run:

    1)  Reverse and Display
    2)  Vowel Amount
    3)  Consonant frequency
    4)  Return First Name
    5)  Return Last Name
    6)  Return Middle Name(s)
    7)  Does the last name contain a hyphen?
    8)  Convert to lowercase
    9)  Convert to uppercase
    10) Random name (mix up letters)
    11) Is the first name a palindrome?
    12) Sorted array of characters
    13) Initials
    14) Contains a title/distinction?
    15) Toggle case (my own)
    X)  EXIT OUT OF PROGRAM
    
    """)

        if userinput == '1':
            reverse_then_display(userinfo)
        elif userinput == '2':
            vowel_counter(userinfo)
        elif userinput == '3':
            consonant_frequency(userinfo)
        elif userinput == '4':
            get_first_name(userinfo)
        elif userinput == '5':
            get_last_name(userinfo)
        elif userinput == '6':
            print(f"Your middle name(s): {get_middle_names(userinfo)}")
        elif userinput == '7':
            print(f"Last name contains a hyphen: {check_for_hyphen(userinfo)}")
        elif userinput == '8':
            print(mylower(userinfo))
        elif userinput == '9':
            print(myupper(userinfo))
        elif userinput == '10':
            print(scramble_name(userinfo))
        elif userinput == '11':
            print(f"First name is a palindrome: {first_name_is_palindrome(userinfo)}")
        elif userinput == '12':
            print(sorted_characters(userinfo))
        elif userinput == '13':
            print(f"Your initials are: {make_initials(userinfo)}")
        elif userinput == '14':
            print(f"Name contains a title: {has_title(userinfo)}")
        elif userinput == '15':
            print(toggle_case(userinfo))
        elif userinput in ('x', 'X'):
            break
        else:
            print("Please give a number as outlined in the menu.")

main()