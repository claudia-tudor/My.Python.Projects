Caroline_tci=bool(int(input("Did Simona defeat Caroline?")))
Maria_tci=bool(int(input("Did Simona defeat Maria?")))
Carla_tci=bool(int(input("Did Maria defeat Carla?")))
Simona_remains_tci=Caroline_tci and Maria_tci or not Maria_tci and not Carla_tci 
Simona_remains_not_tci=not Simona_remains_tci
print(f"It is {Simona_remains_not_tci} that Simona remains number one!")
print(f"It is {Simona_remains_tci} that Simona doesn't remain number one!")
