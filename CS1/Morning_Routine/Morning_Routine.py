import sys  # for the sys.exit to work this has to be here.
import os
import random


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def new_window():
    sys.stdout.write("\033[?1049h")
    sys.stdout.flush()


def previous_window():
    sys.stdout.write("\033[?1049l")
    sys.stdout.flush()


def flashbang():
    print("YOU ARE FLASHBANGED")


def shower_temp():
    print("\nYou now attempt to make the shower the right temperature")
    temp = random.randint(1, 100)
    while True:
        guess = int(input("\nGuess the shower temp: "))
        if not (guess >= 1 and guess <= 100):
            print("\nTemp must be from 1-100")
            continue
        elif guess > temp:
            print("\n\033[31mToo Hot! \033[0m")
        elif guess < temp:
            print("\n\033[34mToo Cold! \033[0m")
        else:
            print("\n\033[32mYou got it! \033[0m")
            break


new_window()
clear()

print("Good Morning\n")  # start of the code --> does not repeat ever.
flashbang()


def breakfast():
    cheerios = input("\nDo you want Cheerios for breakfast? ").lower()
    if cheerios == "yes":
        print("\nYou eat Cheerios ")
    elif cheerios == "no":
        print("\nYou don't end up eating cherios for breakfast ")
        pancakes = input("\nDo you want pancakes for breakfast? ").lower()
        if pancakes == "yes":
            print("\nYou eat pancakes for breakfast ")
        elif pancakes == "no":
            print("\nYou don't eat breakfast ")
        else:
            print("\nYou messed up, no breakfast for you. (Use yes/no next time)")
    else:
        print("\nInvalid response, no breakfast for you. (Use yes/no next time)")


while True:
    school = input("\nIs there school today? ").lower()
    if school == "no":
        print("\nYou go back to sleep")
        input("\nPress enter to exit")
        previous_window()
        sys.exit()  # exits the code and causes the rest of it to not play.

    elif school == "yes":
        break
    else:
        print("\nInvalid response use yes/no")

time_wake = input("\nWhat time is it? (hrs:mins) ").lower()
hour_wake = int(
    time_wake[0]
)  # checks the first integer of the input to see if it matches terms below (This only works with numbers, if a letter is imputed there will be an error code - this has no fix)
minute_wake = int(time_wake[2] + time_wake[3])

while True:
    if hour_wake > 7:
        print("\nYou overslept")
        break
    if (
        hour_wake == 7
    ):  # not totally on time since it only checks the first interger, but I might add 2nd and 3rd interger checks to make sure that this is correct.
        print("\nYou get out of bed on time")
        break
    elif hour_wake < 7:
        print("\nYou snooze for 15 minutes")
        minute_wake += 15
        if minute_wake >= 60:
            hour_wake += 1
            minute_wake = 0
            print("\nIt is now ", end="")
            print(hour_wake, end="")
            print(":00")
        else:
            print("\nIt is now ", end="")
            print(hour_wake, end="")
            print(":", end="")
            print(minute_wake)

        while True:  # loop for the alarm clock.
            if hour_wake == 7:
                break
            elif hour_wake < 7:
                break
            else:
                print("\nInvalid respose")
                break
    else:
        print("\nInvalid response")
while True:
    breakfast()  # all this code is above, so the code looks much cleaner and it allows for the definition not to be in the middle of the line.
    shower_temp()
    print("\nYou go to school")
    break

input("\nPress enter to exit")
previous_window()
