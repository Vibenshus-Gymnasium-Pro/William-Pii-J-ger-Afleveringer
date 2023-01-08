class Phonenumber:
    def __init__(self, number, phonemodel, phonetype):
        self.phonemodel = phonemodel
        self.phonetype = phonetype
        self.number = number

    def get_phoneInfo(self):
        print("Phonenumber:\t" + str(self.number) + "\nType:\t\t\t" + str(self.phonetype) + "\nModel:\t\t\t" + str(self.phonemodel) + "\n")