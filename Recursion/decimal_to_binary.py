# Function to convert decimal to binary
def dtb(a):

    assert int(a) == a, "only integers are allowed"
    if a == 0:
        return 0
    else:
        # Logic here is 11/2 = 1(remainder) + 10 * 5(quotient, which will again be divided by 2)
        return a%2 + 10 * dtb(int(a/2))

print(dtb(13))