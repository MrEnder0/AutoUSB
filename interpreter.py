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
        if "exit" in line:
            break
        if "run" in line:
            try:
                syntax = line.split(" ")
                syntax = letter + ":\\" + syntax[1]
                syntax = syntax.replace("\n","");
                os.startfile(syntax)
                logadd("[#]", f'[{date}]', f'launched {syntax} from drive {letter}')
                pass
            except:
                logadd("[!]", f'[{date}]', f'could not launch {syntax} from drive {letter}')
                pass
        if "log" in line:
            try:
                syntax = line
                syntax = syntax.replace("log ","");
                syntax = syntax.replace("\n","");
                logadd("[*]", f'[{date}]', f'logged "{syntax}" from drive {letter}')
                pass
            except:
                logadd("[!]", f'[{date}]', f'could not log, from drive {letter}')
                pass
        if "logclear" in line:
            logclear()
            logadd("[#]", f'[{date}]', f'the log was cleared from {letter}')
            pass
