Player1_tci = "Simona"
Player2_tci = "Elena"
Player3_tci = "Sorana"

def interactive_menu_tci():
    print("\nMenu:")
    print("i. When will Simona remain number one?")
    print("ii. Save players names")
    print("iii. Change name of second player")
    print("iv. Read names from file")
    print("v. Quit")

while True:
    interactive_menu_tci()
    choice_tci = input("Please enter an option: ")

    if choice_tci == "i":
        print('{0} will remain number one if %s defeats %s and {2}  defeats {1} or if {0} defeats %s and %s defeats {0}'.format(
           Player1_tci, Player2_tci, Player3_tci)%(Player1_tci, Player2_tci, Player3_tci, Player2_tci))

    elif choice_tci == "ii":
        with open("Players_tci.txt", "w") as file_tci:
            file_tci.write("%s\n%s\n%s\n" % (Player1_tci, Player2_tci, Player3_tci))
        print("Player names saved to file!:" )

    elif choice_tci == "iii":
        Player2_tci = input("Enter a new name for the second player: ")
        print("Second player changed to %s!" % Player2_tci)

    elif choice_tci == "iv":
            with open("Players_tci.txt", "r") as file_tci:
                Player1_tci, Player2_tci, Player3_tci = [line.strip() for line in file_tci.readlines()]
            print("Player names loaded from file!", Player1_tci, Player2_tci,Player3_tci)
    elif choice_tci == "v":
        print("Game over!")
        break