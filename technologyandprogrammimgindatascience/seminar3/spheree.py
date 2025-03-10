#def simple_class_tci
import math
class sphere_tci:
    def __init__(self):
        self.radius_tci = 15  
    def say_my_type_tci(self):
        print("I am a sphere")
    def compute_volume_tci(self):
        volume = (4/3) * math.pi * (self.radius_tci ** 3)
        print(f"My volume is: {volume:.2f}")
big_sphere_tci = sphere_tci()
big_sphere_tci.say_my_type_tci()
print("My default volume is:")
big_sphere_tci.compute_volume_tci()
big_sphere_tci.radius_tci = float(input("Please enter a value: "))
print("My new volume is:")
big_sphere_tci.compute_volume_tci()