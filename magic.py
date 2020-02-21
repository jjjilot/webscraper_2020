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

def magic(oldtext, newtext, timesince):
    alaina()
    if (oldtext == newtext):
        timesince = timesince + zzz
    else:
        timesince = (timesince + zzz)
    return(timesince)
alaina
print("It's been" + magic(oldtext, newtext, timesince))
    

    




