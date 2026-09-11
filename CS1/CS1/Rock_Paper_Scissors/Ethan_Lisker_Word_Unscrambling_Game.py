import random
import sys



name = input("what is your name? ")
print(f"Good luck, {name}")
words = ["hello", "goodbye", "forget", "context"]
games = 0
wins = 0
turns = 5
while True:
    word = random.choice(words)
    word_list = list(word)
    random.shuffle(word_list)
    display = "".join(word_list)
    end = False
    
    while turns > 0:
        user_word = input(f"Unscramble this word: {display} ").lower()
            
        if user_word == word and turns > 0:
            print("You won!")
            wins += 1
            turns = 0
        elif turns > 0:
            print(f"you have {turns} turns remaining")
            turns -= 1
            continue
        elif turns == 0:
            print(word)
    while end == False:
        reshuffle = input("Do you want to reshuffle? y/n ").lower()
        
        if reshuffle == "n":
            end = True    
        elif reshuffle == "y":
            random.shuffle(word_list)
            display = "".join(word_list)
            turns = 5
            end = True
            continue
        else:
            print("incorrect answer, use y/n")
        if reshuffle == "n":  
            new_game = input("Do you want to play again? ")    
            if new_game == "y":
                games += 1
                continue
            if new_game == "n":
                sys.exit()
            else:
                print("invalid response, use y/n")
            continue
            