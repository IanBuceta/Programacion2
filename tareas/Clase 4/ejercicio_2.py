from os import system

divisa = {
    "dolar": "$",
    "euro": "€",
    "yen": "¥"
}

while(True):
    system("cls")
    try:
        # Se pide primero el input, despues se pasa a minúsculas para evitar problemas de key, en caso de no existir dispara la exception y avisa. Si todo sale bien, se imprime el símbolo
        print(divisa[str.lower(input("Ingrese una Divisa: "))])
    except:
        print("La divisa ingresada no existe")
    if(str.lower(input("¿Desea continuar?: ")) == "no"):
        break