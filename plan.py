from random import randint
import time
import pyttsx3
engine = pyttsx3.init()
engine.say("I will speak this text")
engine.runAndWait()
""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
print(rate)                        #printing current voice rate
engine.setProperty('rate', 600)     # setting up new voice rate


"""VOLUME"""
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
print (volume)                          #printing current volume level
engine.setProperty('volume',1.0)    #setting up volume level  between 0 and 1

"""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

engine.say("Hello World!")
engine.say('My current speaking rate is ' + str(rate))
engine.runAndWait()
engine.stop()

"""Saving Voice to a file"""
# On linux make sure that 'espeak' and 'ffmpeg' are installed
engine.save_to_file('Hello World', 'test.mp3')
engine.runAndWait()
#array of possible punches and weaves 
#select random length of combo,n, w max of 5
#(randomly select a p/w from the array)* n
#add each randomly selected p/w into a list
#https://pypi.org/project/pyttsx3/ for the text to speech conversion
#read out the combo#
#configurable round lengths,r, rest lengths,re, number of rounds,nr

