import random
def band(musicians, instruments):
    print (musicians)
    for e in instruments:
        print(e)
    for index in range(len(instruments)):
        for i in range (random.randrange(1, 6)):
            print(f"Musician: {musicians[index]}, Instrument: {instruments[index]}")
 
    
band(['Bruce Springsteen', 'Billy Joel', 'Drake'], ['Keyboard', 'Drums', 'Synth'])