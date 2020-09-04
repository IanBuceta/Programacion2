from os import system

def agregarAlFinal(elemento, tupla):
    lista = list(tupla)
    lista.append(elemento)
    return tuple(lista)

def agregarPosN(posicion,elemento, tupla):
    lista = list(tupla)
    lista.insert(posicion, elemento)
    return tuple(lista)

def borrarElemento(elemento, tupla):
    lista = list(tupla)
    lista.remove(elemento)
    return tuple(lista)
    
def modificarPosN(posicion, elemento, tupla):
    lista = list(tupla)
    lista[posicion] = elemento
    return tuple(lista)


tupla = tuple()

opciones = ("1. Agregar al final", "2. Agregar en Pos N", "3. Borrar Elemento", "4. Modificar Pos N", "5. Salir")
continuar = True

while(continuar == True):

    print("Elementos de la tupla:")
    print(str(tupla))
    print("Opciones:")
    for opcion in opciones:
        print(opcion)
    seleccion = input("Seleccione una accion: ")

    if(seleccion == "1"):
       tupla = agregarAlFinal(input("Ingrese elemento a agregar al final: "), tupla)
    elif(seleccion == "2"):
       tupla = agregarPosN(int(input("Ingrese posicion: ")), input("Ingrese elemento a agregar en posicion: "), tupla)
    elif(seleccion == "3"):
        elemento = input("Ingrese elemento a borrar: ")
        if(elemento in tupla):
           tupla = borrarElemento(elemento, tupla)
        else:
            print("El elemento ingresado no existe en la tupla. ")
    elif(seleccion == "4"):
        tupla = modificarPosN(int(input("Ingrese posicion: ")), input("Ingrese elemento nuevo: "), tupla)
    elif(seleccion == "5"):
        continuar = False
    else:
        print("No ha seleccionado un número correspondiente a las opciones")

    system("cls")
    