# Best              O(n)
# Worst             O(n2)
# Average           O(n2)
# Space Complexity  O(1)

from swap import *


def bubble_sort(arr):
    for i in range(len(arr)):
        swapped = False
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                swap(arr, j, j + 1)
                swapped = True
        if swapped:
            break


if __name__ == '__main__':
    array = [6, 5, 12, 10, 9, 1]

    print("Unsorted array is: ")
    print(array)

    bubble_sort(array)
    print("Sorted array is: ")
    print(array)
