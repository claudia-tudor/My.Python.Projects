import math
def compute_sphere_volume_tci(number_of_spheres_tci, radius_tci=20):
    individual_volume = (4/3) * math.pi * (radius_tci ** 3)
    total_volume = number_of_spheres_tci * individual_volume
    return total_volume
    
#from function import compute_sphere_volume_initials
def main():
    no_tci = int(input("Please enter the number of spheres: "))
    total_volume_default = compute_sphere_volume_tci(no_tci)
    print("Total volume with default radius:", total_volume_default)
    radius_tci = int(input("Please enter the radius of the spheres: "))
    total_volume_tci = compute_sphere_volume_tci(no_tci, radius_tci)
    print("Total volume with both arguments is", total_volume_tci)

main()