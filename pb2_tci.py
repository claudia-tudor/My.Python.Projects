
# Online Python - IDE, Editor, Compiler, Interpreter

Caroline_tci=bool(int(input("Did Simona defeat Caroline?")))
Serena_tci=bool(int(input("Did Simona defeat Serena?")))
Carla_tci=bool(int(input("Did Serena defeat Carla?")))
Simona_remains_tci=Caroline_tci and Serena_tci or not Serena_tci and not Carla_tci 
Simona_remains_not_tci=not Simona_remains_tci
print(f"It is {Simona_remains_not_tci} that Simona remains number one!")
print(f"It is {Simona_remains_tci} that Simona doesn't remain number one!")