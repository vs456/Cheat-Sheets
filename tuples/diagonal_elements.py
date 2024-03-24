def diagonal_elements(tup1):

    return (tuple(tup1[i][i] for i in range(len(tup1))))

print(diagonal_elements((
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)))