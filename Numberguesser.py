import random


def number_picker():
    number = random.randint(1, 100)
    while True:
        print (5 - 1)
        if (5 - 1) <= 0:
            break
        try:
            guess = int(input("\nGuess the number: "))
        except ValueError:
            print("\nMust input a number")
            continue
        if not (guess >= 1 and guess <= 100):
            print("\nNumber must be from 1-100")
            continue
        elif guess > number:
            print("\n\033[31mToo High! \033[0m")
            one = 1
        elif guess < number:
            print("\n\033[34mToo Low! \033[0m")
            one = 1
        else:
            print("\n\033[32mYou got it! \033[0m\n")
            break

number_picker()
