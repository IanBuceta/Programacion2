from random import randint
from os import system
from statistics import mean

system("cls")
minimo = 1
maximo = 6

resultados = list()


tiradas = int(input("Ingrese numero de tiradas: "))

for tirada in range(tiradas):
    resultados.append(randint(minimo,maximo) + randint(minimo, maximo))

system("cls")
for numero in range(2, 13):
    print("Cantidad de veces que salio {}: {}. Porcentaje total: {}".format(numero, resultados.count(numero), resultados.count(numero) * 100 / len(resultados)))