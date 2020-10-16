with open("holamundo.txt", "a+") as file:
    file.write(input("Ingrese algo para anotar: ") + "\n")
    print("Cosas escritas en {}:".format(file.name))
    file.seek(0)
    for line in file.readlines():
        print(line)


"""
# Con esto evitas tener que poner el seek, sino lo que ocurre
# es que el puntero queda al final de la linea que
# escribio y no lee nada

with open("holamundo.txt", "a") as file:
    file.write(input("Ingrese algo para anotar: ") + "/n")
with open("holamundo.txt") as file:
    print("Cosas escritas en {}".format(file.name))
    for line in file.readlines():
        print(line)
"""
