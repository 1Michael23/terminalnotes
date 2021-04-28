from rich import print

print('\n')

#check if notes are empty

f = open("notes.txt", "r")

if f.readline() == '':
  print('There are no notes right now.\n')
  exit()

#close and re open file to reset readline

f.close() 
f = open("notes.txt", "r")

#read out notes line by line, numbering them

number = 1  

for note in f:
  
  first = note.replace('(','[bold cyan](')
  second = first.replace(')',')[/bold cyan]')
  third = second.replace('{','[bold green]{')
  fourth = third.replace('}','}[/bold green]')
  
  output = '[bold red][%d][/bold red] '%(number) + fourth +'\n'
  print(output)
  number = number + 1

#close file again

f.close

