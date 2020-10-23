import random
import os

ARCHIVO_DATOS = "datos.txt"


def escribir(nombre_archivo, dni, registro):
    with open(nombre_archivo, "a") as file:
        file.write("{};{}\n".format(dni, registro))


def escribir_ordenado(dni, registro):
    archivo_ordenado = 0
    with open(ARCHIVO_DATOS, "a+") as file:
        escribir(ARCHIVO_DATOS, dni, registro)
        file.seek(0)
        archivo_ordenado = sorted(
            file.readlines(), key=lambda lista: int(lista.split(";")[0]))

    os.remove(ARCHIVO_DATOS)
    with open(ARCHIVO_DATOS, "a+") as file:
        for sorted_line in archivo_ordenado:
            file.write(sorted_line)


rango = 10
for i in range(rango):
    escribir_ordenado(random.randint(i, rango), random.randint(i, rango))
