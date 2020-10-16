numList = [1,2,3,4,5]


print("Numeros Multiplo de 5:")

#Formato lambda = lambda nVariables: codigo
numFilter = filter(lambda numero: numero%5 == 0, numList)
for num in numFilter:
    print(num)
