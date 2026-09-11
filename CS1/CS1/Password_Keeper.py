import csv

saved_usernames = []                                                                #empty list
saved_passwords = []                                                                #empty list
saved_apps = []                                                                     #empty list

def main():
    master = input("What is the password to enter the password keeper? ")           #inputs
    while True:
        if master == "Eagles11e":                                                   #if the password is correct
            main_passwordfunction()                                                 #runs the main function
        else:
            print("Wrong password")                                                 #prints
            master = input("What is the password to enter the password keeper? ")   #allows access to the password keeper
       
def main_passwordfunction():
    while True:
        new_app = input("Pick an app to create an account for: ")                   #input an account
        new_username = input("Pick a username: ")                                   #input a username
        new_password = input("Pick a password for that username: ")                 #input a password
        saved_apps.append(new_app)                                                  #appends the new app to the empty list
        saved_usernames.append(new_username)                                        #appends the new username to the empty list
        saved_passwords.append(new_password)                                        #appends the new password to the empty list
        yen = input("Would you like to create another new account? (y/n): ").lower() #Make psudocode for this down to attempts
        if yen == 'y':                                                              #if the user imputs y
            new_app = input("Pick an app to create an account for: ")               #inputs an app
            new_username = input("Pick a username: ")                               #inputs a username
            new_password = input("Pick a password for that username: ")             #inputs a password
            saved_apps.append(new_app)                                              #links the empty list with any new app
            saved_usernames.append(new_username)                                    #links the empty list with any new username
            saved_passwords.append(new_password)                                    #links the empty list with any new password
        if yen == 'n':                                                              #if the user doesnt want to make another account
            csv_file = input("Would you like to save your passwords to a csv file? (y/n) ")              #asks user if they want to put the passwords into a csv file
            if csv_file == 'y':                                                                          #if user inputs y
                data = ["Apps", "Usernames", "Passwords"]                                                #data
                for i in range(len(saved_apps)):                                                         #if something is in saved apps
                    data.append([[saved_apps[i], saved_usernames[i], saved_passwords[i]]])               #appends the saved apps, usernames, and passwords to the data that will write in csv
                with open("saved_apps.csv", "w") as file:                                                #opens a csv file
                    writer = csv.writer(file)                                                            #writes the data in rows
                    writer.writerows(data)
            else:
                print("You have chosen to not save your apps, accounts, and passwords to a csv file") #prints
            break                                                                   #goes to the entry of the account user and app along with password
        else:
            print("Please put a y or an n")                                         #prints
    attempts = 5                                                                    #attempt counter
    attempts2 = 5                                                                   #secondary attempt counter so the first doesnt have to be repeated

    for i in range(0, len(saved_apps)):                                                                                #if the saved apps list has something in it
        while attempts > 0:                                                                                            #while attempts remain
            if attempts == 5:                                                                                          #if 5 attempts remain
                attempts -= 1                                                                                          #removes an attempt
                app = input("Pick an app to log into: ").lower()                                                       #asks user to imput an app
            if app != saved_apps[i]:                                                                                   #if the app is not found to match the user imput
                attempts -= 1                                                                                          #removes an attempt
                print(f"You do not have an account for that app, you have {attempts} attempts remaining")              #prints
                app = input("What app do you want to log into? ").lower()                                              #inputs user app request (what app do you want to log into)
            elif app == saved_apps[i]:                                                                                 #if the app inputed = the saved app in the list
                print(f"You have accessed {app}")                                                                      #prints 
                break
            elif attempts < 1:                                                                                         #if you run out of attempts
                print(f"Unable to log into {app}, restart the password keeper to try again")                           #prints
                break
            else:
                attempts -= 1                                                                                          #removes an attempt
                print(f"You do not have an account for that app, you have {attempts} attempts remaining")              #prints
                app = input("What app do you want to log into? ")                                                      #asks the user to imput an app to log into
        else:
            print("You have run out of attempts to guess the app, reload the password keeper to try again")            #prints
            break


    for i in range(0, len(saved_usernames)):                                                                            #if a saved username exists
        while attempts2 > 0:                                                                                            #while any attempts remain
            if attempts2 == 5:                                                                                          #resets attempt count
                attempts2 -= 1                                                                                          #removes an attempt
                username = input("Which account would you like to log into? ").lower()                                  #what account would you like to log into input
            if username != saved_usernames[i]:                                                                          #if it is not matching the saved username
                attempts2 -= 1                                                                                          #removes an attempt
                print(f"You do not have a username called {username}, you have {attempts} attempts remaining")          #prints mesage regarding failed attempt
                username = input("Which account would you like to log into? ").lower()                                  #asks user which account they would like to log into
            elif username == saved_usernames[i]:                                                                        #if the username is found in the list and matches
                break
            elif attempts < 1:                                                                                          #when you have 0 attempts remaining
                print(f"Unable to access an account named {username}, restart the password keeper to try again")        #failure message
                break
            else:
                attempts2 -= 1                                                                                          #removes an attempt
                print(f"You do not have a username called {username}, you have {attempts} attempts remaining")          #failed attempt message
                username = input("Which account would you like to log into? ").lower()                                  #account login imput
        else:
            print("You have run out of attempts to guess the username, reload the password keeper to try again")        #failure message
            break
    
    if username in saved_usernames:                                                                                     #if the username is found
            attempts = 5                                                                                                #resets attempts
            password = input(f"What is your password for {username}? ")                                                 #input
            for i in range(0, len(saved_passwords)):                                                                    #sees if there is a password in saved passwords
                if username == saved_usernames[i] and password == saved_passwords[i]:                                   #if username and password are both correct
                    print(f"You have logged into {app} under the account {username}, and the password is {password}")   #print
                else:
                    while attempts > 0:                                                                                 #while attempts still exist
                        if password != saved_passwords[i]:                                                              #if it does not equal the password in the list
                            attempts -= 1                                                                               #removes an attempt
                            print(f"Incorrect password, you have {attempts} attempts remaining")                        #print
                            password = input(f"What is your password for {username}? ")                                 #input password (after failing)
                        elif password == saved_passwords[i]:                                                            #if password is in saved passwords
                            print(f"You have logged into {app} under the account {username}, and your password is {password}")  #log in message
                            return app, password, username                                                                      #returns all the info
                        elif attempts < 1:                                                                                      #if you fail
                            print("Unable to log into account, restart the password keeper to try again")                       #print
                            break
                    else:
                        print("You have run out of attempts to guess the password, reload the password keeper to try again")    #print
                        break
main()                                                                                                                          #runs main function
restart = input("Would you like to log into another account or would you like to end the password keeper? (y/n)").lower()       #asks user if they want to run the password keeper again
if restart == 'y':                                                                                                              #if user inputs y
    main()                                                                                                                      #runs the main function
else:
    print("Password keeper is now closed. Restart the code if you would like to run it again, as a reminder, you have to put y/n next time, so if you put 'yes' it will not work") #prints