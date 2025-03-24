Name1_tci = "Elena"
Name2_tci = "Sorana"
Name3_tci = "Simona"

def interactive_menu_tci():
    print("\nMenu:")
    print("i. Save player names")
    print("ii. When will Simona remain number one?")
    print("iii. Read names from file")
    print("iv. Change name of second player")
    print("v. Quit")

while True:
    interactive_menu_tci()
    choice_tci = input("Please enter an option: ")

    if choice_tci == "i":
        with open("Names_tci.txt", "w") as file_tci:
            file_tci.write("%s\n%s\n%s\n" % (Name1_tci, Name2_tci, Name3_tci))
        print("Player names saved to file!")

    elif choice_tci == "ii":
        print("{2} will remain number one if {2} defeats {1} and %s defeats {0} or if %s defeats {0} and {0} defeats %s" % (
            Name1_tci, Name2_tci, Name2_tci
        ))

    elif choice_tci == "iii":
        try:
            with open("Names_tci.txt", "r") as file_tci:
                Name1_tci, Name2_tci, Name3_tci = [line.strip() for line in file_tci.readlines()]
            print("Player names loaded from file!")
        except FileNotFoundError:
            print("Error: Names_tci.txt not found!")

    elif choice_tci == "iv":
        Name2_tci = input("Enter a new name for the second player: ")
        print("Second player changed to %s!" % Name2_tci)

    elif choice_tci == "v":
        print("Game over!")
        break