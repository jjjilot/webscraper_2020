import time
from output import send_text

send_text()

global timesince
global oldtext
global newtext
global zzz

timesince = 0
oldtext = "old"
newtext = "new"

zzz = int(input('How many seconds between each check? '))
if (zzz < 20):
    zzz = int(input("I can't go that fast! Try something greater than 19 "))

def main():
    def alaina():
        global newtext
        global oldtext

    def henry():
        global timesince
        global zzz

    def magic():
        global timesince
        global newtext
        global oldtext
        global zzz
        if (oldtext == newtext):
            timesince += zzz
            return(timesince)
        else:
            timesince += zzz
            oldtext = newtext
            timesince = 0
            return(oldtext, timesince)

    alaina()
    magic()
    if (timesince == 0):
        henry()

while True:
    time.sleep(zzz)
    main()
    
    




