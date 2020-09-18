from typing import List


class supermercado:

    def __init__(self, nombre):
        self.__nombre = "Walmart"
        self.__opciones = {
            "1. Agregar Cliente": self.agregar_cliente(),
            "2. Cobrar Cliente": self.cobrar_cliente(),
            "3. Mostrar Clientes Encolados en una caja": self.mostrar_clientes_encolados_en_caja(),
            "4. Mostrar Clientes Atendidos en una caja": self.mostrar_clientes_atendidos_en_caja(),
            "5. Mostrar Todos los Clientes Encolados": self.mostrar_todos_clientes_encolados(),
            "6. Mostrar Todos los Clientes Atendidos": self.mostrar_todos_clientes_atendidos(),
            "7. Mostrar Monto Sin Cobrar en una caja": self.mostrar_monto_sin_cobrar_en_caja(),
            "8. Mostrar Monto Obtenido en una caja": self.mostrar_monto_cobrado_en_caja(),
            "9. Mostrar Monto Total Sin Cobrar": self.mostrar_monto_total_sin_cobrar(),
            "10. Mostrar Monto Total Obtenido": self.mostrar_monto_total_cobrado()
        }
        self.__cajas = list(List[caja])
        self.generar_cajas()

    def menu(self):
        for opcion in self.__opciones:
            print(opcion)
        opcion_elegida = int(input("Seleccione una acción:"))

    def generar_cajas(self):
        cantidad_de_cajas = int(input("Ingrese numero de cajas: "))
        cajas = list()

        for i in range(cantidad_de_cajas):
            cajas.append(caja(i))

        self.__cajas = set(cajas)

    def obtener_caja(self):
        return self.__cajas[int(input("Ingrese número de la caja"))]

    def agregar_cliente(self):
        caja = self.obtener_caja()
        nombre = input("Ingrese nombre del cliente: ")
        monto = float(input("Ingrese monto del cliente: "))
        caja.encolar_cliente(cliente(nombre, monto))

    def cobrar_cliente(self):
        caja = self.obtener_caja()
        caja.cobrar()

    def mostrar_clientes_encolados_en_caja(self):
        caja = self.obtener_caja()
        print(caja.clientes_atendidos)

# CAMBIAR
    def mostrar_todos_clientes_encolados(self):
        caja = self.obtener_caja()
        print(caja.clientes_atendidos)

    def mostrar_clientes_atendidos_en_caja(self):
        caja = self.obtener_caja()
        print(caja.clientes_atendidos)

    def mostrar_todos_clientes_atendidos(self):
        caja = self.obtener_caja()
        print(caja.clientes_atendidos)

    def mostrar_monto_sin_cobrar_en_caja(self):
        caja = self.obtener_caja()

    def mostrar_monto_cobrado_en_caja(self):
        caja = self.obtener_caja()

    def mostrar_monto_total_cobrado(self):
        caja = self.obtener_caja()

    def mostrar_monto_total_sin_cobrar(self):
        caja = self.obtener_caja()


class cliente:
    def __init__(self, nombre: str, monto: float):
        self.__nombre = nombre
        self.__monto = monto

    @property
    def nombre(self):
        return self.__nombre

    @property
    def monto(self):
        return self.__monto


class caja:

    __clientes_encolados = list(List[cliente])
    __clientes_atendidos = list(List[cliente])

    def __init__(self, numero: int):
        self.__numero = numero

    def encolar_cliente(self, cliente: cliente):
        self.__clientes_encolados.append(cliente)

    def cobrar(self):
        self.__clientes_atendidos.append(self.__clientes_encolados.pop(0))

    @property
    def clientes_atendidos(self):
        return len(self.__clientes_atendidos)

    @property
    def clientes_encolados(self):
        return len(self.__clientes_encolados)

    @property
    def monto_obtenido(self):
        return sum(i.monto for i in self.__clientes_atendidos)
