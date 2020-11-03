from os import system
from time import sleep
from typing import List
import pymssql


class Menu:
    def __init__(self, opciones: List[tuple]):
        self.__options = dict()
        for i in range(len(opciones)):
            self.__options[i+1] = opciones[i]
        self.__options[i+2] = ("Close",)

    def __cls__(self):
        system("cls")

    def show(self):
        while True:
            try:
                self.__cls__()
                for option_key, option_value in self.__options.items():
                    print("{}. {}".format(option_key, option_value[0]))
                option = int(input("Seleccione una opcion: "))
                self.__cls__()
                if option == len(self.__options):
                    break
                self.__options[option][1]()
                input("Press any key to continue...")
            except Exception as ex:
                print(ex)
                sleep(3)


class MenuPersona(Menu):
    def __init__(self):
        self.__gestor_persona = GestorPersona()
        opciones = [
            ("Agregar Persona", self.alta),
            ("Borrar Persona", self.baja),
            ("Modificacion Persona", self.modificacion),
            ("Mostrar Personas", self.obtener_todos)
        ]
        super().__init__(opciones)

    def __input(self, text: str):
        return input("Ingrese {}: ".format(text))

    def __obtener_dni(self) -> int:
        return int(self.__input("DNI"))

    def alta(self):
        dni = self.__obtener_dni()
        nombre = self.__input("Nombre")
        apellido = self.__input("Apellido")
        self.__gestor_persona.alta(Persona(dni, nombre, apellido))

    def baja(self):
        dni = self.__obtener_dni()
        self.__gestor_persona.baja(dni)

    def modificacion(self):
        dni = self.__obtener_dni()
        nuevo_nombre = self.__input("Nuevo Nombre")
        nuevo_apellido = self.__input("Nuevo Apellido")
        self.__gestor_persona.modificacion(
            Persona(dni, nuevo_nombre, nuevo_apellido))

    def obtener_todos(self):
        personas = self.__gestor_persona.obtener_todos()
        for persona in personas:
            print(persona)


class GestorPersona:
    def __init__(self):
        self.__repositorio_persona = RepositorioPersona()

    def alta(self, persona):
        self.__repositorio_persona.alta(persona)

    def baja(self, dni):
        self.__repositorio_persona.baja(dni)

    def modificacion(self, persona):
        self.__repositorio_persona.modificacion(persona)

    def obtener_todos(self):
        return self.__repositorio_persona.obtener_todos()


class RepositorioPersona:
    def __init__(self):
        self.__connection = pymssql.connect(
            server='localhost',
            database='programacion_2')
        self.__cursor = self.__connection.cursor()

    def alta(self, persona):
        sql_command = "insert into Persona values(%s,%s,%s)"
        valores = (persona.dni, persona.nombre, persona.apellido)
        self.__cursor.execute(sql_command, valores)

    def baja(self, dni):
        sql_command = "delete from Persona where DNI = %s"
        valores = (dni,)
        self.__cursor.execute(sql_command, valores)

    def modificacion(self, persona):
        sql_command = "update Persona set Nombre = %s, Apellido = %s where DNI = %s"
        valores = (persona.nombre, persona.apellido, persona.dni)
        self.__cursor.execute(sql_command, valores)

    def obtener_todos(self) -> List:
        personas = list()
        sql_command = "select * from Persona"
        self.__cursor.execute(sql_command)
        rows = self.__cursor.fetchall()
        for row in rows:
            personas.append(Persona(int(row[0]), str(row[1]), str(row[2])))
        return personas


class Persona:
    def __init__(self, dni: int, nombre: str, apellido: str):
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido

    @ property
    def dni(self):
        return self.__dni

    @ property
    def nombre(self):
        return self.__nombre

    @ nombre.setter
    def nombre(self, value: str):
        self.__nombre = value.strip(';')

    @ property
    def apellido(self):
        return self.__apellido

    @ apellido.setter
    def apellido(self, value: str):
        self.apellido = value.strip(';')

    def __str__(self):
        return "DNI: {}, Nombre: {}, Apellido: {}".format(self.dni, self.nombre, self.apellido)


menu_persona = MenuPersona()
menu_persona.show()
