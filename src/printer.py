DEBUG = True
FILE = True
PRIORITY = 0
filepath = 'completefrechet.txt'


def printer(str):
    global DEBUG
    if DEBUG:
        print('\t' + str)


def file_printer(str, prio=1):
    global FILE
    global PRIORITY
    print(str)
    if FILE and prio >= PRIORITY:
        f = open(filepath, 'a')
        f.write(str + '\n')
        f.close()
