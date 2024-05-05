# Function to implement selection sort
def selection_sort(customList):

    for i in range(len(customList)):
        min_index = i
        for j in range(min_index, len(customList)):
            if customList[min_index] > customList[j]:
                min_index = j
            
        customList[i], customList[min_index] = customList[min_index], customList[i]
        
    return(customList)

print(selection_sort([1,3,4,2,5,3,2,9,1,-1,0]))
    