def insert_at_start(tup1, ele):

    ret_tup = (ele,) + tup1
    return ret_tup

print(insert_at_start((2, 3, 4), 1))