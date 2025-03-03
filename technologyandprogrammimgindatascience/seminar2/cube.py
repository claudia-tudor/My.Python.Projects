def compute_cube_volume_tci(number_of_cubes_tci, size_tci=25):
    individual_volume = size_tci ** 3
    total_volume = number_of_cubes_tci * individual_volume
    return total_volum
#from function import compute_cube_volume_initials

def main():
    no_tci = int(input("Please enter the number of cubes: "))
    total_volume_default = compute_cube_volume_tci(no_tci)
    print("Total volume with default size:", total_volume_default)
    size_tci= int(input("Please enter the size of the cubes: "))
    total_volume_tci = compute_cube_volume_tci(no_tci, size_tci)
    print("Total volume with both arguments is:", total_volume_tci)

# Run the main function
main()