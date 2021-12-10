# Binary Search in python


def binary_search(array, number, low, high):
    # Repeat until the pointers low and high meet each other
    while low <= high:

        mid = low + (high - low) // 2

        if array[mid] == number:
            return mid

        elif array[mid] < number:
            low = mid + 1

        else:
            high = mid - 1

    return -1


if __name__ == '__main__':
    arr = [3, 4, 5, 6, 7, 8, 9]
    x = 4

    result = binary_search(arr, x, 0, len(arr) - 1)

    if result != -1:
        print("Element is present at index " + str(result))
    else:
        print("Not found")
