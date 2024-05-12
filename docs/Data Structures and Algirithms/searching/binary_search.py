# Function to implement binary search
def binary_search(arr, value):

    l = 0
    r = len(arr) - 1
    m = (l + r)//2

    while not (arr[m] == value) and l <= r:
        if value < arr[m]:
            r = m - 1
        else:
            l = m + 1
        m = (l + r) // 2
    if arr[m] == value:
        return m
    else:
        return -1


print(binary_search([11,22,33,44,55,66,77,88], 44))