# Function to check if the elements of an array are odd or even
# Callback Function
def isOdd(num):
    if num%2==0:
        return False
    else:
        return True
    
def someRecursive(arr, cb):

# If null array is passed, then return false
    if len(arr) == 0:
        return False
# Remove the first element and call the function recursively
    if not(cb(arr[0])):
        return someRecursive(arr[1:], cb)
# Once the above recursion ends fully, return True, in case even element is detected Line 12 gets called.
    return True

print(someRecursive([], isOdd))