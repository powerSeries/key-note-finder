from utility import Utility

class Scale:
    ScaleNotes = []
    ALL_MAJOR_SCALE = ['C', 'G', 'D', 'A', 'E', 'B', 'F#', 'C#']
    Root = ''

    def __init__(self) -> None:
        pass

    # Initialize scale to start at a particular root note    
    def __init__(self, rootNote):
        self.Root = rootNote
        self.ScaleNotes = Utility.CompleteMajorScale(rootNote)

    # Change the current scale to the new one based on the root note
    def ChangeScaleTo(self, newRootNote):
        if newRootNote == self.Root:
            return
        else:
            self.ScaleNotes = Utility.CompleteMajorScale(newRootNote)
            self.Root = newRootNote
            return

    # Display the current scale
    def DisplayScale(self):
        print(self.ScaleNotes)    

    def DisplayAllMajorScales(self) -> None:
        count = 0
        for majorScale in Scale.ALL_MAJOR_SCALE:
            print(majorScale + " major"),
        pass