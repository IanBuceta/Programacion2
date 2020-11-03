'''
    This class receives a list of tuples (which must have a str, function structure) as a parameter.
    The following is an example code showing a use case for this class,
    in which the user generates a hello_world function and then
    initializes the class with a list containing a tuple with the desired menu name,
    and the function it calls

    def hello_world():
        print("Hello World")


    screen = Menu([("Hello World", hello_world)])
    screen.show()
'''
from os import system
from typing import List


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
            self.__cls__()
            for option_key, option_value in self.__options.items():
                print("{}. {}".format(option_key, option_value[0]))
            option = int(input("Seleccione una opcion: "))
            self.__cls__()
            if option == len(self.__options):
                break
            self.__options[option][1]()
            input("Press any key to continue...")
