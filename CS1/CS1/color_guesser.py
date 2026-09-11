import random

colors = ["red","orange","yellow","green","blue"]
color = random.choice(colors)
tries = 3

while tries > 0:   
    
    guess = input("Guess a color: ")
    
    if guess == color :
        print(f"You got it in {3 - tries} tries!")
        break 
    
    else:
        tries -= 1
        print(f"You got it wrong! You have {tries} tries remaining!")