class pizza_tci:
    def __init__(self, cost_of_wheat_tci, cost_of_souce_tci, cost_of_ingredients_tci):
        self.cost_of_wheat_tci = cost_of_wheat_tci
        self.cost_of_souce_tci = cost_of_souce_tci
        self.cost_of_ingredients_tci = cost_of_ingredients_tci
        self.cost_of_pizza_tci = self.cost_of_wheat_tci + self.cost_of_souce_tci + self.cost_of_ingredients_tci
        print(f"Cost of pizza: {self.cost_of_pizza_tci}")
    def cost_total_tci(self, package_tci, transportation_tci):
        total_cost_tci = self.cost_of_pizza_tci + package_tci + transportation_tci
        print(f"Total cost at destination: {total_cost_tci}")
    def review_tci(self, message_tci):
        print(f"My review about the pizza is: {message_tci}")
myPizza_tci = pizza_tci(10, 7, 3)  
myPizza_tci.cost_total_tci(2, 3)
myPizza_tci.review_tci("I love this pizza!")