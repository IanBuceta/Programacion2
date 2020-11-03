from os import system
from statistics import mean

lista = list()
while(True):
    lista.append(float(input("Ingrese precio de compra: ")))
    if str.lower(input("¿Desea continuar? ")) == "no":
        break

system("cls")
print("Mayor Compra: {:.2f}".format(max(lista)))
print("Menor compra: {:.2f}".format(min(lista)))
print("Promedio de compras: {:.2f}".format(mean(lista)))