from os import system

ID = "id"
NOMBRE = "nombre"
APELLIDO = "apellido"
FECHA_DE_NACIMIENTO = "fecha_de_nacimiento"
FORMATO = "{}: {}"

try:

    with open("personas.txt", "r", encoding="UTF8") as file:
        system("cls")

        lineas = file.readlines()
        personas = list()

        for linea in lineas:
            persona = linea.strip('\n').split(";")

            diccionario_persona = dict()

            diccionario_persona[ID] = persona[0]
            diccionario_persona[NOMBRE] = persona[1]
            diccionario_persona[APELLIDO] = persona[2]
            diccionario_persona[FECHA_DE_NACIMIENTO] = persona[3]

            personas.append(diccionario_persona)

        for persona in personas:
            id_persona = FORMATO.format(ID.title(), persona[ID])
            nombre_persona = FORMATO.format(NOMBRE.title(), persona[NOMBRE])
            apellido_persona = FORMATO.format(
                APELLIDO.title(), persona[APELLIDO])
            fecha_de_nacimiento_persona = FORMATO.format(
                FECHA_DE_NACIMIENTO.replace("_", " ").title(), persona[FECHA_DE_NACIMIENTO])

            print("{}, {}, {}, {}".format(id_persona, nombre_persona,
                                          apellido_persona, fecha_de_nacimiento_persona))
except Exception as ex:
    print(ex)
