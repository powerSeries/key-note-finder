from utility import Utility

class Scale:
    ScaleNotes = []

    def __init__(self) -> None:
        pass

    # Initialize scale to start at a particular root note    
    def __init__(self, rootNote):
        self.ScaleNotes = Utility.CompleteMajorScale(rootNote)

    # Change the current scale to the new one based on the root note
    def ChangeScaleTo(self, newRootNote):
        self.ScaleNotes = Utility.CompleteMajorScale(newRootNote)

    # Display the current scale
    def DisplayScale(self):
        print(self.ScaleNotes)    