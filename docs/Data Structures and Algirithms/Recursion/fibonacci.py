# Gives the number in the fibonacci series at a specific index n
def fibonacci(n):

    # Check for the index, should be non negative, and not floating point
    assert n >= 0 and int(n)== n, "Fibonacci number can not be negative or floating point"
    # If n becomes 0 or 1, return back the value
    if n in [0,1]:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(7))