# Function to find the greatest common divisor, or greater common factor of two numbers
def gcd(n, m):

    # Limit the numbers to integers only
    assert int(n) == n and int(m) == m, "Only integers are allowed"
    # GCD of negative numbers is same as gcd of positive numbers
    if n < 0:
        n *= -1
    if m < 0:
        m *= -1
    # Logic here is that if you keep dividing the divisor by the remainder, the gcd will be the remainder which after the division gives 0 remainder 
    if m == 0:
        return n
    else:
        return gcd(m, n%m)
    
print(gcd(18, 48))