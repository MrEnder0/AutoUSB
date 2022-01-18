from win10toast import ToastNotifier
from datetime import date
from logger import *
import webbrowser, threading, time, os

today = date.today()
date = today.strftime("%m/%d/%y")
vars = {'autousb_version': '0.4.0', 'autousb_author': 'MrEnder'}

#prepare the file
def preinterpret(letter):
    file = open(letter + ":\\" + "main.autousb", "r")
    interpret(letter, file)

#main function
def interpret(letter, file):
    os.mkdir(letter + ":\\autousbtemp")
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
                times = replacevars(times)
                createloop(letter, command, times)
                syntax = letter + ":\\autousbtemp\\" + "loop.autousb"
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
                syntax = replacevars(syntax)
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
                syntax = replacevars(syntax)
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
                syntax = replacevars(syntax)
                logadd("[*]", f'[{date}]', f'logged "{syntax}" from drive {letter}')
                pass
            except:
                logadd("[!]", f'[{date}]', f'could not log, from drive {letter}')
                pass

        if line.startswith("logclear"):
            logclear()
            logadd("[#]", f'[{date}]', f'the log was cleared from drive {letter}')
            pass

        if line.startswith("notify"):
            try:
                syntax = line
                syntax = syntax.replace("notify ","");
                syntax = syntax.replace("\n","");
                syntax = replacevars(syntax)
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

        if line.startswith("search"):
            try:
                syntax = line
                syntax = syntax.replace("search ","");
                syntax = syntax.replace("\n","");
                syntax = replacevars(syntax)
                webbrowser.open(f'https://www.google.com/search?q={syntax}')
                pass
            except:
                logadd("[!]", f'[{date}]', f'failed to search {syntax} from drive {letter}')
                pass

        if line.startswith("setvar"):
            try:
                syntax = line
                syntax = syntax.replace("setvar ","");
                syntax = syntax.replace("\n","");
                if " = " in syntax:
                    syntaxsplit = syntax.split(" = ")
                    vars[str(syntaxsplit[0])] = str(syntaxsplit[1])
                elif " += " in syntax:
                    syntaxsplit = syntax.split(" += ")
                    syntax1 = replacevars(syntaxsplit[0])
                    syntax2 = replacevars(syntaxsplit[1])
                    vars[str(syntaxsplit[0])] = str(int(syntax1) + int(syntax2))
                elif " -= " in syntax:
                    syntaxsplit = syntax.split(" -= ")
                    syntax1 = replacevars(syntaxsplit[0])
                    syntax2 = replacevars(syntaxsplit[1])
                    vars[str(syntaxsplit[0])] = str(int(syntax1) - int(syntax2))
                elif " *= " in syntax:
                    syntaxsplit = syntax.split(" *= ")
                    syntax1 = replacevars(syntaxsplit[0])
                    syntax2 = replacevars(syntaxsplit[1])
                    vars[str(syntaxsplit[0])] = str(int(syntax1) * int(syntax2))
                elif " /= " in syntax:
                    syntaxsplit = syntax.split(" /= ")
                    syntax1 = replacevars(syntaxsplit[0])
                    syntax2 = replacevars(syntaxsplit[1])
                    vars[str(syntaxsplit[0])] = str(int(syntax1) / int(syntax2))
                else:
                    logadd("[!]", f'[{date}]', f'failed to set variable from drive {letter}')
                    pass
            except:
                logadd("[!]", f'[{date}]', f'failed to set variable {syntax} from drive {letter}')
                pass

        if line.startswith("delvar"):
            try:
                syntax = line
                syntax = syntax.replace("delvar ","");
                syntax = syntax.replace("\n","");
                syntaxsplit = syntax.split(" = ")
                name = syntaxsplit[0]
                #delete from dictionary
                del vars[name]
            except:
                logadd("[!]", f'[{date}]', f'failed to delete variable {syntax} from drive {letter}')
                pass

#part of loop code
def createloop(letter, command, times):
    try:
        loopcommands = open(letter + ":\\autousbtemp\\" + "loop.autousb", "w")
        timeswritten = 0

        while int(times) > timeswritten:
            loopcommands.write(f'{command}\n')
            timeswritten += 1
    except:
        logadd("[!]", f'[{date}]', f'failed to create loop from drive {letter}')
        pass

#part of varible code
def replacevars(input):
    for keyword, value in vars.items():
        if keyword in input:
            input = input.replace(keyword, value)
    return input
