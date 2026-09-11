import random                                                                   #imports random
eight_ball = [                                                                  #possible answers and their corresponding color. 32m = green, 34m = blue, 31m = red.
            "\033[32mYes\033[m",
            "\033[31mNo\033[m",
            "\033[34mMaybe\033[m",
            "\033[34mAsk again later\033[m",
            "\033[32mIt is certain\033[m",
            "\033[32mSigns point to yes\033[m",
            "\033[31mNo chance\033[m",
            "\033[31mProbably not\033[m",
            "\033[34mCannot predict now\033[m",
            "\033[32m100%\033[m",
            "\033[31mNo way\033[m",
            "\033[32mProvably\033[m",
            "\033[34mToo hard to predict\033[m",
            "\033[34mI can not answer that\033[m",
            "\033[31mNo way\033[m"
            ]

while True:                                                                     #forever loop
    question = input("\nAsk your question: ")                                   #prompts user to ask a question
    
    if "?" in question:                                                         #checks if the user imput has a question mark
        print(f"\n{random.choice(eight_ball)}")                                 #prints one of the possible answers
        finish = input("\nType exit to end, or don't to continue: ").lower()    #prompts user to end the code if they want
        if finish == "exit":                                                    #checks if the user types exit
            break                                                               #ends the coe
    else:                                                                       #otherwise
        print("\nNot a question")                                               #prints