def pair_sum(array, num):
    final_pairs = []
    for i in range(len(array)):
        if array[i] > num:
            break
        else:
            if num-array[i] in array and num-array[i] !=array[i+1] and num-array[i] !=array[i-1]:
                final_pairs.append([array[i], num-array[i]])

    return list(final_pairs)

print(pair_sum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9],7))
