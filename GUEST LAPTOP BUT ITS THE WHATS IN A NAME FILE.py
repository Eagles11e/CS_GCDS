"""


"""




def mylower(text):
    result = []
    for char in text:
        if 'A' <= char <= 'Z':
            result.append(chr(ord(char) + 32))
        else:
            result.append(char)
    return ''.join(result)  






userinfo = input("Enter name/word(s) you have chosen? ")

def menu(userinput):
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


def revanddis(string):
    revanddis = ""
    for char in string:
        revanddis = char + revanddis
    print(revanddis)
    
        




def vowel_counter(userinfo):
    vowelcounter = 0
    x = userinfo
    characters = ("a", "e", "i", "o", "u")
    for char in x:
        if char in characters:
            vowelcounter += 1
    print(f"There are {vowelcounter} vowels in your name/word(s)")

menu(userinfo)
userinfo = mylower(userinfo)

vowel_counter(userinfo)