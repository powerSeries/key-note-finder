class Error:
    def __init__(self) -> None:
        pass

    def InvalidInstrument(self):
        print("Instrument has not been created, please create a new one.")
        return
    
    def InvalidKey(self):
        print("Key has not been selected, please select a key. ")
        return
