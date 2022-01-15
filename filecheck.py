from logger import *
import os

letters = ["D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

def fileCheck():
    for word in letters:
        if (os.path.isfile(f'{word}:\\Autorun.inf')):
            print(f'Autorun.inf found on {word}')
            return word
            break
        continue
    else:
        print("Autorun.inf not found")
        #logadd("?", '{date}', "could not find Autorun.inf on any drive")
