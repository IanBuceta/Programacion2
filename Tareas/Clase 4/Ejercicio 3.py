from os import system

def imprimirdict():
    print(persona)

camposPersona = ("nombre", "apellido", "sexo","pais", "documento", "telefono", "correo electronico")
persona = dict()

for campo in camposPersona:
    system("cls")
    persona[campo] = input("Ingrese {}: ".format(campo))
    imprimirdict()
    input()