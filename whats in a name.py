"""
Ethan Lisker

Funtions to manipulate and run things through strings
"""


def mylower(text):
    result = ""
    for char in text:
        if 'A' <= char <= 'Z':
            result = result + chr(ord(char) + 32)
        else:
            result = result + char 
    return result

def myjoin(item_list, separator):
    joined_string = ""
    
    for i in range(len(item_list)):
        joined_string = joined_string + str(item_list[i])
        
        if i < len(item_list) - 1:
            joined_string = joined_string + separator    




userinfo = input("Enter name/word(s) you have chosen? ")


def main(userinfo):
    userinput = input("""\n Pick which function to run:
                      
                      1) Reverse and Display
                      2) Vowel Amount
                      3) Consonant frequency
                      4) Return First Name
                      5) Return Last Name
                      6) Return Middle Name(s)
                      7) Return boolean if last name contains a hyphen
                      8) Function to convert to lowercase
                      
                      
                    
                      """)
    
    if userinput == ('1'):
        revanddis(userinfo)
    if userinput == ('2'):
        vowel_counter(userinfo)
    if userinput == ('3'):
        consonant_frequency(userinfo)
    if userinput == ('4'):
        first_name(userinfo)
    if userinput == ('5'):
        last_name(userinfo)
    if userinput == ('7'):
        has_hyphen(userinfo)
    else:
        print("Please give a number as outlined in the menu.")
        main(userinfo)

def revanddis(string):
    revanddis = ""
    for char in string:
        revanddis = char + revanddis
    print(revanddis)

def vowel_counter(userinfo):
    userinfo = mylower(userinfo)
    vowelcounter = 0
    x = userinfo
    characters = ("a", "e", "i", "o", "u")
    for char in x:
        if char in characters:
            vowelcounter += 1
    print(f"There are {vowelcounter} vowels in your name/word(s)")

def consonant_frequency(userinfo):
    userinfo = mylower(userinfo)
    count = 0
    x = userinfo
    characters = ("a", "e", "i", "o", "u")
    for char in userinfo:
        if char not in characters:
            count += 1
    print (f"There are {count} consonants in your name/wordS(s)")

def first_name(userinfo):
    first = []
    for char in userinfo:
        if char == " ":
            break
        first.append(char)
    
    first_name_str = myjoin("",first)
    print(f"Your first name is: {first_name_str}")

def last_name(userinfo):
    last = []
    for char in userinfo:
        if char == " ":
            break
        last.append(char)
    
    last_name_str = myjoin("",last)
    print(f"Your last name is: {last_name_str}")
    

def has_hyphen(userinfo):
    found_hyphen = False
    for char in userinfo:
        if char == '-':
            found_hyphen = True
            break
    print(f"Last name contains a hyphen: {found_hyphen}")



main(userinfo)
    