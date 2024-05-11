# Function to calculate sum of n elements
def sum_of_integers(a):

    if a <= 0:
        return 0
    else:
        # Logic is add the number to the recursive sum of n-1 numbers
        return a + sum_of_integers(a-1)
    
print(sum_of_integers(2.5))