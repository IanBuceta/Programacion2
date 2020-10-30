import random
import os

ARCHIVO_DATOS = "datos.txt"
ARCHIVO_TEMPORAL = "temp.txt"


def escribir(nombre_archivo, dni, registro):
    with open(nombre_archivo, "a") as file:
        file.write("{};{}\n".format(dni, registro))


def escribir_ordenado(dni, registro):
    escrito = False
    with open(ARCHIVO_DATOS, "a+") as file:
        file.seek(0)
        lineas = file.readlines()
        if(len(lineas) == 0):
            escribir(ARCHIVO_TEMPORAL, dni, registro)
        else:
            for line in lineas:
                datos = line.strip("\n").split(";")
                if(int(datos[0]) > dni and escrito is False):
                    escribir(ARCHIVO_TEMPORAL, dni, registro)
                    escrito = True
                escribir(ARCHIVO_TEMPORAL, datos[0], datos[1])
            if (escrito is False):
                escribir(ARCHIVO_TEMPORAL, dni, registro)
    os.remove(ARCHIVO_DATOS)
    os.rename(ARCHIVO_TEMPORAL, ARCHIVO_DATOS)


rango = 10
for i in range(rango):
    escribir_ordenado(random.randint(i, rango), random.randint(i, rango))
