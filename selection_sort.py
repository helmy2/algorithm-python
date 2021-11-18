from swap import *


def selectionSort(array):
    for i in range(len(array)):
        minIndex = i
        for j in range(i, len(array)):
            if array[j] < array[minIndex]:
                minIndex = j
        swap(array, i, minIndex)


data = [1, 5, 9, 4, 5, 6]
print(data)
selectionSort(data)
print(data)
