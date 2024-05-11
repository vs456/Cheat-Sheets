# Recursion function to calculate a factorial of a number
def factorial(n):

    # Constratint for checking negative numbers
    if n < 0:
        return None
    # If n is 0 or 1, limit the recursion, and return back 1 to the base function
    if n in [0, 1]:
        return 1
    # If n is not 0 or 1, call back the function with value of n-1
    else:
        return n * factorial(n-1)

print(factorial(500))