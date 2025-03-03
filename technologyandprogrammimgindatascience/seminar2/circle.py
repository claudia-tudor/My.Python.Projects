import math
def compute_circle_area_tci(number_of_circle_tci , radius_tci=10):
    total_area_tci=number_of_circle_tci*math.pi*(radius_tci**2)
    return total_area_tci

#from function import compute_circle_area_tci
def main():
    no_tci=int(input("Please enter the number of circles:"))
    total_area_default = compute_circle_area_tci(no_tci)
    print("The total area is" , total_area_default)
    radius_tci = int(input("Please enter the radius of the circles:"))
    total_area_tci = compute_circle_area_tci(no_tci, radius_tci)
    print("The total area with both arguments is", total_area_tci)
main()