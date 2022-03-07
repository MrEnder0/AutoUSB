def logadd(type, date, message):
    log = open('storage/logs.log', 'a')
    log.write(f'{type} {date} {message}\n')
def logclear():
    log = open('storage/logs.log', 'w+')
    log = ""
