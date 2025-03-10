#def simple_class_tci
class cube_tci:
    def __init__(self):
        self.size_tci = 10  
    def say_my_type_tci(self):
        print("I am a cube")
    def compute_volume_tci(self):
        volume = self.size_tci ** 3
        print(f"My volume is: {volume}")
small_cube_tci = cube_tci()
small_cube_tci.say_my_type_tci()
print("My default volume is:")
small_cube_tci.compute_volume_tci()
small_cube_tci.size_tci = int(input("Please enter a value:"))
print("My new volume is:")
small_cube_tci.compute_volume_tci()

#def constructor_class_tci
class cube_tci:
    def __init__(self, size_tci, number_tci):
        self.size_tci = size_tci
        self.number_tci = number_tci
    def say_my_type_tci(self):
        print("I am a cube")
    def compute_total_volume_tci(self):
        total_volume = self.number_tci * (self.size_tci ** 3)
        print(f"My total volume is: {total_volume}")
set_of_cubes_tci = cube_tci(10, 3) 
set_of_cubes_tci.say_my_type_tci()
print("My total volume is:")
set_of_cubes_tci.compute_total_volume_tci()
set_of_cubes_tci.number_tci = int(input("Please enter a value: "))
print("My new total volume is:")
set_of_cubes_tci.compute_total_volume_tci()