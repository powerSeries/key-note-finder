from notes import Notes
from utility import Utility

class OpenString:
    OpenNote = ''
    AllNotes = []

    def __init__(self, note, maxFrets):
        self.OpenNote = note
        self.AllNotes = Utility.FillOpenStringNotes(note, maxFrets)
        

class Instrument:

    TotalFrets = 0
    ListOfOpenNotes = []
    AllNotes = []

    def __init__(self, totalFrets, listOfOpenNotes):
        self.TotalFrets = totalFrets
        self.ListOfOpenNotes = listOfOpenNotes

        allNotes = []
        for openNote in listOfOpenNotes:
            openString = OpenString(openNote, totalFrets)
            allNotes.append(openString)

        self.AllNotes = allNotes     



    
        
    