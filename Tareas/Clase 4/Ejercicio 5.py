from os import system
productosCosmeticos = list()
preciosUnitarios = list()
ventas = dict()

def cargarproductos():
    while(True):
        system("cls")
        productosCosmeticos.append(input("Ingrese nombre del producto: ").lower())
        preciosUnitarios.append(float(input("Ingrese costo unitario: ")))
        if input("¿Desea seguir ingresando elementos?: ").lower() == "no":
            break

def realizarventas():
    numeroFactura = 1

    while(True):
        system("cls")
        for (i, productoCosmetico) in enumerate(productosCosmeticos):
            print("{}. {}. Precio unitario: {:.2f} ".format(i, productoCosmetico,preciosUnitarios[i]))

        while (True):
            index = int(input("Seleccione el codigo producto deseado: "))
            if index < len(productosCosmeticos):
                break
            
        cantidad = int(input("Ingrese cantidad deseada: "))
        ventas[numeroFactura] = (productosCosmeticos[index], preciosUnitarios[index], cantidad)
        numeroFactura += 1

        if input("¿Desea seguir comprando?: ").lower() == "no":
            break
    
def mostrarventas():
    total = 0
    subtotal = 0
    system("cls")
    for key in ventas.keys():
        datosVenta = ventas[key]
        subtotal = datosVenta[1] * datosVenta[2]
        total += subtotal
        print("Numero de factura: {}. Nombre del producto: {}. Precio unitario:{:.2f}. Cantidad: {}.Subtotal: {:.2f}".format(key, datosVenta[0], datosVenta[1], datosVenta[2], subtotal))
        subtotal = 0
    print("Total vendido: {:.2f}".format(total))

cargarproductos()
realizarventas()
mostrarventas()
input()