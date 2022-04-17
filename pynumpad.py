import sys
import pyperclip

f = open("favs.txt", "r")
doc = f.readline()

favoritos = []
for qty in range(len(doc)):
    favorito = f"F{qty + 1}"
    favoritos.append(favorito)

argumentos = ["FP", favoritos]
error = "Usage: python pynumpad.py {number} or {option}\n" \
        f"\targumentos: \n\t\t favoritos: \n \t\t\t{argumentos[1]}\n" \
        f"\t\tFP: print all the favorites"

if len(sys.argv) == 1:
    print(error)

for arg in sys.argv[1:]:
    arg = arg.upper()
    if arg not in favoritos and arg not in argumentos and arg.isnumeric() is False:
        print(error)
        exit(-1)
    if len(sys.argv) == 2 and arg[0].isnumeric():
        character = chr(int(arg))
        pyperclip.copy(character)

    elif arg == "FP":
        for i in range(len(doc)):
            print(doc[i], end=" ")
    elif arg in favoritos:
        a = arg[1]
        posicion = doc[int(a) - 1]
        print(doc[int(a) - 1])
        pyperclip.copy(posicion)
