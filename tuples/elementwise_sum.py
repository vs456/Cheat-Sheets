def elementwise_sum(tup1, tup2):
    prod_tup = []
    if len(tup1)!=len(tup2):
        return("tuple length not matching")
    else:
        for i in range(len(tup1)):
            prod_tup.append(tup1[i]+tup2[i])

    return tuple(prod_tup)

print(elementwise_sum((1, 2, 3),(4, 5, 6)))
