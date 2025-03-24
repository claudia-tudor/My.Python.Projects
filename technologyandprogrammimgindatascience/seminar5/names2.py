NP1_tci = "Serena"
NP2_tci = "Elena"
NP3_tci = "Simona"

def interactive_menu_tci():
    print("\nMenu:")
    print("i. Save player names")
    print("ii. Read names from file")
    print("iii. When will Simona remain number one?")
    print("iv. Change name of first player")
    print("v. Quit")

while True:
    interactive_menu_tci()
    choice_tci = input("Please enter an option: ")

    if choice_tci == "i":
        with open("NP_tci.txt", "w") as file_tci:
            file_tci.write("%s\n%s\n%s\n" % (NP1_tci, NP2_tci, NP3_tci))
        print("Player names saved to file!")

    elif choice_tci == "ii":
        try:
            with open("NP_tci.txt", "r") as file_tci:
                NP1_tci, NP2_tci, NP3_tci = [line.strip() for line in file_tci.readlines()]
            print("Player names loaded from file!")
        except FileNotFoundError:
            print("Error: NP_tci.txt not found!")
            
    elif choice_tci == "iii":
            print("{2} will remain number one if {2} defeats {0} and %s defeats {1} or if %s defeats {1} and {0} defeats %s" % (
                NP1_tci, NP2_tci, NP1_tci
            ))

    elif choice_tci == "iv":
        NP1_tci = input("Please insert the name of the first player: ")
        print("First player changed to %s!" % NP1_tci)

   
    elif choice_tci == "v":
        print("Good bye!")
        break