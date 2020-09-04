from os import system
from typing import List

class Moneda:
    def __init__(self, pais: str, valor: float, year: int):
        self.__pais = pais
        self.__valor = valor
        self.__year = year
    
    @property
    def pais(self):
        return self.__pais

    @pais.setter
    def pais(self, value: str):
        self.__pais = value

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, value: float):
        self.__valor = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value: int):
        self.__year = value        


class usuario:
    def __init__(self, monedas: List[Moneda]):
        self.__monedas = monedas

    @property
    def monedas(self):
        return self.__monedas
    
    @property
    def paises(self):
        paises = set()        
        for moneda in self.monedas:
            paises.add(moneda.pais)
        return paises
        
    @property
    def valores(self):
        valores = set()        
        for moneda in self.monedas:
            valores.add(moneda.valor)
        return valores

    @property
    def years(self):
        years = set()        
        for moneda in self.monedas:
            years.add(moneda.year)
        return years


system("cls")

monedas = [Moneda("Argentina", 1600, 1930), Moneda("Argentina", 100, 2001), Moneda("Chile", 100, 2001)]
user = usuario(monedas)

print("Paises: " + str(user.paises))
print("Valores: " + str(user.valores))
print("Años: " + str(user.years))