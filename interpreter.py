from win10toast import ToastNotifier; from playsound import playsound; from datetime import date; from logger import *; from config import *
import webbrowser, threading, random, time, os, sys

today = date.today()
date = today.strftime("%m/%d/%y")
vars = {'autousb_version': '1.0.2', 'autousb_release_type': 's', 'autousb_author': 'Team Codingo', 'date_today': today, 'π': '3.1415926535', 'num_pi': '3.1415926535', 'num_e': '2.7182818284', 'num_inf': '9999999999999999999999999'}

#prepare the file
def preinterpret(letter):
    file = open(letter + ":\\" + "main.autousb", "r")
    interpret(letter, file)

#main function
def interpret(letter, file):
    if not os.path.exists(letter + ":\\autousbtemp"):
        os.makedirs(letter + ":\\autousbtemp")
        os.system("attrib +h " + letter + ":\\autousbtemp")
    if not os.path.exists(letter + ":\\autousbdata"):
        os.makedirs(letter + ":\\autousbdata")
        os.system("attrib +h " + letter + ":\\autousbdata")

    for line in file:
        if line.startswith(";"):
            continue

        if line.startswith("exit"):
            break

        if line.startswith("help"):
            try:
                syntax = line
                syntax = syntax.replace("help", "")
                syntax = syntax.replace("\n", "")
                if command == ";": print("To comment put ; at the begining of the line this can help orginize your autousb scripts code.")
                elif command == "comments": print("To comment put ; at the begining of the line this can help orginize your autousb scripts code.")
                elif command == "exit": print("To exit the interpreter type exit.")
                elif command == "loop": print("This i used to loop code in your programs to use put loop (times) then put || then your commands if multiple put | inbetween each one.")
                elif command == "if": print("This is used to check if a condition is true or false if it is put if (condition) then put || then your commands if multiple put | inbetween each one.")
                elif command == "setvar": print("This is used to set a variable to a value, to use put setvar (variable) (value), This can be used in almost any command that excepts arguments.")
                elif command == "delvar": print("This is used to delete a variable, to use put delvar (variable).")
                elif command == "wait": print("This is used to wait for a certain amount of time, to use put wait (time).")
                elif command == "run": print("This is used to run a programs, python, or other AutoUSB scripts, to use put run (program). Also if you want to run python put the word python before the python code.")
                elif command == "close": print("This is used to close a program, to use put close (program).")
                elif command == "log": print("This is used to log a message, to use put log (message). This is very helpful for debugging your scripts.")
                elif command == "logclear": print("This is a way to automatically clear logs so you dont have to.")
                elif command == "notify": print("This is used to send a notification to your desktop, to use put notify (message) | (time limit). Also if your using this command inside a statement or loop then use *timed instead of | .")
                elif command == "text": print("This is used to edit text documents on your pc, to use put text (action) (file) (text).")
                elif command == "search": print("This is used to search on your webbrowser.")
                elif command == "math": print("You can do basic math like + - * / % with the setvar command you also have access to pi and e. These 2 numbers can be used by using num_pi or num_e")
                elif command == "examples": print("If you would like some example scripts made check the storage folder inside the AutoUSB dir and open the examples folder this may help beginners learn how to use AutoUSB and some of its use cases.")
                elif command == "about": print(f'AutoUSB version {vars["autousb_version"]}AutoUSB release type {vars["autousb_release_type"]} by {vars["autousb_author"]}')
                elif command == "AutoUSB mk2": print(f'AutoUSB mk2 is the more optimized version of AutoUSB, it is the same as AutoUSB but with a lot of improvements and bug fixes. AutoUSB mk2 is not compatible with AutoUSB mk1. Also AutoUSB mk2 is made for sbc and not for pendrives/flashdrives.')
                else: print("Hmm looks like your not sure what you can put into this command. To help use any of these commands: ;, comments, exit, loop, if, setvar, delvar, wait, run, close, log, logclear, notify, text, search, examples. Hope this helps.")
            except:
                logadd("[!]", f'[{date}]', f'failed to help like that must really suck :/ {letter}')
                pass

        if line.startswith("loop"):
            try:
                syntax = line
                syntax = syntax.replace("loop ","")
                syntax = syntax.replace("\n","")
                syntaxsplit = syntax.split(" || ")
                command = str(syntaxsplit[1])
                times = str(syntaxsplit[0])
                times = replacevars(times)
                if "random " in times:
                    times = times.replace("random ","")
                    times = times.split(" to ")
                    min = times[0]
                    max = times[1]
                    times = random.randint(int(min), int(max))
                createloop(letter, command, times)
                syntax = letter + ":\\autousbtemp\\" + "loop.autousb"
                time.sleep(0.2)
                loopthread = threading.Thread(target=interpret(letter, open(syntax, "r"))).start()
                while loopthread.is_alive():
                    pass
                continue
            except:
                logadd("[!]", f'[{date}]', "syntax error in loop")
                continue

        if line.startswith("if"):
            try:
                syntax = line
                syntax = syntax.replace("if ","")
                syntax = syntax.replace("\n","")
                syntaxsplit = syntax.split(" || ")
                condition = syntaxsplit[0]
                condition = replacevars(condition)
                command = syntaxsplit[1]
                if " = " in condition:
                    syntaxsplit = condition.split(" = ")
                    if syntaxsplit[0] == syntaxsplit[1]:
                        createif(letter, command)
                        syntax = letter + ":\\autousbtemp\\" + "if.autousb"
                        time.sleep(0.2)
                        ifthread = threading.Thread(target=interpret(letter, open(syntax, "r"))).start()
                        while ifthread.is_alive():
                            pass
                        continue
                elif " != " in condition:
                    syntaxsplit = condition.split(" != ")
                    if syntaxsplit[0] != syntaxsplit[1]:
                        createif(letter, command)
                        syntax = letter + ":\\autousbtemp\\" + "if.autousb"
                        time.sleep(0.2)
                        ifthread = threading.Thread(target=interpret(letter, open(syntax, "r"))).start()
                        while ifthread.is_alive():
                            pass
                        continue
                elif " > " in condition:
                    syntaxsplit = condition.split(" > ")
                    if int(syntaxsplit[0]) > int(syntaxsplit[1]):
                        createif(letter, command)
                        syntax = letter + ":\\autousbtemp\\" + "if.autousb"
                        time.sleep(0.2)
                        ifthread = threading.Thread(target=interpret(letter, open(syntax, "r"))).start()
                        while ifthread.is_alive():
                            pass
                        continue
                elif " < " in condition:
                    syntaxsplit = condition.split(" < ")
                    if int(syntaxsplit[0]) < int(syntaxsplit[1]):
                        createif(letter, command)
                        syntax = letter + ":\\autousbtemp\\" + "if.autousb"
                        time.sleep(0.2)
                        ifthread = threading.Thread(target=interpret(letter, open(syntax, "r"))).start()
                        while ifthread.is_alive():
                            pass
                        continue
                elif " >= " in condition:
                    syntaxsplit = condition.split(" >= ")
                    if int(syntaxsplit[0]) >= int(syntaxsplit[1]):
                        createif(letter, command)
                        syntax = letter + ":\\autousbtemp\\" + "if.autousb"
                        time.sleep(0.2)
                        ifthread = threading.Thread(target=interpret(letter, open(syntax, "r"))).start()
                        while ifthread.is_alive():
                            pass
                        continue
                elif " <= " in condition:
                    syntaxsplit = condition.split(" <= ")
                    if int(syntaxsplit[0]) <= int(syntaxsplit[1]):
                        createif(letter, command)
                        syntax = letter + ":\\autousbtemp\\" + "if.autousb"
                        time.sleep(0.2)
                        ifthread = threading.Thread(target=interpret(letter, open(syntax, "r"))).start()
                        while ifthread.is_alive():
                            pass
                        continue
                elif " contains " in condition:
                    syntaxsplit = condition.split(" contains ")
                    if syntaxsplit[1] in syntaxsplit[0]:
                        createif(letter, command)
                        syntax = letter + ":\\autousbtemp\\" + "if.autousb"
                        time.sleep(0.2)
                        ifthread = threading.Thread(target=interpret(letter, open(syntax, "r"))).start()
                        while ifthread.is_alive():
                            pass
                        continue
                else:
                    logadd("[!]", f'[{date}]', f'invalid if statement from drive {letter}')
                    continue
            except:
                logadd("[!]", f'[{date}]', f'failed to create if from drive {letter}')
                continue

        if line.startswith("setvar"):
            try:
                syntax = line
                syntax = syntax.replace("setvar ","")
                syntax = syntax.replace("\n","")
                if " = " in syntax:
                    syntaxsplit = syntax.split(" = ")
                    vars[str(syntaxsplit[0])] = str(syntaxsplit[1])
                    continue
                elif " += " in syntax:
                    syntaxsplit = syntax.split(" += ")
                    syntax1 = replacevars(syntaxsplit[0])
                    syntax2 = replacevars(syntaxsplit[1])
                    vars[str(syntaxsplit[0])] = str(int(syntax1) + int(syntax2))
                    continue
                elif " -= " in syntax:
                    syntaxsplit = syntax.split(" -= ")
                    syntax1 = replacevars(syntaxsplit[0])
                    syntax2 = replacevars(syntaxsplit[1])
                    vars[str(syntaxsplit[0])] = str(int(syntax1) - int(syntax2))
                    continue
                elif " *= " in syntax:
                    syntaxsplit = syntax.split(" *= ")
                    syntax1 = replacevars(syntaxsplit[0])
                    syntax2 = replacevars(syntaxsplit[1])
                    vars[str(syntaxsplit[0])] = str(int(syntax1) * int(syntax2))
                    continue
                elif " /= " in syntax:
                    syntaxsplit = syntax.split(" /= ")
                    syntax1 = replacevars(syntaxsplit[0])
                    syntax2 = replacevars(syntaxsplit[1])
                    vars[str(syntaxsplit[0])] = str(int(syntax1) / int(syntax2))
                    continue
                elif " %= " in syntax:
                    syntaxsplit = syntax.split(" %= ")
                    syntax1 = replacevars(syntaxsplit[0])
                    syntax2 = replacevars(syntaxsplit[1])
                    vars[str(syntaxsplit[0])] = str(int(syntax1) % int(syntax2))
                    continue
                elif " random " in syntax:
                    syntaxsplit = syntax.split(" random ")
                    var = syntaxsplit[0]
                    syntaxsplit = str(syntaxsplit[1]).split(" to ")
                    syntax1 = replacevars(syntaxsplit[0])
                    syntax2 = replacevars(syntaxsplit[1])
                    vars[str(var)] = str(random.randint(int(syntax1), int(syntax2)))
                    continue
                elif " round " in syntax:
                    syntaxsplit = syntax.split(" round ")
                    var =  syntaxsplit[0]
                    value = replacevars(syntaxsplit[1])
                    vars[str(var)] = str(round(float(value)))
                    continue
                elif " join " in syntax:
                    syntaxsplit = syntax.split(" join ")
                    var = replacevars(syntaxsplit[0])
                    syntax2 = replacevars(syntaxsplit[1])
                    vars[str(var)] = str(syntax1) + str(syntax2)
                    continue
                elif " file " in syntax:
                    syntaxsplit = syntax.split(" file ")
                    var = replacevars(syntaxsplit[0])
                    syntax2 = replacevars(letter + ":\\" + syntaxsplit[1])
                    vars[str(var)] = str(open(syntax2, "r").read())
                    continue
                elif " length " in syntax:
                    syntaxsplit = syntax.split(" length ")
                    syntax1 = replacevars(syntaxsplit[0])
                    vars[str(syntax1)] = str(len(syntax1))
                    continue
                elif " lower " in syntax:
                    syntaxsplit = syntax.split(" lower ")
                    syntax1 = replacevars(syntaxsplit[0])
                    vars[str(syntax1)] = str(syntax1.lower())
                    continue
                elif " upper " in syntax:
                    syntaxsplit = syntax.split(" upper ")
                    syntax1 = replacevars(syntaxsplit[0])
                    vars[str(syntax1)] = str(syntax1.upper())
                    continue
                elif " replace " in syntax:
                    syntaxsplit = syntax.split(" replace ")
                    name = replacevars(syntaxsplit[0])
                    value = replacevars(syntaxsplit[1])
                    oldValue = value.split(" with ")[0]
                    newValue = value.split(" with ")[1]
                    vars[str(name)] = str(name.replace(oldValue, newValue))
                    continue
                else:
                    logadd("[!]", f'[{date}]', f'failed to set variable from drive {letter}')
                    continue
            except:
                logadd("[!]", f'[{date}]', f'failed to set variable {syntax} from drive {letter}')
                continue

        if line.startswith("delvar"):
            try:
                syntax = line
                syntax = syntax.replace("delvar ","")
                syntax = syntax.replace("\n","")
                syntaxsplit = syntax.split(" = ")
                name = syntaxsplit[0]
                del vars[name]
                continue
            except:
                logadd("[!]", f'[{date}]', f'failed to delete variable {syntax} from drive {letter}')
                continue

        if line.startswith("wait"):
            try:
                syntax = line
                syntax = syntax.replace("wait ","")
                syntax = syntax.replace("\n","")
                syntax = replacevars(syntax)
                syntax = int(syntax)
                time.sleep(syntax)
                continue
            except:
                logadd("[!]", f'[{date}]', f'failed to wait {syntax} from drive {letter}')
                continue

        if line.startswith("run"):
            try:
                syntax = line.replace("run ","")
                syntax = syntax.replace("\n","")
                syntax = letter + ":\\" + syntax
                syntax = replacevars(syntax)
                if ".autousb" in line:
                    thread = threading.Thread(target=interpret(letter, open(syntax, "r"))).start()
                    while thread.is_alive():
                        pass
                    continue
                elif " python " in line:
                    if allowPython:
                        syntax = syntax.strip(f'{letter}:\\')
                        syntax = syntax.replace("python ","")
                        exec(syntax)
                    else:
                        logadd("[!]", f'[{date}]', f'please enable allowPython in settings.py')
                    continue
                    
                else:
                    if allowProgramExecution == True:
                        os.startfile(syntax)
                        logadd("[#]", f'[{date}]', f'launched {syntax} from drive {letter}')
                    else:
                        logadd("[!]", f'[{date}]', f'please enable allowProgramExecution in settings.py')
                    continue
            except:
                logadd("[!]", f'[{date}]', f'could not launch {syntax} from drive {letter}')
                continue

        if line.startswith("close"):
            try:
                syntax = line
                syntax = syntax.replace("close ","")
                syntax = syntax.replace("\n","")
                syntax = replacevars(syntax)
                syntax = int(syntax)
                sys.exit(syntax)
                continue
            except:
                logadd("[!]", f'[{date}]', f'failed to close program {syntax} from drive {letter}')
                continue

        if line.startswith("sound"):
            try:
                syntax = line
                syntax = syntax.replace("sound ","")
                syntax = syntax.replace("\n","")
                syntax = replacevars(syntax)
                playsound(letter + ":\\" + syntax)
                continue
            except:
                logadd("[!]", f'[{date}]', f'failed to play sound at {syntax} from drive {letter}')
                continue

        if line.startswith("text"):
            if allowFileEditing:
                try:
                    syntax = line
                    syntax = syntax.replace("text ","")
                    syntax = syntax.replace("\n","")
                    syntax = replacevars(syntax)
                    if " *file " in syntax:
                        syntaxsplit = syntax.split(" *file ")
                    else:
                        syntaxsplit = syntax.split(" | ")
                    if "create " in syntax:
                        syntax = syntax.replace("create ","")
                        path = letter + "://" + syntax
                        with open(path, "w") as file:
                            file.write("")
                    if "append " in syntax:
                        data = str(syntaxsplit[0]).replace("append ","")
                        path = letter + "://" + syntaxsplit[1]
                        with open(path, "a") as file:
                            file.write(data + "\n")
                    if "rename " in syntax:
                        original = str(syntaxsplit[0]).replace("rename ","")
                        originalPath = letter + "://" + original
                        os.rename(originalPath, letter + "://" + syntaxsplit[1])
                    if "delete " in syntax:
                        syntax = syntax.replace("delete ","")
                        path = letter + "://" + syntax
                        os.remove(path)
                    continue
                except:
                    logadd("[!]", f'[{date}]', f'failed to edit file on {letter}')
                    continue

        if line.startswith("notify"):
            try:
                syntax = line
                syntax = syntax.replace("notify ","")
                syntax = syntax.replace("\n","")
                syntax = replacevars(syntax)
                if " *timed " in syntax:
                    syntax = syntax.split(" *timed ")
                    toaster = ToastNotifier()
                    toaster.show_toast("AutoUSB Project", f"{str(syntax[0])}", duration=int(syntax[1]), threaded=True)
                    continue
                elif " | " in syntax:
                    syntax = syntax.split(" | ")
                    toaster = ToastNotifier()
                    toaster.show_toast("AutoUSB Project", f"{str(syntax[0])}", duration=int(syntax[1]), threaded=True)
                else:
                    toaster = ToastNotifier()
                    toaster.show_toast("AutoUSB Project", f"{syntax}", threaded=True)
                    continue    
            except:
                logadd("[!]", f'[{date}]', f'failed to display notification from drive {letter}')
                continue

        if line.startswith("log"):
            try:
                syntax = line
                syntax = syntax.replace("log ","")
                syntax = syntax.replace("\n","")
                syntax = replacevars(syntax)
                logadd("[*]", f'[{date}]', f'logged "{syntax}" from drive {letter}')
                continue
            except:
                logadd("[!]", f'[{date}]', f'could not log, from drive {letter}')
                continue

        if line.startswith("logclear"):
            if allowLogClearing == True:
                logclear()
                logadd("[#]", f'[{date}]', f'the log was cleared from drive {letter}')
            continue

        if line.startswith("search"):
            try:
                syntax = line
                syntax = syntax.replace("search ","")
                syntax = syntax.replace("\n","")
                syntax = replacevars(syntax)
                webbrowser.open(f'https://www.google.com/search?q={syntax}')
                continue
            except:
                logadd("[!]", f'[{date}]', f'failed to search {syntax} from drive {letter}')
                continue

#part of loop code
def createloop(letter, command, times):
    try:
        loopcommands = open(letter + ":\\autousbtemp\\" + "loop.autousb", "w")
        commands = command.split(" | ")
        timeswritten = 0

        while int(times) > timeswritten:
            for command in commands:
                loopcommands.write(f'{command}\n')
            timeswritten += 1
        
    except:
        logadd("[!]", f'[{date}]', f'failed to create loop from drive {letter}')

#part of if code
def createif(letter, command):
    try:
        ifcommands = open(letter + ":\\autousbtemp\\" + "if.autousb", "w")
        commands = command.split(" | ")
        for command in commands:
            ifcommands.write(command + '\n')
    except:
        logadd("[!]", f'[{date}]', f'failed to create if from drive {letter}')
        pass

#part of varible code
def replacevars(input):
    for keyword, value in vars.items():
        if keyword in input:
            input = input.replace(keyword, value)
    return input
