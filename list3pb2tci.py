shopping_cart_tci = ['oranges', 'carrots', 'strawberries', 'pineapples', 'pears']

interactive_menu_tci = """
a. Display shopping cart
b. Add to the list a fruit inserted by the user
c. Display the number of items in the shopping cart
d. Display the last three items of the shopping cart
e. Remove strawberries from the shopping cart
f. Remove the last item in the shopping cart
g. Display the shopping cart sorted alphabetically
h. Quit
"""
print(interactive_menu_tci)
while True: 
    choice_tci = input("Please select an option: ")
    if choice_tci == "a": 
        print(f"The cart contains: {shopping_cart_tci}")
    else:
        if choice_tci == "b":
            shopping_cart_tci.append(input("Please enter a fruit to the cart:"))
        else:
            if choice_tci == "c":
                print("There are", len(shopping_cart_tci), "items in the shopping cart")
            else: 
                if choice_tci == "d": 
                    print("The last three items in the shopping cart are:", shopping_cart_tci[-3:])
                else: 
                    if choice_tci == "e":
                        del shopping_cart_tci[2]
                        print(shopping_cart_tci)
                    else:
                        if choice_tci == "f":
                            del shopping_cart_tci[-1]
                            print(shopping_cart_tci)
                        else: 
                            if choice_tci == "g":
                                print("The content is, in alphabetic order:", sorted(shopping_cart_tci))
                            else:
                                if choice_tci == "h":
                                    print("Thank you!")
                                    break
                                else: 
                                    print("Invalid choice. Please select a valid option.")