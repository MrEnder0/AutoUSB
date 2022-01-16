from datetime import date
from logger import *
import os

today = date.today()
date = today.strftime("%m/%d/%y")

def interpret(letter):
    file = open(letter + ":\\" + "Autorun.infp", "r")
    for line in file:
        if line[0] == "[":
            pass
        if line[0] == ";":
            pass
        if "run" in line:
            try:
                executeLocation = line.split(" ")
                executeLocation = letter + ":\\" + executeLocation[1]
                executeLocation = executeLocation.replace("\n","");
                os.startfile(executeLocation)
                logadd("[#]", f'[{date}]', f'launched {executeLocation} from drive {letter}')
                pass
            except:
                logadd("[!]", f'[{date}]', f'could not launch {executeLocation} from drive {letter}')
                pass
        if "log" in line:
            try:
                logtext = line
                logtext = logtext.replace("log ","");
                logtext = logtext.replace("\n","");
                logadd("[*]", f'[{date}]', f'logged "{logtext}" from drive {letter}')
                pass
            except:
                logadd("[!]", f'[{date}]', f'could not log from drive {letter}')
                pass
