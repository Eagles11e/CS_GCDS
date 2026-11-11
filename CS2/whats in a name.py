
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
#                                                                      #
# Log:         - 9/29/2026: Submitted                                  #
#              - 11/11/2026: Added In-Line Documentation               #
########################################################################

import random

def mylower(text):
    """
    Description: Converts every uppercase letter in a string to lowercase.
    Parameters:  text (str) - the string to convert
    Returns:     (str) a new string with all letters lowercase
    """    
    result = ""                                                                                # result = empty string
    for char in text:
        if 'A' <= char <= 'Z':                                                                 # chained comparison, true only if char is between A and Z
            result = result + chr(ord(char) + 32)                                              # ord gives the letter's number, +32 jumps to lowercase, chr turns it back into a letter
        else:
            result = result + char                                                             # adds the result to the character given
    return result

def myupper(text):
    """
    Description: Converts every lowercase letter in a string to uppercase.
    Parameters:  text (str) - the string to convert
    Returns:     (str) a new string with all letters uppercase
    """
    result = ""                                                                                # starts with an empty string
    for char in text:
        if 'a' <= char <= 'z':                                                                 # checks if the character is lowercase
            result = result + chr(ord(char) - 32)                                              # same idea as above for mylower but backwards, -32 goes lowercase to uppercase
        else:
            result = result + char                                                             # adds the result to the character given
    return result

def myjoin(item_list, separator):
    """
    Description: Joins the items of a list into one string, placing the
                 separator between items (not after the last one).
    Parameters:  item_list (list) - items to join (converted with str())
                 separator (str)  - text placed between each item
    Returns:     (str) the combined string
    """    
    joined_string = ""                                                                         # empty string to store the finished result
    
    for i in range(len(item_list)):
        joined_string = joined_string + str(item_list[i])                                      # str() so numbers or other types dont crash it
        if i < len(item_list) - 1:                                                             # last index is len - 1, so this skips the separator on the final item
            joined_string = joined_string + separator                                          # adds the seperator to the joinded string to connect them
    return joined_string

def reverse_then_display(string):
    """
    Description: Reverses a string and displays it.
    Parameters:  string (str) - the text to reverse
    Returns:     nothing (prints the reversed text)
    """
    reversed_str = ""
    for char in string:
        reversed_str = char + reversed_str                                                     # Putting each new character in front of the result reverses it            
    print(reversed_str)


def vowel_counter(userinfo):
    """
    Description: Counts the vowels (a, e, i, o, u) in a string,
                 ignoring case.
    Parameters:  userinfo (str) - the text to check
    Returns:     nothing (prints the vowel count)
    """
    userinfo = mylower(userinfo)                                                               # lowercase so A and a both match
    vowelcounter = 0                                                                           # sets the base value of vowelcounter to 0 
    vowels = ("a", "e", "i", "o", "u")                                                         # the vowels to be looked for

    for char in userinfo:
        if char in vowels:
            vowelcounter += 1                                                                  # adds up the amount of vowels to count them
    print(f"There are {vowelcounter} vowels in your name/word(s)")

def consonant_frequency(userinfo):
    """
    Description: Counts the consonants in a string, ignoring case.
                 Spaces, hyphens, digits, and other non-letters are
                 not counted.
    Parameters:  userinfo (str) - the text to check
    Returns:     nothing (prints the consonant count)
    """
    userinfo = mylower(userinfo)                                                               # lowercase so A and a both match
    count = 0                                                                                  # sets the base value of the counter to 0
    vowels = ("a", "e", "i", "o", "u")                                                         # gives the list of vowels

    for char in userinfo:
        if 'a' <= char <= 'z' and char not in vowels:                                          # checks for every letter except for vowels
            count += 1                                                                         # adds one to count
    print(f"There are {count} consonants in your name/word(s)")

def get_middle_names(userinfo):
    """
    Description: Finds the middle name(s): every word between the first
                 and last word.
    Parameters:  userinfo (str) - the full name
    Returns:     (str) middle names separated by spaces, or "" if the
                 name has fewer than three words
    """
    words = split_words(userinfo)                                                              # seperates the words in the word
    middle = []                                                                                # empty list
    for i in range(1, len(words) - 1):                                                         # for i in range of the middle of the word total 
        middle.append(words[i])                                                                # adds each middle name into the list
    return myjoin(middle, " ")                                                                 # joins the middle names with spaces between them

def get_first_name(userinfo):
    """
    Description: Extracts the first name (all characters before the
                 first space) and displays it.
    Parameters:  userinfo (str) - the full name
    Returns:     nothing (prints the first name)
    """
    first = []                                                                                 # empty list to store the first name
    for char in userinfo:
        if char == " ":                                                                        # checks for the first space in the name
            break             
        first.append(char)                                                                     # adds each character before the space into the list

    print(f"Your first name is: {myjoin(first, '')}")

