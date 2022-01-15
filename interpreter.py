from datetime import date
from logger import *
import os

today = date.today()
date = today.strftime("%m/%d/%y")

def interpret(letter):
    file = open(letter + ":\\" + "Autorun.inf", "r")
    for line in file:
        if line[0] == "[":
            pass
        if line[0] == ";":
            pass
        if "run" in line:
            executeLocation1 = line.split("= ")
            executeLocation2 = letter + ":\\" + executeLocation1[1]
            executeLocation3 = executeLocation2.replace("\n","");
            os.startfile(executeLocation3)
            logadd("[#]", f'[{date}]', f'launched {executeLocation3} from drive {letter}')
