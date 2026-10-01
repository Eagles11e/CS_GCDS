import time
def chorus():
    print("""But I'm a creep
I'm a weirdo
What the hell am I doin' here?
I don't belong here\n""")
    time.sleep(5)
        
def sing_song():
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

sing_song()
