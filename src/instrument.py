# import packages
from utility import Utility

class OpenString:
    # Class variables
    OpenNote = ''
    AllNotes = []
    AllKeyNotes = []
    MAX_FRETS = 0

    # Initialize the open string with all notes the string can play
    # from 0 to MAX fret number
    def __init__(self, note, maxFrets):
        self.OpenNote = note
        self.MAX_FRETS = maxFrets
        self.AllNotes = Utility.FillOpenStringNotes(note, maxFrets)

    # Change the open string to the new note and find all its notes
    def ChangeOpenStringNotes(self, newNote):
        self.OpenNote = newNote
        self.AllNotes = Utility.FillOpenStringNotes(newNote, self.MAX_FRETS)

    # Creates a list of the location of all the notes in key
    def InitializeKeyNotes(self, scaleNotes):
        self.AllKeyNotes = []
        count = 0
        for i in range(len(self.AllNotes)):
            if self.AllNotes[i] in scaleNotes:
                self.AllKeyNotes.append(str(count))
            else:
                self.AllKeyNotes.append('-')
            
            count += 1

    # Display all the notes for the particular OpenString
    def displayAllNotes(self):
        print(self.AllNotes)
        
    # Display all the notes found that are in key
    def displayAllKeyNotes(self):
        print(self.AllKeyNotes)

class Instrument:
    # Class variables
    TotalFrets = 0
    ListOfOpenNotes = []
    AllStringNotes = []

    # Initialize the instrument object with the total number of frets
    # the instrument has. Also with a list of all the open notes it
    # then fills up an array show what note is on what string at X
    # location.
    def __init__(self, totalFrets, listOfOpenNotes):
        self.TotalFrets = totalFrets
        self.ListOfOpenNotes = listOfOpenNotes

        # Found all the notes
        allNotes = []
        for openNote in listOfOpenNotes:
            openString = OpenString(openNote, totalFrets)
            allNotes.append(openString)

        self.AllStringNotes = allNotes

    # Able to change the instruments open strings
    def ChangeOpenStringTo(self, changeNote, newNote):
        changeNoteIndex = self.ListOfOpenNotes.index(changeNote)
        self.ListOfOpenNotes[changeNoteIndex] = newNote

        self.AllStringNotes[changeNoteIndex].ChangeOpenStringNotes(newNote)
        pass
    
    # Finds the position of all the notes that are in key
    def FindKeyNotes(self, scaleNotes) -> None:    
        self.AllKeyNotes = self.AllStringNotes

        for openString in self.AllKeyNotes:
            openString.InitializeKeyNotes(scaleNotes)

    # Shows all the notes that the instrument has available
    def ShowAllNotes(self):
        for stringNotes in self.AllStringNotes:
            stringNotes.displayAllNotes()

    # Shows all the notes that the instrument will be in key with
    def ShowAllKeyNotes(self):
        for keyNotes in self.AllKeyNotes:
            keyNotes.displayAllKeyNotes()

    # Shows all the notes of a particular OpenString
    def ShowOpenStringNotes(self, openNote):
        openNoteIndex = self.ListOfOpenNotes.index(openNote)
        self.AllStringNotes[openNoteIndex].displayAllNotes()

    # Shows all the open strings the instrument has
    def ShowOpenStrings(self) -> None:
        print(self.ListOfOpenNotes)

    
        
    