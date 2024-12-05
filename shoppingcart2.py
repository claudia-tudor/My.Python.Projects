shopping_cart_tci = ['apples', 'oranges', 'carrots', 'strawberries', 'pineapples']
interactive_menu_tci = """
a. Display shopping cart
b. Remove the first item in the shopping cart
c. Display the last three items of the shopping cart
d. Display the number of items in the shopping cart
e. Display the shopping cart sorted alphabetically
f. Remove carrots from shopping cart
g. Add to the list a fruit inserted by the user
h. Quit
"""
print (interactive_menu_tci)
while True:
    option_tci = input("Please select an option: ")
    
    if option_tci == "a":
        print("The cart contains:" , shopping_cart_tci)
    else:
        if option_tci == "b":
            shopping_cart_tci.pop(0)
            print("The cart contains:" , shopping_cart_tci)
        else:
            if option_tci == "c":
                print("The last three items in the shopping cart are:" , shopping_cart_tci[-3:])
            else:
                if option_tci == "d":
                    print("There are" , len(shopping_cart_tci) "items in the shopping cart")
                else:
                    if option_tci == "e":
                        print("The content is, in alphabetic order:" sorted(shopping_cart_tci))
                    else:
                        if option_tci == "f":
                            shopping_cart_tci = [item for item in shopping_cart_tci if item != 'carrots']
                            print("The cart contains:" , shopping_cart_tci )
                        else:
                            if option_tci == "g":
                                new_fruit_tci = input("Please add a fruit to the cart: ")
                                shopping_cart_tci.append(new_fruit_tci)
                                print("The cart contains:" , shopping_cart_tci)
                            else:
                                if option_tci == "h":
                                    print("Thank you!")
                                    break
                                else:
                                    print("Invalid option. Please select again.")