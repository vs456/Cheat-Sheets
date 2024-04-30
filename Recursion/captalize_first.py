# Function to capitalize the first letter of an array of strings
def capitalizefirst(arr):

    result = []
# If array becomes 0, return the result array, and exit
    if len(arr)==0:
        return result
    # Else capitalize the first element and move on
    else:
        result.append(arr[0][0].upper()+arr[0][1:])
    
    return result + capitalizefirst(arr[1:])

print(capitalizefirst(['car', 'taco', 'banana']))
