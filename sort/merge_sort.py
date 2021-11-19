# Best              O(n*log n)
# Worst             O(n*log n)
# Average           O(n*log n)
# Space Complexity  O(n)

def merge_sort(arr):
    if len(arr) <= 1:
        return

    #  mid_index is the point where the array is divided into two sub arrays
    mid_index = len(arr) // 2
    right_array = arr[:mid_index]
    left_array = arr[mid_index:]

    # Sort the two halves
    merge_sort(right_array)
    merge_sort(left_array)

    merge(arr, left_array, right_array)


def merge(arr, left_array, right_array):
    right_index = left_index = index = 0

    # Until we reach either end of either rightArray or leftArray, pick larger among
    # elements rightArray and leftArray and place them in the correct position at A[p..midIndex]
    while right_index < len(right_array) and left_index < len(left_array):
        if right_array[right_index] < left_array[left_index]:
            arr[index] = right_array[right_index]
            right_index += 1
        else:
            arr[index] = left_array[left_index]
            left_index += 1
        index += 1

    # When we run out of elements in either rightArray or leftArray,
    # pick up the remaining elements and put in A[p..midIndex]
    while right_index < len(right_array):
        arr[index] = right_array[right_index]
        right_index += 1
        index += 1
    while left_index < len(left_array):
        arr[index] = left_array[left_index]
        left_index += 1
        index += 1


if __name__ == '__main__':
    array = [6, 5, 12, 10, 9, 1]

    print("Unsorted array is: ")
    print(array)

    merge_sort(array)
    print("Sorted array is: ")
    print(array)
