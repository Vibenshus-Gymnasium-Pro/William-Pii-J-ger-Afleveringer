phonebook = {}

def show_phonebook():
    """Print all contacts in the phonebook."""
    for (name, phonenumber) in phonebook.items():
        print(name, ':', phonenumber)

def add_personTophonebook():
    name = input("Name: ")
    phonenumber = input("Phonenumber: ")
    if (get_personeInphonebook(name) == None):
        phonebook[name] = phonenumber
    else:
        print("Person is already in registry")


def get_personeInphonebook(name = 0):    
    if (name == 0):
        name = input("Name: ")
    return phonebook.get(name)

def delete_personInphonebook(name = 0):
    if (name == 0):
        if (phonebook.__len__() != 0):
            while (phonebook.get(name) == None):
                name = input("Name : ")
            phonebook.pop(name)
        else:
            print("Phonebook is empty")
    print(name)

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
        print()

        inp = input("> ")
        if inp.isdigit():
            i = int(inp)
            if i >= 0 and i <= 4:
                return i
        
        print("INVALID INPUT")

def main():
    """Main loop, where the menu is shown, the user chooses an option,
    and the relevant code is run."""
    while True:
        i = menu()
        
        if i == 0:
            break
        elif i == 1:
            show_phonebook()
        elif i == 2:
            add_personTophonebook()
            pass # her tilføjes kode for at tilføje en ny kontakt
        elif i == 3:
            delete_personInphonebook()
            pass # her tilføjes kode for at slette en kontakt
        elif i == 4:
            print(get_personeInphonebook())
            pass # her tilføjes kode for at slå en kontakt op ved navn

if __name__ == "__main__":
    main()