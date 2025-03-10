#def simple_class_tci
import math
class circle_tci:
    def __init__(self):
        self.radius_tci = 5  
    def say_my_type_tci(self):
        print("I am a circle")
    def compute_area_tci(self):
        area = math.pi * (self.radius_tci ** 2)
        print(f"My area is: {area:.2f}")
one_circle_tci = circle_tci()
one_circle_tci.say_my_type_tci()
print("My default area is:")
one_circle_tci.compute_area_tci()
one_circle_tci.radius_tci = float(input("Please enter a value: "))
print("My new area is:")
one_circle_tci.compute_area_tci()

#def constructor_class_tci
import math
class circle_tci:
    def __init__(self, radius_tci, number_tci):
        self.radius_tci = radius_tci
        self.number_tci = number_tci
    def say_my_type_tci(self):
        print("I am a circle")
    def compute_total_area_tci(self):
        total_area = self.number_tci * math.pi * (self.radius_tci ** 2)
        print(f"My total area is: {total_area:.2f}")
set_of_circles_tci = circle_tci(5, 3) 
set_of_circles_tci.say_my_type_tci()
print("My total area is:")
set_of_circles_tci.compute_total_area_tci()
set_of_circles_tci.number_tci = int(input("Please enter a value: "))
print("My new total area is:")
set_of_circles_tci.compute_total_area_tci()