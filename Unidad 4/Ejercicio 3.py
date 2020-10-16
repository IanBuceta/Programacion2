with open("holamundo.txt", "a") as file:
    file.write(input("Ingrese algo para anotar: ") + "\n")
with open("holamundo.txt") as file:
    print("Cosas escritas en {}".format(file.name))
    for line in file.readlines():
        print(line)