def scramble_name(userinfo):
    """
    Description: Mixes up the letters of the name. Spaces stay in place.
    Parameters:  userinfo (str) - the full name
    Returns:     (str) the scrambled name
    """
    letters = []                                                                               # empty list to hold all the letters
    for char in userinfo:
        if char != " ":                                                                        # skips spaces so they arent mixed up
            letters.append(char)

    for i in range(len(letters) - 1, 0, -1):                                                   # counts backwards from the last index down to 1
        j = random.randint(0, i)                                                               # random spot from 0 to i, both ends included
        temp = letters[i]                                                                      # temp holds one letter so the swap doesnt lose it
        letters[i] = letters[j]                                                                # puts the random letter into the current spot
        letters[j] = temp                                                                      # finishes swapping the two letters


    result = ""                                                                                # empty string for the scrambled name
    next_letter = 0                                                                            # keeps track of which scrambled letter to use
    for char in userinfo:
        if char == " ":
            result = result + " "                                                              # keeps the spaces in their original spots
        else:
            result = result + letters[next_letter]                                             # adds the next scrambled letter
            next_letter += 1                                                                   # moves to the next letter in the list
    return result

def get_last_name(userinfo):
    """
    Description: Extracts the last name (the last word) and displays it.
                 Trailing spaces are ignored.
    Parameters:  userinfo (str) - the full name
    Returns:     nothing (prints the last name)
    """
    last = []                                                                                  # wipe the old word once a real letter shows up after a space
    new_word = False                                                                           # True after a space, until a letter appears

    for char in userinfo:
        if char == " ":
            new_word = True                                                                    # flag so we know a new word might be starting

        else:
            if new_word:
                last = []                                                                      # clears the previous word when a new one starts
                new_word = False                                                               # resets the flag until another space is found
            last.append(char)                                                                  # adds the character to the current word

    print(f"Your last name is: {myjoin(last, '')}")

def check_for_hyphen(userinfo):
    """
    Description: Checks whether the LAST name contains a hyphen.
    Parameters:  userinfo (str) - the full name
    Returns:     (bool) True if the last name has a '-', else False
    """
    words = split_words(userinfo)                                                              # separates the name into individual words
    if len(words) == 0:
        return False                                                                           # returns false if there are no words
    for char in words[len(words) - 1]:                                                         # last word in the list (last index is len - 1)
        if char == '-':
            return True                                                                        # returns true if a hyphen is found
    return False                                                                               # no hyphen was found in the last name

def split_words(text):
    """
    Description: Splits text into a list of words on spaces. Extra,
                 leading, and trailing spaces are ignored.
    Parameters:  text (str) - the full name
    Returns:     (list) of word strings (empty list if no words)
    """
    words = []                                                                                 # empty list to hold the finished words
    current = []                                                                               # holds the characters of the current word
    for char in text:
        if char == " ":
            if len(current) > 0:                                                               # makes sure there is a word before adding it
                words.append(myjoin(current, ""))                                              # joins the letters and adds the word to the list
                current = []                                                                   # resets the list for the next word
        else:
            current.append(char)                                                               # adds the character to the current word
    if len(current) > 0:
        words.append(myjoin(current, ""))                                                      # adds the final word if there is one
    return words

def first_name_is_palindrome(userinfo):
    """
    Description: Checks whether the first name reads the same forward
                 and backward, ignoring case.
    Parameters:  userinfo (str) - the full name
    Returns:     (bool) True if the first name is a palindrome
    """
    words = split_words(userinfo)                                                              # splits the full name into separate words
    if len(words) == 0:
        return False                                                                           # cannot check if there are no words
    first = mylower(words[0])                                                                  # converts the first name to lowercase
    left = 0                                                                                   # starts at the first letter
    right = len(first) - 1                                                                     # starts at the last letter
    while left < right:                                                                        # checks letters from both sides until reaching the middle
        if first[left] != first[right]:
            return False                                                                       # if the letters dont match it isnt a palindrome
        left += 1                                                                              # moves one character to the right
        right -= 1                                                                             # moves one character to the left
    return True                                                                                # all letters matched so it is a palindrome

