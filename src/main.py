# import packages
from instrument import Instrument, OpenString
from notes import Notes
from utility import Utility

# Ask the user to input the number of frets their instruments has
maxFretCount = input("Enter the max fret your instrument can go: ")

Utility.ValidateAsInteger(maxFretCount)

# Ask the user to input what open string it has
maxNumOfOpenStrings = input("Enter the number of open strings your instrument has: ")

Utility.ValidateAsInteger(maxNumOfOpenStrings)

# Ask the user to list the note of each open string.
# From lowest - highest
listOfNotes = []

print("List the notes from A - G lowest to highest in sound")
for i in range(0, int(maxNumOfOpenStrings)):
    temp = input()

    listOfNotes.append(temp)

mainInst = Instrument(maxFretCount, listOfNotes)

mainInst.ShowAllNotes()
mainInst.ShowOpenStringNotes('E')

    