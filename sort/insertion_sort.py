from swap import *


def insertionSort(array):
    for i in range(len(array)):
        j = i - 1
        while j >= 0 and array[j] > array[j + 1]:
            swap(array, j, j + 1)
            j = j - 1


data = [1, 5, 9, 4, 5, 6]
print(data)
insertionSort(data)
print(data)
