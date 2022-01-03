from utility import Utility

class Scale:
    ScaleNotes = []

    def __init__(self, rootNote):
        self.ScaleNotes = Utility.CompleteScale(rootNote)

    def ChangeScaleTo(self, newRootNote):
        self.ScaleNotes = Utility.CompleteScale(newRootNote)

    def displayScale(self):
        print(self.ScaleNotes)    