Simona_tci=bool(int(input("Did Simona defeat Carla?")))
Simona_tci=bool(int(input("Did Simona defeat Serena?")))
Serena_tci=bool(int(input("Did Serena defeat Camilla?")))
Simona_remains_tci=Simona_tci and Simona_tci or not Serena_tci and not Simona_tci 
Simona_remains_not_tci=not Simona_remains_tci
print(f"It is {Simona_remains_tci} that Simona remains number one!")
print(f"It is {Simona_remains_not_tci} that Simona doesn't remain number one!")