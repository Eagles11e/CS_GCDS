########################################################################
# Name:        Ethan Lisker                                            #
# Assignment:  CS2 Functions - What's in a Name?                       #
# Description: A set of functions that manipulate and interrogate a    #
#              name or word entered by the user. A menu lets the user  #
#              choose which function to run. No string class methods   #
#              or global variables are used.                           #
#                                                                      #
# Bugs:        - none                                                  #
#                                                                      #
# Bonus:       - Menu (#13)                                            #
#              -                                                       #
########################################################################


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

def revanddis(string):
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
            break              # first space ends the first name
        first.append(char)

    print(f"Your first name is: {myjoin(first, '')}")


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
    Description: Checks whether the name contains a hyphen and displays
                 the True/False result.
    Parameters:  userinfo (str) - the text to check
    Returns:     nothing (prints True or False)
    """
    found_hyphen = False
    for char in userinfo:
        if char == '-':
            found_hyphen = True
            break              # to stop looking once found
    print(f"Last name contains a hyphen: {found_hyphen}")


def main():
    """
    Description: Program entry point. Asks the user for a name/word,
                 shows the menu, and runs the chosen function. The name
                 is kept local and passed to each function, so no global
                 variables are needed.
    Parameters:  none
    Returns:     nothing
    """
    userinfo = input("Enter name/word(s) you have chosen: ")
    userinput = input("""\nPick which function to run:

    1) Reverse and Display
    2) Vowel Amount
    3) Consonant frequency
    4) Return First Name
    5) Return Last Name
    6) Return Middle Name(s)
    7) Return boolean if last name contains a hyphen
    8) Convert to lowercase
    x) EXIT OUT OF PROGRAM

    """)
    while True:
        if userinput == '1':
            revanddis(userinfo)
            break
        elif userinput == '2':
            vowel_counter(userinfo)
            break
        elif userinput == '3':
            consonant_frequency(userinfo)
            break
        elif userinput == '4':
            get_first_name(userinfo)
            break
        elif userinput == '5':
            get_last_name(userinfo)
            break
        elif userinput == '7':
            check_for_hyphen(userinfo)
            break
        elif userinput == '8':
            print(mylower(userinfo))
            break
        elif userinput == ('x', 'X'):
            break
        else:
            print("Please give a number as outlined in the menu.")
            continue


main()