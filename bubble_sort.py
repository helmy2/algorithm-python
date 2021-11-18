from swap import *


def bubbleSort(array):
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                swap(array, j, j + 1)


data = [1, 5, 9, 4, 5, 6]
print(data)
bubbleSort(data)
print(data)
