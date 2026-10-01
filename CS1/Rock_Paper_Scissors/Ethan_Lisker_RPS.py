import random                                                       #imports random
import pygame                                                       #imports pygame
import sys                                                          #imports system

pygame.init()                                                       #starts pygame
screen = pygame.display.set_mode((800, 600))                        #sets the screen size to 800, 600

def score():                                                        #prints the score
    print(f"\nThe score is {player} to {robot}")                    
robot = 0                                                           #resets the robot score
player = 0                                                          #resets the player score

print("\nWelcome to Rock, Paper, Scissors. You are going against the robot and the first to 3 wins. Good luck!")    #prints opening statement

while True:                                                         #forever loop
    rps = ["rock","paper","scissors"]                               #list of possible outputs for the game
    player_input = input("\nRock, Paper, or Scissors? ").lower()    #prompts the user to pick r, p, or s
    robot_choice = random.choice(rps)                               #picks a random answer from the list
    print(f"\nThe robot picks {robot_choice}")                      #prints the robot choice    
    if player_input == "rock":                                      #checks if the player imput is rock
        
        rock = pygame.image.load("rock.png")                        #loads rock image
        rock = pygame.transform.scale(rock, (800,600))              #sets the size of the rock image to 800, 600
        while True:                                                 #forever loop
            for event in pygame.event.get():                        #when something happens in pygame
                if event.type == pygame.QUIT:                       #if you quit pygame
                    pygame.quit()                                   #quits pygame
                    sys.exit()                                      #exits the program
            screen.fill((255, 255, 255))                            #fills the screen with white
            screen.blit(rock, (0,0))                                #displays the rock in the middle
            pygame.display.flip()                                   #flips the buffers
            break                                                   #breaks
            
        if robot_choice == "paper":                                 #checks if the robot choice is paper
            print("\033[31m\nYou lose!\033[m")                      #prints you lose
            robot += 1                                              #adds one to the robot score
            score()
        elif robot_choice == "scissors":                            #checks if the robot choice is scissors
            print("\033[32m\nYou win!\033[m")                       #prints you win
            player += 1                                             #adds one to the player score
            score()
    elif player_input == "paper":                                   #checks if the player imput is paper
        
        paper = pygame.image.load("paper.png")
        paper = pygame.transform.scale(paper, (800,600))
        while True: 
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                screen.fill((255, 255, 255))
                screen.blit(paper, (0,0))
                pygame.display.flip()
                break
        
        if robot_choice == "rock":                                  #checks if the robot choice is rock
            print("\033[32m\nYou win!\033[m")
            player += 1
            score()
        elif robot_choice == "scissors":                            #checks if the robot choice is scissors
            print("\033[31m\nYou lose!\033[m") 
            robot += 1
            score()
    elif player_input == "scissors":                                #checks if the player imput is scissors
        
        scissors = pygame.image.load("scissors.png")
        scissors = pygame.transform.scale(scissors, (800,600))
        while True: 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            screen.fill((255, 255, 255))
            screen.blit(scissors, (0,0))
            pygame.display.flip()
            break
        
        if robot_choice == "rock":                                  #checks if the robot choice is rock
            print("\033[31m\nYou lose!\033[m") 
            robot += 1
            score()
        elif robot_choice == "paper":                               #checks if the robot choice is paper
            print("\033[32m\nYou win!\033[m")
            player += 1
            score()
    if player_input == robot_choice:                              #checks if there is a tie
        print("\nTie")                                              #prints tie
    else:                                                           #otherwise
        print("\nYou must say either rock, paper, or scissors.")    #prints that the player must use r, p, or s
        continue                                                    #goes back to the top of the loop
    if player == 3 or robot == 3:                                   #if one player wins
        if player == 3:                                             #checks the player's score
            print("\033[32m\nYou beat the robot!\033[m")            #prints you beat the robot
        if robot == 3:                                              #checks the robot's score
            print("\033[31m\nYou lost to the robot!\033[m")         #prints you lost to the robot
        again = input("\nType 1 to play again: ").lower()           #prompts the player to continue if they want
        if again == "1":                                            #checks the input
            robot = 0                                               #resets the robot's score
            player = 0                                              #resets the player's score
            print("\nWelcome to Rock, Paper, Scissors. You are going against the robot and the first to 3 wins. Good luck!") #prints opening statement
            continue                                                #goes back to the top of the loop
        else:                                                       #otherwise
            break                                                   #breaks the loop
    else:                                                           #otherwise
        continue                                                    #goes back to the top of the loop