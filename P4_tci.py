
# Online Python - IDE, Editor, Compiler, Interpreter

Alisa_tci=bool(int(input("Did Simona defeat Alisa?")))
Maria_tci=bool(int(input("Did Simona defeat Maria?")))
Venus_tci=bool(int(input("Did Maria defeat Venus?")))
Simona_remains_tci=Alisa_tci and Maria_tci or not Maria_tci and not Venus_tci 
Simona_remains_not_tci=not Simona_remains_tci
print(f"It is {Simona_remains_not_tci} that Simona remains number one!")
print(f"It is {Simona_remains_tci} that Simona doesn't remain number one!")