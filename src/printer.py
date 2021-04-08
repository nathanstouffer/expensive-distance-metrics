DEBUG = True


def printer(str):
    global DEBUG
    if DEBUG:
        print('\t' + str)