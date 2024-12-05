
# Online Python - IDE, Editor, Compiler, Interpreter

Carla_tci=bool(int(input("Did Simona defeat Carla?")))
Serena_tci=bool(int(input("Did Simona defeat Serena?")))
Camilla_tci=bool(int(input("Did Serena defeat Camilla?")))
Simona_remains_tci=Carla_tci and Serena_tci or not Serena_tci and not Camilla_tci 
Simona_remains_not_tci=not Simona_remains_tci
print(f"It is {Simona_remains_not_tci} that Simona remains number one!")
print(f"It is {Simona_remains_tci} that Simona doesn't remain number one!")