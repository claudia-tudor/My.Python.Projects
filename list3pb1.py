shopping_cart_tci = ['strawberries', 'pineapples', 'oranges', 'carrots']

interactive_menu_tci = """
a. Display the number of items in the shopping cart
b. Remove the last item in the shopping cart
c. Display the shopping cart sorted alphabetically
d. Display shopping cart
e. Remove pineapples from shopping cart
f. Display the last three items of the shopping cart
g. Add to the list a fruit inserted by the user
h. Quit
"""

while True:
    print(interactive_menu_tci)
    choice = input("Please select an option: ").strip().lower()

    if choice == 'a':
        print(f"There are {len(shopping_cart_tci)} items in the shopping cart.")
    else:
        if choice == 'b':
            if shopping_cart_tci:
                shopping_cart_tci.pop()
                print(f"The cart now contains: {shopping_cart_tci}")
            else:
                print("The shopping cart is empty.")
        else:
            if choice == 'c':
                print(f"The cart items in alphabetical order: {sorted(shopping_cart_tci)}")
            else:
                if choice == 'd':
                    print(f"The cart contains: {shopping_cart_tci}")
                else:
                    if choice == 'e':
                        if 'pineapples' in shopping_cart_tci:
                            shopping_cart_tci.remove('pineapples')
                            print(f"The cart now contains: {shopping_cart_tci}")
                        else:
                            print("Pineapples are not in the cart.")
                    else:
                        if choice == 'f':
                            print(f"The last three items in the cart are: {shopping_cart_tci[-3:]}")
                        else:
                            if choice == 'g':
                                fruit = input("Enter a fruit to add to the cart: ").strip()
                                shopping_cart_tci.append(fruit)
                                print(f"The cart now contains: {shopping_cart_tci}")
                            else:
                                if choice == 'h':
                                    print("Exiting the program.")
                                    break
                                else:
                                    print("Invalid option, please try again.")