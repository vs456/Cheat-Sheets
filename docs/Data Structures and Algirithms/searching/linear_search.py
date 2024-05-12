# Function to implement linear search
def linearsearch(arr, value):

    for i in arr:
        if i == value:
            return arr.index(i)
    return -1


print(linearsearch([11,22,33,44,55,66,77,88], 4))