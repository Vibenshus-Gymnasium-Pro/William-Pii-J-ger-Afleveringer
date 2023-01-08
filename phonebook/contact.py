import phonenumber

class Contant:
    def __init__(self, name, email, address, phonenum, model, type):
        self.name = name
        self.email = email
        self.phones = []
        self.addPhone(phonenum, model, type)
        self.address = address

    def get_Name(self):
        return self.name

    def addPhone(self, phonenum, model, type):
        self.phones.append(phonenumber.Phonenumber(phonenum, model, type))

    def get_informationDetails(self, info = 0):
        if (info == 0):
            print(self.name + "\n" + self.email + "\n" + self.address + "\n")
        self.get_Phones()

    def get_Phones(self):
        for i in self.phones:
            i.get_phoneInfo()
