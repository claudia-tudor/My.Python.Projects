NoP1_tci = "Elena"
NoP2_tci = "Simona"
NoP3_tci = "Caroline"

def interactive_menu_tci():
    print("\nMenu:")
    print("i. Save names")
    print("ii. Change name of third player")
    print("iii. When will Simona remain number one?")
    print("iv. Read names from file")
    print("v. Quit")

while True:
    interactive_menu_tci()
    choice_tci = input("Please enter an option: ")

    if choice_tci == "i":
        with open("NoP_tci.txt", "w") as file_tci:
            file_tci.write("%s\n%s\n%s\n" % (NoP1_tci, NoP2_tci, NoP3_tci))
        print("Player names saved to file!")

    elif choice_tci == "ii":
        NoP3_tci = input("Please insert a new name for the third player: ")
        print("Third player changed to %s!" % NoP3_tci)

    elif choice_tci == "iii":
        print("{1} will remain number one if %s defeats {0} and %s defeats {2} or if {1} defeats %s and {2} defeats %s" % (
            NoP2_tci, NoP2_tci, NoP3_tci, NoP3_tci, NoP1_tci
        ))

    elif choice_tci == "iv":
        try:
            with open("NoP_tci.txt", "r") as file_tci:
                NoP1_tci, NoP2_tci, NoP3_tci = [line.strip() for line in file_tci.readlines()]
            print("Player names loaded from file!")
        except FileNotFoundError:
            print("Error: NoP_tci.txt not found!")

    elif choice_tci == "v":
        print("Good bye!")
        break