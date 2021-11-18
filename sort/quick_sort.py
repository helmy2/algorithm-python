from swap import swap


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            swap(arr, i, j)

    swap(arr, i + 1, high)

    return i + 1


def quick_sort(arr, low, high):
    if low > high:
        return

    loc = partition(arr, low, high)

    quick_sort(arr, low, loc - 1)

    quick_sort(arr, loc + 1, high)


if __name__ == '__main__':
    array = [6, 5, 12, 10, 9, 1]

    print("Unsorted array is: ")
    print(array)
    quick_sort(array, 0, len(array) - 1)
    print("Sorted array is: ")
    print(array)
