#settings

location = '/home/sl3/notes.txt'

#imports

from rich import print
import sys

#save arguments to variable 

inputarguments = sys.argv

del inputarguments[0]



#function to convert to string

def instantStringage(inputarguments):
    string = ''
    for object in inputarguments:
        if object == inputarguments[0]:
            pass
        string += object+' '
    return string

#function to add a note

if sys.argv[0] == 'addnote':
    note = (instantStringage(inputarguments))

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
        print('\nAdding Note.')
        f = open(location, 'a')
        f.write(note + '\n')
        f.close

#function to remove a note

if sys.argv[0] == 'rmnote':
    a_file = open(location, "r")
    lines = a_file.readlines()
    a_file.close()
    del lines[int(inputarguments[1])-1]
    new_file = open("/home/sl3/notes.txt", "w+")
    for line in lines:
        new_file.write(line)
    new_file.close()

#function to list notes

if sys.argv[0] == 'lsnotes':
    print('\n')
    f = open(location, "r")
    
    if f.readline() == '':
        print('There are no notes right now.\n')
        exit()

    f.close() #needed to reset the line python is reading
    f = open(location, "r")

    number = 1  

    for note in f:
    
        first = note.replace('(','[bold cyan](')
        second = first.replace(')',')[/bold cyan]')
        third = second.replace('{','[bold green]{')
        fourth = third.replace('}','}[/bold green]')
        
        output = '[bold red][%d][/bold red] '%(number) + fourth +'\n'
        print(output)
        number = number + 1

else:
    print('\n[bold red]Invalid command[/bold red]\n')

