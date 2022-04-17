import sys
from sys import argv
import pyperclip

# Create the parser and add arguments
favoritos = ["F1", "F2", "F3", "F4", "F5"]
argumentos = ["FA" ,"FP", favoritos]
error = "Usage: python pynumpad.py {number} or {option}\n" \
        f"\targumentos: \n\t\t favoritos: \n \t\t\t{argumentos[2]}\n" \
        f"\t\tFA: Appends a new char to favorites\n" \
        f"\t\tFP: print all the favorites"

if len(sys.argv) == 1:
    print(error)





for arg in argv[1:]:
    arg = arg.upper()
    if arg not in favoritos and arg not in argumentos and arg.isnumeric() is False:
        print(error)
        exit(-1)
    f = open("favs.txt", "r")
    doc = f.readline()
    if len(sys.argv) == 2 and arg[0].isnumeric():
        character = chr(int(arg))
        pyperclip.copy(character)

    elif arg == "FP":
        print(doc)
    elif arg == "FA":
        print("Saber como le voy a hacer para agregar uno nuevo xDDD")
    elif arg in favoritos:
        try:
            a = arg[1]
            posicion = doc[int(a) - 1]
            print(doc[int(a) - 1])
            pyperclip.copy(posicion)
        except:
            print("Dont have that index in fav")
