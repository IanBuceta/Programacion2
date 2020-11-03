# import random
import os

ARCHIVO_DATOS = "datos.txt"


def escribir(nombre_archivo, dni, registro):
    with open(nombre_archivo, "a") as file:
        file.write("{};{}\n".format(dni, registro))


def escribir_ordenado(dni, registro):
    with open(ARCHIVO_DATOS, "a+") as file:
        file.seek(0)
        lista_datos = list()
        for line in file.readlines():
            datos = line.strip("\n").split(";")
            lista_datos.append([datos[0], datos[1]])
        lista_datos.append([dni, registro])
        lista_datos.sort(key=lambda lista: int(lista[0]))
    os.remove(ARCHIVO_DATOS)
    for dato in lista_datos:
        escribir(ARCHIVO_DATOS, dato[0], dato[1])


escribir_ordenado(1, 14)

'''
rango = 1000
for i in range(rango):
    escribir_ordenado(random.randint(i, rango), random.randint(i, rango))
'''
