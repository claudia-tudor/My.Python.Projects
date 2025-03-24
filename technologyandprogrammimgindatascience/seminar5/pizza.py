food1='pizza'
ingredient1='cheese'
ingredient2='mushrooms'
ingredient3='basil'
food2='pasta'

print('I like {0} with {1} and %s and if there is no %s in the menu I would like %s with {1}, %s and %s'.format(
    food1, ingredient1, ingredient2, ingredient3, food2)%(ingredient2,food1,food2, ingredient2, ingredient3))

with open('ingredient.txt' , 'w') as f:
     f.write(ingredient1+ '\n')
     f.write(ingredient2+ '\n')
     f.write(ingredient3+ '\n')
     
with open('ingredients.txt' , 'r') as f:
    a=f.readline()
    b=f.readline()
    c=f.readline()
    
print('The ingredients stored in the file are: ', a, b, c)