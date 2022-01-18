from interpreter import *
from filecheck import *
from logger import *
import shutil

if __name__ == "__main__":
    DriveLetter = fileCheck()
    preinterpret(DriveLetter)

    try:
        shutil.rmtree(f'{DriveLetter}:\\autousbtemp')
    except:
        pass
