class Utility:
    
    OrderOfNotes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']

    # Validates that the input is an integer and prompts user
    # to correctly re-enter the value if it isnt
    def ValidateAsInteger(data):
        if data.isnumeric() == True:
            return True

        temp = int(input("Please enter a valid integer value: "))

        return Utility.ValidateAsInteger(temp)

    # Depending on the starting note it fills each fret of the open string
    # with notes
    def FillOpenStringNotes(startNote, maxFret):
        temp = []
        index = Utility.OrderOfNotes.index(startNote)

        for i in range(int(maxFret)):
            tempNote = (i + index) % len(Utility.OrderOfNotes)
            temp.append(Utility.OrderOfNotes[tempNote])
        
        return temp


        

