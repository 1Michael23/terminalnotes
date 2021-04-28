import sys

list = sys.argv

del list[0]

a_file = open("notes.txt", "r")

lines = a_file.readlines()
a_file.close()

del lines[int(list[0])-1]

new_file = open("notes.txt", "w+")

for line in lines:
    new_file.write(line)

new_file.close()
