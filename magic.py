#import requests
#from bs4 import beautifulsoup4
import time

timesince = 0
zzz = int(input('How many seconds between each check? '))
if (zzz <= 19):
    zzz = int(input("I can't go that fast! Try something greater than 19 "))
oldtext = ""
newtext = ""

def alaina():
    
    oldtext = 'I Am Walker and Also Run'
    newtext = 'I Am Walker and Never Run'

    return (oldtext)
    return (newtext)

def henry(timesince):
    print("twilio time" , (str(timesince)))

def magic(oldtext, newtext, timesince):
    print("BRUHHHHHHHHHH")
    alaina()
    if (oldtext == newtext):
        timesince += zzz
        return(timesince)
        print("bruh")
        magic(oldtext, newtext, timesince)
    else:
        timesince += zzz
        return(timesince)
        henry(timesince)
    
magic(oldtext, newtext, timesince)


    




