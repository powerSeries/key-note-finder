# import packages
from notes import Notes
from utility import Utility

class OpenString:
    # Class variables
    OpenNote = ''
    AllNotes = []
    MAX_FRETS = 0

    # Initialize the open string with all notes the string can play
    # from 0 to MAX fret number
    def __init__(self, note, maxFrets):
        self.OpenNote = note
        self.MAX_FRETS = maxFrets
        self.AllNotes = Utility.FillOpenStringNotes(note, maxFrets)

    def ChangeOpenStringNotes(self, newNote):
        self.OpenNote = newNote
        self.AllNotes = Utility.FillOpenStringNotes(newNote, self.MAX_FRETS)


    # Display all the notes for the particular OpenString
    def displayAllNotes(self):
        print(self.AllNotes)
        

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

    def ChangeOpenStringTo(self, changeNote, newNote):
        changeNoteIndex = self.ListOfOpenNotes.index(changeNote)
        self.ListOfOpenNotes[changeNoteIndex] = newNote

        self.AllStringNotes[changeNoteIndex].ChangeOpenStringNotes(newNote)

        pass


    # Shows all the notes that the instrument has available
    def ShowAllNotes(self):
        for stringNotes in self.AllStringNotes:
            stringNotes.displayAllNotes()

    # Shows all the notes of a particular OpenString
    def ShowOpenStringNotes(self, openNote):
        openNoteIndex = self.ListOfOpenNotes.index(openNote)
        self.AllStringNotes[openNoteIndex].displayAllNotes()

    def ShowOpenStrings(self) -> None:
        print(self.ListOfOpenNotes)

    
        
    