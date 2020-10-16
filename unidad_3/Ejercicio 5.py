from sys import getsizeof

numList = [1,2,3,4,5]
print("Lista + 1:")
#List comprehension
mappedList = [num for num in map(lambda numero: numero + 1, numList)]
print(mappedList)
print("Size of listComprehension: ", getsizeof(mappedList))