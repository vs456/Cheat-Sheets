def sum_prod(tup1):

    prod = 1
    for i in tup1:
        prod *= i

    return sum(tup1), prod

print(sum_prod((1, 2, 3, 4)))