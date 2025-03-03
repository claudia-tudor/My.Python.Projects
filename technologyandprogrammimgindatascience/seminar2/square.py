def compute_square_area_tci(number_of_squares_tci, size_tci=15):
    total_area = number_of_squares_tci * (size_tci ** 2)
    return total_area
    
#from function import compute_square_area_tci
def main():
    no_tci = int(input("Enter the number of squares: "))
    total_area_default = compute_square_area_tci(no_tci)
    print("Total area is:", total_area_default)
    size_tci = int(input("Please enter the size of the squares: "))
    total_area_tci = compute_square_area_tci(no_tci, size_tci)
    print("Total area with both arguments is:", total_area_tci)
    
main()