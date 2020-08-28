from functools import reduce

numList = [1,2,3,4,5]

#Filter
print("Numeros Multiplo de 5:")
numFilter = filter(lambda numero: numero%5 == 0, numList)
for num in numFilter:
    print(num)

#Map
print("Lista + 1:")
numMap = map(lambda numero: numero + 1, numList)

numList = []
for num in numMap:
    numList.append(num)

print(numList)

#Reduce
print("Suma de elementos de la lista: ", end="")
print(reduce(lambda a,b: a+b, numList))