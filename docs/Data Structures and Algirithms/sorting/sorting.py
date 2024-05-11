from math import ceil, sqrt

# Function to implement bubble sorting
def bubble_sort(customList):

    for i in range(len(customList)-1):
        for j in range(len(customList)-i-1):
            if customList[j] > customList[j+1]:
                customList[j], customList[j+1] = customList[j+1], customList[j]
    
    return customList

# Function to implement selection sort
def selection_sort(customList):

    for i in range(len(customList)):
        min_index = i
        for j in range(min_index, len(customList)):
            if customList[min_index] > customList[j]:
                min_index = j
            
        customList[i], customList[min_index] = customList[min_index], customList[i]
        
    return(customList)
    
#  Function to implement insertion sort
def insertion_sort(customList):

    for i in range(1, len(customList)):
        j = i
        while j > 0 and customList[j-1] > customList[j]:
            customList[j], customList[j-1] = customList[j-1], customList[j]
            j -= 1
    
    return customList

# Function to implement bucket sort, only works real numbers
def bucket_sort(customList):

    num_buckets = round(sqrt(len(customList)))
    buckets = [[] for _ in range(num_buckets)]
    max_num = max(customList)

    for i in customList:
        buckets[(ceil((i*num_buckets)/max_num)-1)].append(i)
    
    for i in buckets:
        insertion_sort(i)
    
    customList = []
    for i in buckets:
        customList.extend(i)
        
    return customList

# Function to implement merge sorting
# Funtion to sort & merge the sub arrays 
def merge(customList, l, m, r):

    n1 = m - l + 1
    n2 = r - m

    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0, n1):
        L[i] = customList[l + i]
    
    for j in range(0, n2):
        R[j] = customList[m + 1 + j]

    i = 0
    j = 0
    k = l

    while i < n1 and j < n2:

        if L[i] <= R[j]:
            customList[k] = L[i]
            i += 1
        else:
            customList[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        customList[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        customList[k] = R[j]
        j += 1
        k += 1

# Fucntion to divide the array in sub arrays recursively, and at last merge the sub arrays
def merge_sort(customlist, l, r):

    if l < r:
        m = l+(r-l)//2   # Can use (l+r)//2 but it overflows for large l and r
        merge_sort(customlist, l, m)
        merge_sort(customlist, m + 1, r)
        merge(customlist, l, m, r)

    return customlist


# print(bubble_sort([1,3,4,2,5,3,2,9,1]))
# print(selection_sort([1,3,4,2,5,3,2,9,1,-1,0]))
# print(insertion_sort([1,3,4,2,5,3,2,9,1,-1,0]))
# print(bucket_sort([1,3,4,2,5,3,2,9,1,-1,0]))
print(merge_sort([1,3,4,2,5,3,2,9,1,-1,0], 0, 10))
