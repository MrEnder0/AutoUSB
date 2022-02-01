from datetime import date
from logger import *
from config import *
import os

letters = ["C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
today = date.today()
date = today.strftime("%m/%d/%y")

def fileCheck():
    for word in letters:
        if (os.path.isfile(f'{word}:\\main.autousb')):
            if not word in driveBlackList:
                logadd("[#]", f'[{date}]', f'main.autousb found on {word}')
                return word
                break
        continue
    else:
        logadd("[?]", f'[{date}]', "could not find main.autousb on any drive")
        quit()
