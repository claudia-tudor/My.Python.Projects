interactive_menu_tci = """
A - Set size 
C - Display circle area
D - Display circle perimeter
S - Display square area
P - Display square perimeter
Q - Quit"""
print (interactive_menu_tci)

while True: 
    pick_tci = input("Please insert an option:")
    if pick_tci == "A":
        size_tci = float(input("Please insert the size value:"))
    else:
        if pick_tci == "C":
            circle_area_tci = 3.14 * size_tci ** 2
            print("The area of a circle having a radius of", size_tci, "is", circle_area_tci)
        else: 
            if pick_tci == "D":
                circle_perimeter_tci = 2 * 3.14 * size_tci
                print("The perimeter of a circle having the radius of", size_tci, "is", circle_perimeter_tci)
            else: 
                if pick_tci == "S":
                    square_area_tci = size_tci ** 2
                    print("The area of a square having side of", size_tci, "is", square_area_tci)
                else: 
                    if pick_tci == "P":
                        square_perimeter_tci = 4 * size_tci
                        print("The perimeter of a square having a side of", size_tci, "is", square_perimeter_tci)
                    else: 
                        if pick_tci == "Q":
                            print("Thank you for using our application!")
                            break 
                        else:
                            print("Please select a valid menu option:")
                            