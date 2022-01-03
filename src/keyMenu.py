from instrument import Instrument
from scale import Scale
from utility import Utility
from error import Error

class KeyMenu:
    # Class variables
    option = 0
    selectKey = ''
    
    def __init__(self) -> None:
        print("Welcome to KNF....")

        while(self.option != 5):
            self.InitializeMenu()

            if(self.option == 1):
                # Initialize instrument
                self.InitializeInstrument()
                pass
            elif(self.option == 2):
                # Select the key
                self.InitializeScale()
                pass
            elif(self.option == 3):
                # Change open strings
                self.ChangeOpenStrings()
                pass
            elif(self.option == 4):
                # Display 
                self.KeyNoteFinder()
                pass
            elif(self.option == 5):
                print("Goodbye...")
                break
        

    def InitializeMenu(self) -> None:
        print("[1] - Initialize instrument.")
        print("[2] - Select the key.")
        print("[3] - Change open strings.")
        print("[4] - Display notes location.")
        print("[5] - Exit")

        print()
        self.option = int(input("Enter your option: "))    
    
    def InitializeInstrument(self) -> None:
        # Ask the user to input the number of frets their instruments has
        maxFretCount = input("Enter the max fret your instrument can go: ")
        Utility.ValidateAsInteger(maxFretCount)

        # Ask the user to input what open string it has
        maxNumOfOpenStrings = input("Enter the number of open strings your instrument has: ")
        Utility.ValidateAsInteger(maxNumOfOpenStrings)

        # Ask the user to list the note of each open string.
        # From lowest - highest
        listOfNotes = []
        print("List the notes from A - G lowest to highest in sound.")
        for i in range(0, int(maxNumOfOpenStrings)):
            temp = input()
            listOfNotes.append(temp)

        # Create the instruments the user wants.
        self.Instrument = Instrument(maxFretCount, listOfNotes)

        print("Instrument has been initialized.........!")

    def InitializeScale(self) -> None:
        # initialize Scale
        self.Key = Scale('C')

        # Display the major keys available
        print("Choose from the following keys.")
        self.Key.DisplayAllMajorScales()

        # Ask the user to choose a key
        self.selectKey = input("Select your key: ")
        self.Key.ChangeScaleTo(self.selectKey)
        
        print("Key has been selected........!")

    def ChangeOpenStrings(self) -> None:
        if self.Instrument is None:
            print("Intrument has not been created, please create a new one.")
            return

        self.Instrument.ShowOpenStrings()
        
        # taking multiple inputs at a time
        changeOpen = [str(changeOpen) for changeOpen in input("Enter open strings you want to change: ").split()]
        
        print()
        print("List of all possible notes")
        print(Utility.OrderOfNotes)
        for open in changeOpen:
            newNote = input("Change " + open + " to: ")
            self.Instrument.ChangeOpenStringTo(open, newNote)
        print("Open strings have been changed.")
        print("These are the following new Open Strings")
        self.Instrument.ShowOpenStrings()

    def KeyNoteFinder(self) -> None:
        if self.Instrument is None:
            Error.InvalidInstrument()
            return
        elif self.Key is None:
            Error.InvalidKey()
            return

        self.Instrument.FindKeyNotes(self.Key.ScaleNotes)
        print("Where to find all the notes in key with " + self.selectKey)
        print("===============================================================")
        self.Instrument.ShowAllKeyNotes()
        print("===============================================================")

        