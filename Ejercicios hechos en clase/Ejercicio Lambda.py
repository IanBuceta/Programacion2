from os import system

def concatenarstring(palabra):
    return lambda a : palabra + a

system("cls")
funcion = concatenarstring(input("Ingrese una palabra: "))
print(funcion(input("Ingrese otra palabra: ")))