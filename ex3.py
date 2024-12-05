a_tci = float(input("Please enter value for a:\n"))
b_tci = float(input("Please enter value for b:\n"))
c_tci = float(input("Please enter value for c:\n"))

if a_tci == 0:
    if b_tci == 0:
        if c_tci == 0:
            print("Infinite solutions!")
        else:
            print("Impossible solution!")
    else:
        x1_tci = -c_tci / b_tci
        print("x1 =", x1_tci)
else:
    delta_tci = b_tci**2 - 4 * a_tci * c_tci
    if delta_tci < 0:
        print("Complex solution!")
    elif delta_tci == 0:
        x1_tci = -b_tci / (2 * a_tci)
        print("x1 =", x1_tci)
    else:
        x1_tci = (-b_tci + delta_tci**0.5) / (2 * a_tci)
        x2_tci = (-b_tci - delta_tci**0.5) / (2 * a_tci)
        print("x1 =", x1_tci)
        print("x2 =", x2_tci)