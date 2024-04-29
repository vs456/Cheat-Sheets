# Function to calculate product of all elements of array
def product_of_array(arr):
    
    if not arr:
        return 1
    else:
        # Logic here is to seperate the first element and then recusively call the function for the remaining array
        return arr[0] * product_of_array(arr[1:])
    
print(product_of_array([2]))