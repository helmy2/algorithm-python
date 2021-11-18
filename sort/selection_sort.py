from swap import *


def selection_sort(arr):
    for i in range(len(arr)):
        minIndex = i
        for j in range(i, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        swap(arr, i, minIndex)


if __name__ == '__main__':
    array = [6, 5, 12, 10, 9, 1]

    print("Unsorted array is: ")
    print(array)

    selection_sort(array)
    print("Sorted array is: ")
    print(array)
