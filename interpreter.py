from win10toast import ToastNotifier
from datetime import date
from logger import *
import threading, time, os

today = date.today()
date = today.strftime("%m/%d/%y")

def preinterpret(letter):
    file = open(letter + ":\\" + "main.autousb", "r")
    interpret(letter, file)

def interpret(letter, file):
    for line in file:
        if line[0] == ";":
            pass

        if "exit" in line:
            break

        if "run" in line:
            try:
                syntax = line.split(" ")
                syntax = letter + ":\\" + syntax[1]
                syntax = syntax.replace("\n","");
                if ".autousb" in line:
                    thread = threading.Thread(target=interpret(letter, open(syntax, "r"))).start()
                    pass
                else:
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

        if "notify" in line:
            try:
                syntax = line
                syntax = syntax.replace("notify ","");
                syntax = syntax.replace("\n","");
                #might add customizable duration in future
                #syntax = syntax.split("||")
                toaster = ToastNotifier()
                toaster.show_toast("AutoUSB Project", f"{syntax}", duration=5, threaded=True)
                pass
            except:
                logadd("[!]", f'[{date}]', f'failed to display notification from drive {letter}')
                pass
            
        if "wait" in line:
            try:
                syntax = line
                syntax = syntax.replace("wait ","");
                syntax = syntax.replace("\n","");
                syntax = int(syntax)
                time.sleep(syntax)
                pass
            except:
                logadd("[!]", f'[{date}]', f'failed to wait {syntax} from drive {letter}')
                pass
