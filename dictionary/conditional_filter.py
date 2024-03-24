def conditional_filter(dict1, condition):

    return { k: v for k, v in dict1.items() if condition(k,v)}

print(conditional_filter({'a': 1, 'b': 2, 'c': 3, 'd': 4} , lambda k, v: v % 2 == 0))