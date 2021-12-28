from notes import Notes

class OpenString:
    MAX_OF_NOTES = 8
    

    def __init__(self, note):
        self.Note = note

    def Initialize() -> None:
        pass
        

class Instrument:
    def __init__(self):
        self.TotalFrets = 0
        self.NumOfOpen = 0

    def __init__(self, totalFrets, numOfOpen):
        self.TotalFrets = totalFrets
        self.NumOfOpen = numOfOpen

        
    