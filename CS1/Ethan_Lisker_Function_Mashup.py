import random
import time

def chorus():

    '''
    Prints the chorus lyrics of "Creep" by Radiohead with a 5 second pause after
 
    Args:
        None
 
    Print:
        Print (str): The chorus lyrics printed to the console
 
    Raises:
        None
    '''    
    
    print("""But I'm a creep
I'm a weirdo
What the hell am I doin' here?
I don't belong here\n""")
    time.sleep(5)      

def sing_song():
    
    '''
    Prints the full lyrics of "Creep" by Radiohead with timed pauses between sections
 
    Args:
        None
 
    Print:
        Print (str): All verses, choruses, and the bridge printed to the console with delays
 
    Raises:
        None
    '''
    
    
    verse_1 = print("""When you were here before
Couldn't look you in the eye
You're just like an angel
Your skin makes me cry
You float like a feather
In a beautiful world
I wish I was special
You're so very special\n""")
    time.sleep(10)
    chorus()
    verse_2 = print("""I don't care if it hurts
I wanna have control
I want a perfect body
I want a perfect soul
I want you to notice
When I'm not around
You're so very special
I wish I was special\n""")
    time.sleep(10)
    chorus()

    bridge = print("""She's runnin' out the door
She's runnin' out
She run, run, run, run
Run
""")
    time.sleep(6) 
    verse_3 = print("""Whatever makes you happy
Whatever you want
You're so fuckin' special
I wish I was special\n""")
    time.sleep(2)  
    chorus()

def get(order):
    
    '''
    Prompts the user to enter a positive integer and keeps asking until a valid one is given
 
    Args:
        order (str): A label for the prompt, such as "first" or "second"
 
    Return:
        Return (int): The valid positive integer entered by the user
 
    Raises:
        ValueError: If the input cannot be converted to an integer, prints an error and breaks the loop
    '''
    
    while True:
        try:
            num = int(input(f'Enter your {order} integer: '))
            
            if num > 0:
                return num   
        except ValueError:
            print("Please input an integer")
            break

def add():
    
    '''
    Repeatedly asks the user for two positive integers and prints their sum until the user chooses to stop
 
    Args:
        None
 
    Return:
        Return (int): The sum of the two entered integers printed to the console
 
    Raises:
        None
    '''
    
    while True:
        a = get("first")
        b = get("second")
        print(a+b)
        
        print('This allows you to add numbers')
        
        again = input('run again? y/n ').lower()
        
        if again == 'n':
            break

def print_list(): 

    '''
    Asks the user for a string and prints each character on its own line
 
    Args:
        string (str): Any text entered by the user
 
    Print:
        Print (str): Each individual character of the input printed on a separate line
 
    Raises:
        None
    '''

    string = input("Say something: ")
    for i in string:
        print(i)
    
def in_list():
    
    '''
    Asks the user for a comma-separated list and checks whether a given element is in it
 
    Args:
        array (str): A comma-separated list of elements entered by the user
        element (str): The element to search for in the list
 
    Print:
        Print (str): A message saying whether or not the element was found in the list
 
    Raises:
        None
    '''    
        
    array = input("Enter the elements seperate by commas").split(",")
    element = input("Enter the element to check in the list")
    if element in array:
        print("Your element is in the list")
    else:
        print("Your element is not in the list")

def is_integer(value):    
    
    '''
    Checks whether a given value can be converted to an integer
 
    Args:
        value (str): The value to check
 
    Return:
        Return (bool): Returns True if the value is an integer, False if it is not
 
    Raises:
        ValueError: Caught internally if the value cannot be converted to an integer
    '''
    
    try:
        int(value)
        return True
    except ValueError:
        return False  

def get_integer():
    
    '''
    Repeatedly prompts the user to enter a number until a valid integer is provided
 
    Args:
        None
 
    Return:
        Return (int): The valid integer entered by the user
 
    Raises:
        None
    '''

    while True:
        value = input("Pick a number: ")
        
        if is_integer(value):
            return int(value)

def number_picker():
    
    '''
    Generates a random number from 1 to 100 and lets the user guess it, giving hints until correct
 
    Args:
        None
 
    Print:
        Print (str): Prints "Too High", "Too Low", or "You got it" depending on the guess
 
    Raises:
        None
    '''
    
    number = random.randint(1, 100)
    
    while True:
        guess = get_integer()
        
        if not (guess >= 1 and guess <= 100):
            print("\nNumber must be from 1-100")
            continue
        elif guess > number:
            print("\n\033[31mToo High! \033[0m")
        elif guess < number:
            print("\n\033[34mToo Low! \033[0m")
        else:
            print("\n\033[32mYou got it! \033[0m")
            break

def get_random():
    
    '''
    Asks the user for two integers and prints a random number between them
 
    Args:
        number1 (int): The first boundary number entered by the user
        number2 (int): The second boundary number entered by the user
 
    Return:
        Return (int): A random integer between the two provided numbers, inclusive
 
    Raises:
        None
    '''
    
    number1 = get_integer()
    number2 = get_integer()
    
    if number1 < number2:
        print(random.randint(number1,number2))
    else:
        print(random.randint(number2,number1))

def count_vowels():
    
    '''
    Asks the user for a string and counts the total number of each vowel and all vowels combined
 
    Args:
        vowel_line (str): Any sentence or word entered by the user
 
    Print:
        Print (str): Prints the count of each individual vowel (a, e, i, o, u) and the total vowel count
 
    Raises:
        None
    '''
    
    a_number = 0
    e_number = 0
    i_number = 0
    o_number = 0
    u_number = 0
    
    number = 0
    vowel_line = input("Say something and the vowel counter will count the amount of vowels: ").lower()
    vowels = ["a","e","i","o","u"]
    a1 = ["a"]
    e1 = ["e"]
    i1 = ["i"]
    o1 = ["o"]
    u1 = ["u"]
    for i in vowel_line:
        if i in vowels:
            number +=1
        if i in a1:
                a_number += 1 
        if i in e1:
            e_number += 1 
        if i in i1:
            i_number += 1
        if i in o1:
            o_number += 1
        if i in u1:
            u_number += 1
    numbers = number
    print (f"There are {a_number} total a's")
    print (f"There are {e_number} total e's")
    print (f"There are {i_number} total i's")
    print (f"There are {o_number} total o's")
    print (f"There are {u_number} total u's")
    print (f"There are {numbers} total vowels")

def funciton_picker():
    
    '''
    Displays a menu and runs the function corresponding to the user's number choice
 
    Args:
        pick (str): A number from 1 to 9 entered by the user representing the desired function
 
    Print:
        Print (str): Runs and prints the output of the chosen function, or a message if the input is out of range
 
    Raises:
        None
    '''
    
    pick = input("""Which function would you like to use?
                 1 = sing song
                 2 = add
                 3 = print list
                 4 = in list
                 5 = number picker
                 6 = is integer
                 7 = get integer
                 8 = get random
                 9 = count vowels
                 10+ = nonexistant
                 below 1 = nonexistant
                 dont put in decimals
                 What would you like to use? """)
    
    if pick == "1": sing_song()
    elif pick == "2": add()
    elif pick == "3": print_list()
    elif pick == "4": in_list()
    elif pick == "5": number_picker()
    elif pick == "6": is_integer(value = input("Say something and you will be told if it is an integer: "))
    elif pick == "7": get_integer()
    elif pick == "8": get_random()
    elif pick == "9": count_vowels()
    else:
        print("Pick a number 1-9")

funciton_picker()