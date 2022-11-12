#Вернуть массив, состоящий только из неуникальных элементов данного массива.

def checkio(data):
    return list(filter(lambda x: data.count(x)>1, data))

print("Example:")
print(checkio([1, 2, 3, 1, 3]))
