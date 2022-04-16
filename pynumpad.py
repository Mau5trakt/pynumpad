import sys
from sys import argv
import pyperclip

# Create the parser and add arguments
favoritos = ["F1", "F2", "F3", "F4", "F5"]
argumentos = ["FA" ,"FP", favoritos]
error = "Usage: python pynumpad.py {number} or {option}\n" \
        f"\targumentos: \n\t\t favoritos: \n \t\t\t{argumentos[2]}"


print(f"number of arguments {len(sys.argv)}")
if len(sys.argv) == 1:
    print(error)





for arg in argv[1:]:
    arg = arg.lower()
    f = open("favs.txt", "r")
    doc = f.readline()
    print(arg)
    print(type(arg))
    if len(sys.argv) == 2 and arg[0].isnumeric():
        print(chr(int(arg)))

    elif arg == "fp":
        print(doc)
    elif arg == "FA":
        print("Saber como le voy a hacer para agregar uno nuevo xDDD")
    elif arg in favoritos:
        a = arg[1]
        print(arg[1])
        print(f"Favorito {a}")
        doc = f.readline()
        posicion = doc[int(a) - 1]
        print(doc[int(a) - 1])
        pyperclip.copy(posicion)
    else:
        print(error)