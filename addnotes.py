import sys

list = sys.argv

del list[0]

def instantStringage(list):
    string = ''
    for object in list:
        string += object+' '
    return string

note = instantStringage(list)[:-1]

def confirmation():
    while "the answer is invalid":
        reply = str(input('\n"'+note+'"\n\nIs this note correct? (Y/n): ')).lower().strip()
        if reply[:1] == 'y':
            return True
        if reply[:1] == 'n':
            return False
        if reply == '':
            return True


if confirmation() == True:
    print('\nAdding note.')

    f = open("notes.txt", "a")
    f.write(note+'\n')
    f.close()   

