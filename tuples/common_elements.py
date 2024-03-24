def common_elements(tup1, tup2):

    return(tuple(x for x in tup1 if x in tup2))

print(common_elements((1, 2, 3, 4, 5),(4, 5, 6, 7, 8)))