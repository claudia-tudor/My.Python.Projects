description=['Trailing Hearts Duo', 'Trailing Hearts Duo', 'The Easy Care Duo', 
             'The Easy Care Duo', 'Tropical Trio', 'Tropical Trio',
             'Living Room Duo', 'Living Room Duo', 'Plant Parent Set', 
             'Plant Parent Set', 'Modern Office Duo', 'Modern Office Duo',
             'Low-Light Duo', 'Low-Light Duo', 'Touch of Pink Duo',
             'Touch of Pink Duo', 'New Digs Plant Trio', 'New Digs Plant Trio', 
             'Mini Rare Cactus Bundle', 'Mini Rare Cactus Bundle',
             'Hardy Houseplants Duo', 'Hardy Houseplants Duo', 
             'Orchid Party Pack, Set of 20', 'Orchid Party Pack, Set of 20',
             'Pet-Friendly Plant Parent Set', 'Pet-Friendly Plant Parent Set', 
             'Air Purifying Trio', 'Air Purifying Trio', 
             'New Digs Pet Friendly Plant Trio',
             'New Digs Pet Friendly Plant Trio', 'Best Sellers Duo', 
             'Best Sellers Duo', 'The Big and Bright Duo', 
             'The Big and Bright Duo', 'Top-Seller Duo', 'Top-Seller Duo', 
             'The Palm Bundle', 'The Palm Bundle', 
             'Orchid Party Pack, Set of 12', 'Orchid Party Pack, Set of 12',
             'Succulent Party Pack, Set of 20', 
             'Succulent Party Pack, Set of 20', 'Olive Tree', 
             'Monstera Deliciosa', 'Money Tree Plant',
             'Red Dragon Japanese Maple Tree']

price = ['$89.0-$90', '$89.0-$93', '$199.0-$205', "$79.0-$85", '$99.0-$110', '$219.0-$230',
         '$169.0-$180', '$79.0-$85', '$159.0-$170', '$119.0-$125', '$99.0-$114', '$149.0-$155',
         '$169.0-$173', "$139.0-$147", '$289.0-$299', '$49.0-$58']

p1_list=[]
d1_list=[]
for desc in description:
    d1=desc.upper()
    d1_list.append(d1)
print(d1_list)

for p in price:
    pu=p.replace('$' , '')
    print(pu)
    if '-' in pu : 
        dashPosition=pu.find('-')
        print(dashPosition)
        if dashPosition>0:
            p1=float(pu[:dashPosition])
            print(p1)
            p1_list.append(p1)
            print(p1_list)
print(p1_list)
