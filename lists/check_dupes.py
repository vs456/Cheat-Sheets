def check_dupes(array):
    return (len(array) == len(set(array)))

print(check_dupes([1,2,3,1]))

print(check_dupes([1,2,3,5,6,7,8]))