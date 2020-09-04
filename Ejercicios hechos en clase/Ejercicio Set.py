from os import system

class Moneda:
    def __init__(self, pais, valor, year):
        self.__pais = pais
        self.__valor = valor
        self.__year = year
    
    @property
    def pais(self):
        return self.__pais

    @pais.setter
    def pais(self, value):
        self.__year = value

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, value):
        self.__valor = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        self.__year = value        

class usuario:
    def __init__(self, monedas):
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
moneda1 = Moneda("Argentina", 1600, 1930)
moneda2 = Moneda("Argentina", 100, 2001)
moneda3 = Moneda("Chile", 100, 2001)

monedas = [moneda1, moneda2, moneda3]
user = usuario(monedas)

print("Paises: " + str(user.paises))
print("Valores: " + str(user.valores))
print("Años: " + str(user.years))