ARCHIVO_DATOS = "datos.txt"
ARCHIVO_TEMPORAL = "temp.txt"


def escribir(nombre_archivo, dni, registro):
    with open(nombre_archivo, "a") as file:
        file.write("{};{}\n".format(dni, registro))


def ordenar(dni, registro):
    escrito = False
    with open(ARCHIVO_DATOS, "r") as file_datos:
        for line in file_datos.readlines():
            datos = line.split(";")
            if(int(datos[0]) > dni and escrito is False):
                escribir(ARCHIVO_TEMPORAL, dni, registro)
                escrito = True
            escribir(ARCHIVO_TEMPORAL, datos[0], datos[1])


for i in range(100):
    escribir(ARCHIVO_DATOS, i, i)

ordenar(15, 16)
