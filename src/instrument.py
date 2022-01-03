from notes import Notes
from utility import Utility

class OpenString:
    OpenNote = ''
    AllNotes = []

    def __init__(self, note, maxFrets):
        self.OpenNote = note
        self.AllNotes = Utility.FillOpenStringNotes(note, maxFrets)

    def displayAllNotes(self):
        print(self.AllNotes)
        

class Instrument:

    TotalFrets = 0
    ListOfOpenNotes = []
    AllStringNotes = []

    def __init__(self, totalFrets, listOfOpenNotes):
        self.TotalFrets = totalFrets
        self.ListOfOpenNotes = listOfOpenNotes

        allNotes = []
        for openNote in listOfOpenNotes:
            openString = OpenString(openNote, totalFrets)
            allNotes.append(openString)

        self.AllStringNotes = allNotes     


    def ShowAllNotes(self):
        for stringNotes in self.AllStringNotes:
            stringNotes.displayAllNotes()

    def ShowOpenStringNotes(self, openNote):
        openNoteIndex = self.ListOfOpenNotes.index(openNote)
        self.AllStringNotes[openNoteIndex].displayAllNotes()

    
        
    