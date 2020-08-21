class persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre
    
    @property
    def apellido(self):
        return self.__apellido
    
    @apellido.setter
    def apellido(self, apellido):
        self.__apellido = apellido


fulano = persona("fulano", "de tal")
print("Datos de la persona: " + fulano.nombre + " " + fulano.apellido)
