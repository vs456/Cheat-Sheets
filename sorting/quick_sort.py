# Functions to implement quick sort
# Quick sort can be implemeneted in various ways, depending on the way of the pivot selection
    
# Here the pivot is the last element in the array.
def partition_last(arr, left, right):

    pivot = arr[right]
    i = left
    j = right - 1

    # Loop till j is to the right of i
    while i < j:
        # Loop to move i to right and check for an element greater than pivot
        while i < right and arr[i] < pivot:
            i += 1
        # Loop to move j to left, and check for an element less than equal to pivot
        while j >= left and arr[j] >= pivot:
            j -= 1
        # Condition if j is still to right of i, swap arr[i] and arr[j]
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    # In any case, pivot gets swapped with the last value of i, which is the correct position of pivot in the array
    if arr[i] > pivot:    
        arr[i], arr[right] = arr[right], arr[i]

    # Return the position, so that we can recursively call the same function for the left subarray and right subarray
    return i

def quick_sort_pivotlast(arr, left, right):

    # Get the position for the pivot
    pos = partition_last(arr, left, right)
    # Recursive call for the left subarray
    partition_last(arr, left, pos-1)
    # Recursive call for the right subarray
    partition_last(arr, pos + 1, right)

    return arr

arr = [22,11,88,66,55,77,33,44,-22,0]
# right is len(array)-1, i.e. index of the last element
# print(quick_sort_pivotlast(arr, 0, len(arr)-1))

# Here the pivot is the first element in the array.
def partition_first(arr, left, right): 

    pivot = arr[left]
    i = left + 1
    j = right

    while j > i:
        while i < right and arr[i] >= pivot:
            i += 1
        while j > left + 1 and arr[j] < pivot:
            j -= 1
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
    arr[i], pivot = pivot, arr[i]

    return i

def quick_sort_pivotfirst(arr, left, right):

    # Get the position for the pivot
    pos = partition_first(arr, left, right)
    # Recursive call for the left subarray
    partition_first(arr, left, pos-1)
    # Recursive call for the right subarray
    partition_first(arr, pos + 1, right)

    return arr
print(quick_sort_pivotfirst(arr, 0, len(arr)-1))
