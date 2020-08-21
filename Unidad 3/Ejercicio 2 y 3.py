from functools import reduce

numList = [1,2,3,4,5]

#Filter
numFilter = filter(lambda numero: numero%5 == 0, numList)
for num in numFilter:
    print(num)

#Map
numMap = map(lambda numero: numero + 1, numList)

numList = []
for num in numMap:
    numList.append(num)

print(numList)

#Reduce
print("Elementos de la lista")