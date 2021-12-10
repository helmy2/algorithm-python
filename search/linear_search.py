def linear_search(array, number):
    for i in range(len(array)):
        if array[i] == number:
            return i
    return -1


if __name__ == '__main__':
    arr = [2, 4, 0, 1, 9]
    x = 1
    result = linear_search(arr, x)
    if result == -1:
        print("Element not found")
    else:
        print("Element found at index: ", result)
