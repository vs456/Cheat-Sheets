def find_missing_number(array):
    array_sum = sum(array)
    print(array_sum)
    sum_of_all_continuous_numbers = ((len(array)+1)*(len(array)+2))/2   # Since length of array is reduced by 1 element
    print(sum_of_all_continuous_numbers)

    return int(sum_of_all_continuous_numbers-array_sum)

print(find_missing_number([1, 2, 3, 4, 6]))