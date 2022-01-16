from interpreter import *
from filecheck import *
from logger import *

if __name__ == "__main__":
    DriveLetter = fileCheck()
    interpret(DriveLetter)
