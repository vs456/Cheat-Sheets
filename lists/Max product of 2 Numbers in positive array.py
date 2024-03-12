def max_product(array):
    return (sorted(array)[-1]*sorted(array)[-2])

print(max_product([1, 7, 3, 4, 9, 5]))