def sorted_characters(userinfo):
    """
    Description: Returns the name as a sorted array of characters
                 (spaces removed), ordered by character code.
    Parameters:  userinfo (str) - the full name
    Returns:     (list) of single characters in sorted order
    """
    chars = []                                                                                 # empty list to store the characters
    for char in userinfo:
        if char != " ":
            chars.append(char)                                                                 # adds all characters except spaces

    for i in range(len(chars)):                                                                # loops through every character in the list
        smallest = i                                                                           # assumes the current position has the smallest character
        for j in range(i + 1, len(chars)):                                                     # checks the remaining characters
            if chars[j] < chars[smallest]:
                smallest = j                                                                   # updates the smallest character found
        temp = chars[i]                                                                        # temporarily stores the current character
        chars[i] = chars[smallest]                                                             # moves the smallest character into position
        chars[smallest] = temp                                                                 # finishes swapping the characters
    return chars

def make_initials(userinfo):
    """
    Description: Makes initials (first letter of each word, uppercase,
                 each followed by a period).
    Parameters:  userinfo (str) - the full name
    Returns:     (str) initials such as "E.L."
    """
    initials = ""                                                                              # empty string to store the initials
    for word in split_words(userinfo):
        initials = initials + myupper(word[0]) + "."                                           # takes the first letter, makes it uppercase and adds a period
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
        "mr", "mr.", "mrs", "mrs.", "ms", "ms.", "prof", "prof.")                              # list of titles that the program checks for
    for word in split_words(userinfo):
        word = mylower(word)                                                                   # makes the word lowercase so capitalization doesnt matter
        if len(word) > 0 and word[len(word) - 1] == ",":                                       # checks if the word ends with a comma
            word = word[0:len(word) - 1]                                                       # removes the comma from the word
        if word in titles:
            return True                                                                        # returns true if the word matches one of the titles
    return False                                                                               # returns false if there were no titles found

def toggle_case(userinfo):
    """
    Description: Swaps the case of every letter. Non-letters unchanged.
    Parameters:  userinfo (str) - the text to convert
    Returns:     (str) the text with each letter's case flipped
    """
    result = ""                                                                                # empty string to store the changed text
    for char in userinfo:
        if 'A' <= char <= 'Z':                                                                 # checks if the character is uppercase
            result = result + chr(ord(char) + 32)                                              # converts the uppercase letter to lowercase
        elif 'a' <= char <= 'z':                                                               # checks if the character is lowercase
            result = result + chr(ord(char) - 32)                                              # converts the lowercase letter to uppercase
        else:
            result = result + char                                                             # keeps spaces, numbers and other symbols the same
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
        if userinfo == int:                                                                     # if userinfo is an integer
            print("Please enter a word or name")
            continue                                                                            # continues 
        else:
            break
                                                                                                # displays a menu and loops so if the answer isnt applicable or function is finished it is possible to repeat
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

        if userinput == '1':                                                                    # if the input = 1
            reverse_then_display(userinfo)                                                      # runs the reverse then display function
        elif userinput == '2':                                                                  # if the input = 2
            vowel_counter(userinfo)                                                             # runs the vowel counter function
        elif userinput == '3':                                                                  # if the input = 3
            consonant_frequency(userinfo)                                                       # runs the consonant frequency function
        elif userinput == '4':                                                                  # if the input = 4
            get_first_name(userinfo)                                                            # runs the get first name function
        elif userinput == '5':                                                                  # if the input = 5
            get_last_name(userinfo)                                                             # runs the get last name function
        elif userinput == '6':                                                                  # if the input = 6
            print(f"Your middle name(s): {get_middle_names(userinfo)}")                         # runs the get middle names function
        elif userinput == '7':                                                                  # if the input = 7
            print(f"Last name contains a hyphen: {check_for_hyphen(userinfo)}")                 # runs the check for hyphen function
        elif userinput == '8':                                                                  # if the input = 8
            print(mylower(userinfo))                                                            # runs the my lower function
        elif userinput == '9':                                                                  # if the input = 9
            print(myupper(userinfo))                                                            # runs the my upper function
        elif userinput == '10':                                                                 # if the input = 10
            print(scramble_name(userinfo))                                                      # runs the scrabble name function
        elif userinput == '11':                                                                 # if the input = 11
            print(f"First name is a palindrome: {first_name_is_palindrome(userinfo)}")          # runs the first name is palindrome function
        elif userinput == '12':                                                                 # if the input = 12
            print(sorted_characters(userinfo))                                                  # runs the sorted characters function
        elif userinput == '13':                                                                 # if the input = 13
            print(f"Your initials are: {make_initials(userinfo)}")                              # runs the initials function
        elif userinput == '14':                                                                 # if the input = 14
            print(f"Name contains a title: {has_title(userinfo)}")                              # runs the title function
        elif userinput == '15':                                                                 # if the input = 15
            print(toggle_case(userinfo))                                                        # runs the toggle case function
        elif userinput in ('x', 'X'):                                                           # else if the input = x
            break
        else:
            print("Please give a number as outlined in the menu.")                              # tells user their input is invalid

main()