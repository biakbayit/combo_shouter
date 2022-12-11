from random import randint
import time
from datetime import datetime
import pyttsx3
engine = pyttsx3.init()

ROUND_REST = 60 #seconds
COMBO_MULTIPLIER = 0.7 #seconds
MAX_COMBO = 5
WORD_PAUSE = 1 #seconds
SPEAKING_RATE = 160
NO_OF_ROUNDS = 5
LENGTH_OF_ROUND = 120 #seconds
engine.setProperty('rate',SPEAKING_RATE)


#array of possible punches and weaves 
possible_moves = ['jab','cross','left uppercut','right uppercut','left hook','right hook','slip','roll','pivot']
#select random length of combo,n, w max of 5

for i in range(NO_OF_ROUNDS):  
    engine.say(f'Round {i}')
    engine.runAndWait()
    round = True
    start = datetime.now()
    while round:   
        combo_length = randint(1,MAX_COMBO)
        #(randomly select a p/w from the array)* n
        combo_pause = combo_length * COMBO_MULTIPLIER
        moves = []
        for _ in range(combo_length):
            move_idx = randint(0,len(possible_moves)-1)
            move = possible_moves[move_idx]
            #add each randomly selected p/w into a list
            moves.append(move)
        for move in moves:
            # Say stuff
            engine.say(move)
            engine.runAndWait()
            time.sleep(WORD_PAUSE)
        time.sleep(combo_pause)    
        # Give enough time to do combo
        end = datetime.now()
        length = (end - start).total_seconds()
        round = length < LENGTH_OF_ROUND
    engine.say(f'end of round {i}, rest for {ROUND_REST} seconds')
    engine.runAndWait()
    time.sleep(ROUND_REST)
#https://pypi.org/project/pyttsx3/ for the text to speech conversion


#read out the combo#
#configurable round lengths,r, rest lengths,re, number of rounds,nr
    