def SecuenciaCondicional():
    numero = 0
    if numero == 0:
        numero = 1
    elif numero == 1:
        numero = 2
    else:
        numero = 3
    print(numero)

def SecuenciaIterativa():
    for i in range(10):
        numero = i
    while(numero != 0):
        numero -= 1      
    print(numero)  

SecuenciaCondicional()
SecuenciaIterativa()