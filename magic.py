#import requests
#from bs4 import beautifulsoup4
import time

global timesince
global oldtext
global newtext
global zzz

timesince = 0
zzz = int(input('How many seconds between each check? '))
if (zzz <= 19):
    zzz = int(input("I can't go that fast! Try something greater than 19 "))
oldtext = ""
newtext = ""

def main():
    def alaina():
        global newtext
        global oldtext
        oldtext = 'I Am Walker and Also Run'
        newtext = 'I Am Walker and Never Run'
        print("made it past alaina")

    def henry(timesince):
        print("twilio time" , timesince, newtext)

    def magic():
        global timesince
        global newtext
        global oldtext
        global zzz
        print("made it to magic")
        if (oldtext == newtext):
            timesince += zzz
            print("theyre the same" , timesince)
            return(timesince)
        else:
            timesince += zzz
            henry(timesince)
            timesince = 0
            oldtext = newtext
            return(timesince, oldtext)
    alaina()
    magic()

while True:
    main()
    time.sleep(zzz)
    




