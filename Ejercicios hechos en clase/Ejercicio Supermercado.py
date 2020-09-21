from os import system


class supermercado:

    def __init__(self, nombre):
        self.__nombre = nombre
        self.__cajas = list()
        self.generar_cajas()
        self.__opciones = {
            1: ("Agregar Cliente", self.agregar_cliente),
            2: ("Cobrar Cliente", self.cobrar_cliente),
            3: ("Mostrar Clientes Encolados en una caja", self.mostrar_clientes_encolados_en_caja),
            4: ("Mostrar Clientes Atendidos en una caja", self.mostrar_clientes_atendidos_en_caja),
            5: ("Mostrar Todos los Clientes Encolados", self.mostrar_todos_clientes_encolados),
            6: ("Mostrar Todos los Clientes Atendidos", self.mostrar_todos_clientes_atendidos),
            7: ("Mostrar Monto Sin Cobrar en una caja", self.mostrar_monto_sin_cobrar_en_caja),
            8: ("Mostrar Monto Obtenido en una caja", self.mostrar_monto_cobrado_en_caja),
            9: ("Mostrar Monto Total Sin Cobrar", self.mostrar_monto_total_sin_cobrar),
            10: ("Mostrar Monto Total Obtenido", self.mostrar_monto_total_cobrado)
        }

    def menu(self):
        system("cls")
        for opcionKey, opcionValue in self.__opciones.items():
            print("{}. {}".format(opcionKey, opcionValue[0]))

        opcion = int(input("Seleccione una opcion: "))
        self.__opciones[opcion][1]()

    def generar_cajas(self):
        system("cls")
        cantidad_de_cajas = int(input("Ingrese numero de cajas: "))
        cajas = list()

        for i in range(cantidad_de_cajas):
            cajas.append(caja(i))

        self.__cajas = list(cajas)

    def obtener_caja(self):
        system("cls")
        for caja in self.__cajas:
            print(caja.numero)

        return self.__cajas[int(input("Ingrese número de la caja: "))]

    def agregar_cliente(self):
        system("cls")
        caja = self.obtener_caja()
        nombre = input("Ingrese nombre del cliente: ")
        monto = float(input("Ingrese monto del cliente: "))
        caja.encolar_cliente(cliente(nombre, monto))
        print("Cliente Agregado")

    def cobrar_cliente(self):
        system("cls")
        caja = self.obtener_caja()
        caja.cobrar()
        print("Se le ha cobrado al cliente")

    def mostrar_clientes_encolados_en_caja(self):
        system("cls")
        caja = self.obtener_caja()
        print("Total de clientes encolados en caja:")
        print(caja.clientes_encolados)

    def mostrar_clientes_atendidos_en_caja(self):
        system("cls")
        caja = self.obtener_caja()
        print("Total de clientes atendidos en caja:")
        print(caja.clientes_atendidos)

    def mostrar_todos_clientes_encolados(self):
        system("cls")
        print("Total de clientes encolados:")
        print(sum(i.clientes_encolados for i in self.__cajas))

    def mostrar_todos_clientes_atendidos(self):
        system("cls")
        print("Total de clientes atendidos:")
        print(sum(i.clientes_atendidos for i in self.__cajas))

    def mostrar_monto_sin_cobrar_en_caja(self):
        system("cls")
        caja = self.obtener_caja()
        print("Monto Total sin cobrar en caja:")
        print(caja.monto_sin_cobrar)

    def mostrar_monto_cobrado_en_caja(self):
        system("cls")
        caja = self.obtener_caja()
        print("Monto Total cobrado en caja:")
        print(caja.monto_obtenido)

    def mostrar_monto_total_cobrado(self):
        system("cls")
        print("Monto Total cobrado:")
        print(sum(i.monto_obtenido for i in self.__cajas))

    def mostrar_monto_total_sin_cobrar(self):
        system("cls")
        print("Monto Total sin cobrar:")
        print(sum(i.monto_sin_cobrar for i in self.__cajas))


class cliente:
    def __init__(self, nombre: str, monto: float):
        self.__nombre = nombre
        self.__monto = monto

    @ property
    def nombre(self):
        return self.__nombre

    @ property
    def monto(self):
        return self.__monto


class caja:

    def __init__(self, numero: int):
        self.__numero = numero
        self.__clientes_encolados = list()
        self.__clientes_atendidos = list()

    def encolar_cliente(self, cliente: cliente):
        self.__clientes_encolados.append(cliente)

    def cobrar(self):
        aCobrar = self.__clientes_encolados.pop(0)
        self.__clientes_atendidos.append(aCobrar)

    @property
    def numero(self):
        return self.__numero

    @property
    def clientes_atendidos(self):
        return len(self.__clientes_atendidos)

    @property
    def clientes_encolados(self):
        return len(self.__clientes_encolados)

    @property
    def monto_obtenido(self):
        return sum(i.monto for i in self.__clientes_atendidos)

    @property
    def monto_sin_cobrar(self):
        return sum(i.monto for i in self.__clientes_encolados)


try:
    system("cls")
    super = supermercado("walmart")
    while True:
        super.menu()
        input()
except Exception as ex:
    system("cls")
    print(ex)
