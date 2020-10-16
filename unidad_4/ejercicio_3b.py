with open("holamundo_binario.txt", "ab+") as file:
    file.write((input("Ingrese algo para anotar: ") + "\n").encode())
    print("Cosas escritas en {}:".format(file.name))
    file.seek(0)
    for line in file.readlines():
        print(line.decode())
