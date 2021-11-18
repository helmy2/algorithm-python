from swap import *


def insertion_sort(arr):
    for i in range(len(arr)):
        j = i - 1
        while j >= 0 and arr[j] > arr[j + 1]:
            swap(arr, j, j + 1)
            j = j - 1


if __name__ == '__main__':
    array = [6, 5, 12, 10, 9, 1]

    print("Unsorted array is: ")
    print(array)

    insertion_sort(array)
    print("Sorted array is: ")
    print(array)
