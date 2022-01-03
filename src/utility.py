class Utility:
    MAX_NOTES_IN_SCALE = 8
    OrderOfNotes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
    ALL_POSSIBLE_NOTES = len(OrderOfNotes)
    WHOLE_STEP = 2
    HALF_STEP = 1

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
            tempNote = (i + index) % Utility.ALL_POSSIBLE_NOTES
            temp.append(Utility.OrderOfNotes[tempNote])
        
        return temp

    # Completes the major scale depending on the starting root note
    def CompleteMajorScale(rootNote):
        temp = []
        temp.append(rootNote)
        currentNote = rootNote
        startIndexOfRootNote = Utility.OrderOfNotes.index(rootNote)
        for i in range(Utility.MAX_NOTES_IN_SCALE):
            if i == 0:
                pass
            elif i == 1 or i == 2 or i == 4 or i == 5 or i == 6:
                currentIndex = startIndexOfRootNote + Utility.WHOLE_STEP
                
                startIndexOfRootNote = currentIndex

                tempNoteIndex = (currentIndex) % Utility.ALL_POSSIBLE_NOTES
                temp.append(Utility.OrderOfNotes[tempNoteIndex])
            elif i == 3 or i == 7:
                currentIndex = startIndexOfRootNote + Utility.HALF_STEP
                startIndexOfRootNote = currentIndex

                tempNoteIndex = (currentIndex) % Utility.ALL_POSSIBLE_NOTES
                temp.append(Utility.OrderOfNotes[tempNoteIndex])
   
        return temp

    

    

