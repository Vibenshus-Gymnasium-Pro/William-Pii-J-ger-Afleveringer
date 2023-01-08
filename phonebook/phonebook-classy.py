import contact

phonebook = []

def show_phonebook():
    for objects in phonebook:
        print(objects.get_Name())

def add_personTophonebook():
    name = input("Name: ")
    phonenumber = input("Phonenumber: ")
    address = input("Address: ")
    email = input("Email: ")
    model = input("Model: ")
    type = input("Type: ")
    
    if (get_personInphonebook(name) == None):
        phonebook.append(contact.Contant(name, email, address, phonenumber, model, type))
    else:
        print("Person is already in registry")   


def get_personInphonebook(name = 0):
    directlookup = 0
    if (name == 0):
        name = input("Name: ")
        directlookup = 1
    for objects in phonebook:
        if (objects.get_Name() == name):
            if (directlookup == 1):
                objects.get_informationDetails()
            return objects
    return None

def delete_personInphonebook(name = 0):
    
    if (phonebook.__len__() != 0):
        if (name == 0):
            name = input("Name: ")
    if (get_personInphonebook(name) != None):
        phonebook.remove(get_personInphonebook(name))
    else:
        print("0 people in phonebook")
    
def add_phoneNumberToPerson():
    name = input("Person: ")
    number = input("Phonenumber: ")
    model = input("Model: ")
    type = input("Type: ")
    if (get_personInphonebook(name) != None):
        get_personInphonebook(name).addPhone(number, model, type)


def menu():
    """Display a menu, and ask the user to choose an option.
    Ensures that the chosen option is valid."""
    while True:
        print()
        print("0: quit")
        print("1: Print all contacts")
        print("2: Add contact")
        print("3: Remove contact")
        print("4: Look up contact by name")
        print("5: Add phonenumber to a person")
        print()

        inp = input("> ")
        if inp.isdigit():
            i = int(inp)
            if i >= 0 and i <= 5:
                return i
        
        print("INVALID INPUT")

def main():

    contact1 = contact.Contant("William", "minewpj@gmail.com", "Kildevældsgade 5 København Ø", 22184788, "personal", "mobile")
    contact1.get_informationDetails()
    contact1.addPhone(88992233, "wired", "work")
    contact1.get_informationDetails()

    phonebook.append(contact1)

    while True:
        i = menu()
        
        if i == 0:
            break
        elif i == 1:
            show_phonebook()
        elif i == 2:
            add_personTophonebook()
            pass
        elif i == 3:
            delete_personInphonebook()
            pass
        elif i == 4:
            get_personInphonebook()
            pass
        elif i == 5:
            add_phoneNumberToPerson()


if __name__ == "__main__":
    main()
