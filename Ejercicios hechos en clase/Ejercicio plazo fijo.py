from os import system

def calcularPlazoFijo(cantidad, interes, tiempo):
    return (float(cantidad) * float(interes) * float(tiempo))/36500

def clear():
    system("cls")

seguirInvirtiendo = "si"
while(seguirInvirtiendo == "si"):
    clear()
    cantidad = input("Ingrese cantidad: ")
    interes = input("Ingrese interes: ")
    tiempo = input("Ingrese lapso de tiempo (en dias): ")

    plazoFijo = calcularPlazoFijo(cantidad, interes, tiempo)
    capitalTotal = (float(cantidad) + plazoFijo)
    
    textoPf = "El plazo fijo es de: {:.2f}"
    textCapitalTotal = "El capital total es de {:.2f}"
    print(textoPf.format(plazoFijo))
    print(textCapitalTotal.format(capitalTotal))

    seguirInvirtiendo = str.lower(input("¿Seguir invirtiendo? (si/no): "))
    clear()