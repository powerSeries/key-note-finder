from scale import Scale
class KeyMenu:
    # Class variables
    ActiveKey = Scale('C')
    IsMenuActive = False
    ALL_MAJOR_SCALE = ['C', 'G', 'D', 'A', 'E', 'B', 'F#', 'C#']

    def __init__(self) -> None:
        pass

    def InitializeMenu(self) -> None:
        print("Choose from the following keys.")

        self.IsMenuActive = True
        self.ShowMajorScales()
        while(self.IsMenuActive):
            selectScale = input("Select your key")
            self.ActiveKey.ChangeScaleTo(selectScale)
            self.ActiveKey.DisplayScale()
            pass        
                
    def ShowMajorScales(self) -> None:
        for majorScale in KeyMenu.ALL_MAJOR_SCALE:
            print(majorScale + " major")
        pass

