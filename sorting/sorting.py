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

# print(bubble_sort([1,3,4,2,5,3,2,9,1]))
# print(selection_sort([1,3,4,2,5,3,2,9,1,-1,0]))
print(insertion_sort([1,3,4,2,5,3,2,9,1,-1,0]))

