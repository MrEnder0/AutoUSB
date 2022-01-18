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
        if line.startswith(";"):
            pass

        if line.startswith("exit"):
            break
    
        if line.startswith("loop"):
            try:
                syntax = line
                syntax = syntax.replace("loop ","");
                syntax = syntax.replace("\n","");
                syntaxsplit = syntax.split(" || ")
                command = str(syntaxsplit[1])
                times = str(syntaxsplit[0])
                createloop(letter, command, times)
                syntax = letter + ":\\autousb\\" + "loop.autousb"
                time.sleep(0.5)
                loopthread = threading.Thread(target=interpret(letter, open(syntax, "r"))).start()
                pass
            except:
                logadd("[!]", f'[{date}]', "syntax error in loop")
                pass

        if line.startswith("wait"):
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

        if line.startswith("run"):
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

        if line.startswith("log"):
            try:
                syntax = line
                syntax = syntax.replace("log ","");
                syntax = syntax.replace("\n","");
                logadd("[*]", f'[{date}]', f'logged "{syntax}" from drive {letter}')
                pass
            except:
                logadd("[!]", f'[{date}]', f'could not log, from drive {letter}')
                pass

        if line.startswith("logclear"):
            logclear()
            logadd("[#]", f'[{date}]', f'the log was cleared from {letter}')
            pass

        if line.startswith("notify"):
            try:
                syntax = line
                syntax = syntax.replace("notify ","");
                syntax = syntax.replace("\n","");
                try:
                    syntaxtimed = syntax.split(" || ")
                    toaster = ToastNotifier()
                    toaster.show_toast("AutoUSB Project", f"{str(syntaxtimed[0])}", duration=str(syntaxtimed[1]), threaded=True)
                    pass
                except:
                    toaster = ToastNotifier()
                    toaster.show_toast("AutoUSB Project", f"{syntax}", threaded=True)
                    pass    
            except:
                logadd("[!]", f'[{date}]', f'failed to display notification from drive {letter}')
                pass

def createloop(letter, command, times):
    try:
        loopcommands = open(letter + ":\\autousb\\" + "loop.autousb", "w")
        timeswritten = 0

        while int(times) > timeswritten:
            loopcommands.write(f'{command}\n')
            timeswritten += 1
    except:
        logadd("[!]", f'[{date}]', f'failed to create loop from drive {letter}')
        pass
