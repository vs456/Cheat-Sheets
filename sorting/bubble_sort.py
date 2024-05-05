# Function to implement bubble sorting
def bubble_sort(customList):

    for i in range(len(customList)-1):
        for j in range(len(customList)-i-1):
            if customList[j] > customList[j+1]:
                customList[j], customList[j+1] = customList[j+1], customList[j]
    
    return customList

print(bubble_sort([1,3,4,2,5,3,2,9,1]))
