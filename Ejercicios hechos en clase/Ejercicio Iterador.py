class iterador_de_primos:

    def __init__(self, max):
        self.max = max
        self.primos = self.obtener_numeros_primos(max)
        self.inicio = 1

    def __iter__(self):
        self.inicio = 1
        return self

    def __next__(self):
        if self.inicio < len(self.primos):
            primo = self.primos[self.inicio]
            self.inicio += 1
            return primo
        else:
            raise StopIteration

    def obtener_numeros_primos(self, max):
        max += 1
        numeros = list()
        for num in range(1, max):
            contador = 0
            temp = num
            num += 1
            for x in range(1, num):
                if temp % x == 0:
                    contador += 1
            if contador == 2:
                numeros.append(temp)
        return numeros


primos = iterador_de_primos(10)
iterador = iter(primos)
for primo in iterador:
    print(primo)
