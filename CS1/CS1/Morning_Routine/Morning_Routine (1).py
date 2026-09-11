import sys                                                                         #imports system
import os                                                                          #imports os
import random                                                                      #imports random

def clear():                                                                       #clear window function
    os.system("cls" if os.name == "nt" else "clear")                               #clears the window

def new_window():                                                                  #new window function
    sys.stdout.write("\033[?1049h")                                                #opens a new window in the terminal
    sys.stdout.flush()                                                             #prints the output immedietly
def previous_window():                                                             #previous window function
    sys.stdout.write("\033[?1049l")                                                #returns to the previous window
    sys.stdout.flush()                                                             #prints the output immedietly

def flashbang():                                                                   #function for the flashbang command
    print("YOU ARE FLASHBANGED")                                                   #prints

def shower_temp():                                                                 #function to run the shower temp minigame
    print("\nYou now attempt to make the shower the right temperature")            #prints
    temp = random.randint(1, 100)                                                  #chooses a number 1-100
    while True:                                                                    #forever loop
        try:                                                                       #trys
            guess = int(input("\nGuess the shower temp: "))                        #converts the input into an integer so that it is readable by the code
        except ValueError:                                                         #if value error the code doesn't fully break
            print("\nMust input a number")                                         #prompts someone to guess
            continue                                                               #goes to the next variation of the loop
        if not (guess >= 1 and guess <= 100):                                      #if the guess isn't within the correct range
            print("\nTemp must be from 1-100")                                     #prints
            continue                                                               #goes to the next variation of the loop
        elif guess > temp:                                                         #if the guess is too high
            print("\n\033[31mToo Hot! \033[0m")                                    #prints
        elif guess < temp:                                                         #if the guess is too low
            print("\n\033[34mToo Cold! \033[0m")                                   #prints
        else:                                                                      #else
            print("\n\033[32mYou got it! \033[0m")                                 #prints
            break                                                                  #breaks the loop

new_window()                                                                       #opens a new window
clear()                                                                            #clears the window

print("Good Morning\n")                                                            #start of the code --> does not repeat ever.
flashbang()                                                                        #prints

def breakfast():                                                                   #function
    cheerios = input("\nDo you want Cheerios for breakfast? ").lower()             #prompts user to imput an answer
    if cheerios == "yes":                                                          #if they say yes
        print("\nYou eat Cheerios ")                                               #prints
    elif cheerios == "no":                                                         #if they say no
        print("\nYou don't end up eating cherios for breakfast ")                  #prints
        pancakes = input("\nDo you want pancakes for breakfast? ").lower()         #prompts user to imput an answer
        if pancakes == "yes":                                                      #if they say yes
            print("\nYou eat pancakes for breakfast ")                             #prints
        elif pancakes == "no":                                                     #if they say no
            print("\nYou don't eat breakfast ")                                    #prints
        else:                                                                      #otherwise
            print("\nYou messed up, no breakfast for you. (Use yes/no next time)") #prints
    else:                                                                          #otherwise
        print("\nInvalid response, no breakfast for you. (Use yes/no next time)")  #prints

while True:                                                                        #forever loop
    school = input("\nIs there school today? ").lower()                            #asking if there is school
    if school == "no":                                                             #if they say no
        print("\nYou go back to sleep")                                            #prints
        input("\nPress enter to exit: ")                                           #prompts user to exit the code
        previous_window()                                                          #returns to the previous window
        sys.exit()                                                                 #exits the window

    elif school == "yes":                                                          #if there is school
        break                                                                      #ends the loop
    else:                                                                          #otherwise
        print("\nInvalid response use yes/no")                                     #prints

time_wake = input("\nWhat time is it? (hrs:mins) ").lower()                        #prompts the user for the time
time_wake = time_wake.split(':')                                                   #splits the time by the colon allowing for 2 integers to check both sides of the colon
hour_wake = int(time_wake[0])                                                      #checks the first side of the colon (hours)
minute_wake = int(time_wake[1])                                                    #checks the second side of the colon (minutes)

while True:                                                                        #forever loop
    if hour_wake > 7:                                                              #if the time is greater than 7
        print("\nYou overslept")                                                   #prints
        break                                                                      #ends the loop
    if (hour_wake == 7):                                                           #if the time is 7
        print("\nYou get out of bed on time")                                      #prints
        break                                                                      #ends the loop
    elif hour_wake < 7:                                                            #if the time is less than 7
        print("\nYou snooze for 15 minutes")                                       #prints
        minute_wake += 15                                                          #adds 15 minutes to the time
        if minute_wake >= 60:                                                      #prevents mistakes and allows 60 minutes to equal 1 hour
            hour_wake += 1                                                         #adds one hour
            minute_wake = 0                                                        #resets the minutes
            print("\nIt is now ", end="")                                          #prints time
            print(hour_wake, end="")                                               #prints time
            print(":00")                                                           #prints time
        else:                                                                      #otherwise
            print("\nIt is now ", end="")                                          #prints time
            print(hour_wake, end="")                                               #prints time
            print(":", end="")                                                     #prints time
            print(minute_wake)                                                     #prints time

        while True:                                                                #forever loop inside forever loop
            if hour_wake == 7:                                                     #if the time is 7
                break                                                              #ends this loop
            elif hour_wake < 7:                                                    #if it is before 7
                break                                                              #ends this loop
            else:                                                                  #else
                print("\nInvalid respose")                                         #prints
                break                                                              #ends the loop
    else:                                                                          #else
        print("\nInvalid response")                                                #prints
while True:                                                                        #forever loop
    breakfast()                                                                    #runs the function breakfast()
    shower_temp()                                                                  #runs the function shower_temp()
    print("\nYou go to school")                                                    #prints
    break                                                                          #ends the loop

input("\nPress enter to exit: ")                                                   #manual end to the code
previous_window()                                                                  #returns to the previous window