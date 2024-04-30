# Create a function to flatten an array of array, and return the final array
def flatten(arr):

    resultarr = []
    for i in arr:
    # Check if the element is of type list, then extend the result array
        if type(i) is list:
            resultarr.extend(flatten(i))
            # Else append the result array
        else:
            resultarr.append(i)
    return resultarr

print(flatten([[[[1], [[[2]]], [[[[[[[3]]]]]]]]]]))