


time = "10:10"


input_time = input("Input the time with colon: ")
    
if input_time == time:
        print("wake up")
        
elif input != "10:10":
        print ("snooze for 10 minutes")
else:
        print("you overslept")
        
# 7:10
# 7:34
# 6:58

input_time = int (input_time[0]) #only works with 0-9

if input_time >= 7:
    print("you should wake up")