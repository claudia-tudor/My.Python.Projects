def print_min(firstnumber, secondnumber):
    if firstnumber < secondnumber:
        print(f"{firstnumber} is smaller")
    elif secondnumber < firstnumber:
        print(f"{secondnumber} is smaller")
    else:
        print("Numbers are equal")
print_min(2, 3)
print_min(15, 10)