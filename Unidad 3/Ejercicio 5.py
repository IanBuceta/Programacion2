numList = [1,2,3,4,5]
print("Lista + 1:")
mappedList = [num for num in map(lambda numero: numero + 1, numList)]
print(mappedList)