import sys
from sys import argv
import pyperclip

# Create the parser and add arguments
print(f"number of arguments {len(sys.argv)}")
if len(sys.argv) == 1:
    print("Usage: python pynumpad.py {number} or {option}")

argumentos = ["F1", "F2", "F3", "F4"]


favoritos = []
for arg in argv[1:]:
    print(arg)
    print(type(arg))
    if len(sys.argv) == 2 and arg[0].isnumeric():
        print("Es numero")
    elif arg in argumentos:
        a = arg[1]
        #print(arg[1])
        #print(f"Favorito {a}")
        f = open("favs.txt", "r")
        doc = f.readline()
        posicion = doc[int(a) - 1]
        print(doc[int(a) - 1])
        pyperclip.copy(posicion)
        """
        f = open("favs.txt", "r")
        f1 = f.readline()
        if arg == "F1":
            print("Favorito 1")
            print(f1[:1])
            print(f1[2:3])
            pyperclip.copy(f1[2:3])
        elif arg == "F2":
            print("Favorito 2")
            print(f1[1])
            pyperclip.copy(f1[2:3])"""

