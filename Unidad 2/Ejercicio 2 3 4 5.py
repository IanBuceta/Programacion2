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

class estudiante(persona):
    def __init__(self, nombre, apellido, codigo):
        super().__init__(nombre, apellido)
        self.codigo = codigo

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

class empleado():
    def __init__(self, titulo):
        self.titulo = titulo

    @property
    def titulo(self):
        return self.__titulo
    
    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

class profesor(estudiante, empleado):
    def __init__(self, nombre, apellido, codigo, titulo):
        super(profesor, self).__init__(nombre, apellido, codigo)
        empleado.__init__(self, titulo)

fulano = persona("fulano", "de tal")
print("Datos de la persona: " + fulano.nombre + " " + fulano.apellido)

alumno = estudiante("fulano", "de tal", "a4fd4gf5")
print("Datos del estudiante: " + alumno.nombre + " " + alumno.apellido + " " + alumno.codigo)

maestro = profesor("bla", "blabla", "a15fsls433", "maestro")
print("Datos del estudiante: " + maestro.nombre + " " + maestro.apellido + " "+ maestro.codigo + " " + maestro.titulo)
