shopping_list_tci = ["carrots", "apples", "oranges", "pineapples", "strawberries"]
interactive_menu_tci = """
a. Display shopping cart
b. Add to the list a fruit inserted by the user
c. Display the shopping cart sorted alphabetically
d. Display the last four items in the shopping cart
e. Remove oranges from the shopping cart
f. Remove the first item in the shopping cart
g. Display the number of items in the shopping cart
h. Quit
"""
print (interactive_menu_tci)
while True:
    option_tci = input("Please select an option: ").lower()

    if option_tci == "a":
        print("The cart contains:", shopping_list_tci)
    else:
        if option_tci == "b":
            shopping_list_tci.append(input("Please add a fruit to the cart: "))
        else:
            if option_tci == "c":
                sorted_list_tci = sorted(shopping_list_tci)
                print("The content is, in alphabetic order:", sorted_list_tci)
            else:
                if option_tci == "d":
                    print("The last four items in the shopping cart are:", shopping_list_tci[-4:])
                else:
                    if option_tci == "e":
                        if "oranges" in shopping_list_tci:
                            shopping_list_tci.remove("oranges")
                        else:
                            print("Oranges are not in the cart.")
                    else:
                        if option_tci == "f":
                            if shopping_list_tci:
                                removed_item_tci = shopping_list_tci.pop(0)
                        else:
                            if option_tci == "g":
                                print("There are" , len(shopping_list_tci) , "items in the shopping cart")
                            else:
                                if option_tci == "h":
                                    print("Thank you!")
                                    break
                                else:
                                    print("Invalid option. Please try again.")