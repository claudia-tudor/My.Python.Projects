#def simple_class_tci
class square_tci:
    def __init__(self):
        self.size_tci = 8  
    def say_my_type_tci(self):
        print("I am a square")
    def compute_area_tci(self):
        area_tci = self.size_tci ** 2
        print(f"My area is: {area_tci}")
simple_square_tci = square_tci()
simple_square_tci.say_my_type_tci()
print("My default area is:")
simple_square_tci.compute_area_tci()
simple_square_tci.size_tci = int(input("Please enter a value:"))
print("My new area is:")
simple_square_tci.compute_area_tci()

#def constructor_class_tci
class square_tci:
    def __init__(self, size_tci, number_tci):
        self.size_tci = size_tci
        self.number_tci = number_tci
    def say_my_type_tci(self):
        print("I am a square")
    def compute_total_area_tci(self):
        total_area = self.number_tci * (self.size_tci ** 2)
        print(f"My total area is: {total_area}")
set_of_squares_tci = square_tci(8, 4)  
set_of_squares_tci.say_my_type_tci()
print("My total area is:")
set_of_squares_tci.compute_total_area_tci()
set_of_squares_tci.number_tci = int(input("Please enter a value:"))
print("My new total area is:")
set_of_squares_tci.compute_total_area_tci()
