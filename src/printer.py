DEBUG = True
FILE = True
filepath = 'out.txt'


def printer(str):
    global DEBUG
    if DEBUG:
        print('\t' + str)


def file_printer(str):
    global FILE
    print(str)
    if FILE:
        f = open(filepath, 'a')
        f.write(str)
        f.close()