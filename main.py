from interpreter import *
from filecheck import *
from logger import *
import time

DriveLetter = fileCheck()
interpret(DriveLetter)

time.sleep(5)
