class Utility:
    # Validates that the input is an integer and prompts user
    # to correctly re-enter the value if it isnt
    def ValidateAsInteger(data):
        if data.isnumeric() == True:
            return True

        temp = int(input("Please enter a valid integer value: "))

        return Utility.ValidateAsInteger(temp)
