import numpy as np

def sort(elem):
    return elem[1]

# Array of notes
notes = ["c", "c#", "d", "d#", "e", "f", "f#", "g", "g#", "a", "a#", "b"]

# Load tabs
tabs = open("TabExample.txt", "r").readlines()

# collecting of significant frets
tuples = []

for tab in tabs:
    notenum = notes.index(tab[0].lower())
    for index in range(1, len(tab)-1):
        char = tab[index]
        if char.isnumeric():
            tuples.append((notenum + int(char), index))

# sorting
tuples.sort(key=sort)

# convorting frets to notes
result = ""
for tap in tuples:
    noteNum = tap[0] % 12
    result = result + notes[noteNum] + ", "

print(result[:-2])