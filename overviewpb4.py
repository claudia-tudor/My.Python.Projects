interactive_menu_tci = """
A - Set size
P - Display square perimeter
Q - Quit
"""

while True:
    print(interactive_menu_tci)
    choice_tci = print(input("Please enter a choice: "))
    if choice_tci == "A":
        size_tci = float(input("Please enter the size of the square: "))
    elif choice_tci == "P":
        square_perimeter_tci = 4*size_tci
        print(f"The perimeter of a square having a side of {size_tci} is {square_perimeter_tci}")
    elif choice_tci == "Q":
        print("Thank you for using our application.")
        break 
    else:
        print("Please insert a valid menu option.")