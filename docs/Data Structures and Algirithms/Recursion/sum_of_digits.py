def sum_of_digits(n):

    # Check the number has to be postive and integer
    assert n > 0 and int(n) == n, "Number has to be positive"
    # If the number becomes less than 10, return back the number
    if n < 10:
        return n
    # The pattern here is sum = remainder + sum of digits of the quotient.
    return int(n%10) + sum_of_digits(n//10)


print(sum_of_digits(21121))
