from interpreter import *
from filecheck import *
from logger import *
from config import *
import shutil

if __name__ == "__main__":
    DriveLetter = fileCheck()
    preinterpret(DriveLetter)

    if autoRemoveTempFiles:
        try:
            shutil.rmtree(f'{DriveLetter}:\\autousbtemp')
        except:
            pass
