def power_of_number(n, m):

    assert int(m) == m, "The power should be an integer"
    # If the power becomes 1, return back the same number
    if m == 1:
        return n
    # If the power becomes 0, return back 1 since num^0 = 1
    elif m == 0:
        return 1
    # If the power is negative, then pattern becomes 1/(number * (reduce the power by 1 for the number(-1-1 = -2)))
    elif m < 0:
        return 1/n * power_of_number(n, m+1)
    # pattern here is number * (reduce the power by 1 for the number)
    else:
        return n * power_of_number(n, m-1)
    
print(power_of_number(5, -2))