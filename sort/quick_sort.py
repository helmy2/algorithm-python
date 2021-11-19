# Best              O(n*log n)
# Worst             O(n2)
# Average           O(n*log n)
# Space Complexity  O(log n)


from swap import swap


# function to find the partition position
def partition(arr, low, high):

    # choose the rightmost element as pivot
    pivot = arr[high]

    # pointer for greater element
    i = low

    for j in range(low, high):
        if arr[j] <= pivot:
            # if element smaller than pivot is found
            # swapping element at i with element at j
            swap(arr, i, j)
            i = i + 1

    # swap the pivot element with the greater element specified by i
    swap(arr, i, high)

    # return the position from where partition is done
    return i


def quick_sort(arr, low, high):
    if low > high:
        return

    pi = partition(arr, low, high)

    quick_sort(arr, low, pi - 1)

    quick_sort(arr, pi + 1, high)


if __name__ == '__main__':
    array = [6, 5, 12, 10, 9, 1]

    print("Unsorted array is: ")
    print(array)
    quick_sort(array, 0, len(array) - 1)
    print("Sorted array is: ")
    print(array)
