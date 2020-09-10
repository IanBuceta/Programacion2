from os import system

traductor = dict()

while(True):
    system("cls")
    traduccion = input("Ingrese palabra a traducir y su traduccion con el formato '<palabra>:<traducción>': ").split(":")
    traductor[traduccion[0].lower()] = traduccion[1].lower()
    if input("¿Desea seguir ingresando elementos?: ").lower() == "no":
        break

while(True):
    system("cls")
    llave = input("Ingrese palabra en ESPAÑOL: ").lower()
    traduccion = str()
    if llave in traductor.keys():
        traduccion = traductor[llave]

    print(traduccion)

    if input("¿Desea seguir traduciendo?: ").lower() == "no":
        system("cls")
        break
