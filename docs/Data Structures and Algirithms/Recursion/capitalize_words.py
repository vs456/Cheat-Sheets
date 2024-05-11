# Function to capitalize all letters in an array of words(works with even nested arrays)
def capitalizewords(arr):

    result = []
    if len(arr) == 0:
        return arr 
    else:
        result.append(arr[0].upper())
        return result + capitalizewords(arr[1:])
    
print(capitalize_words(['i', 'am', ['Learning'], 'recursion']))