def best_scores(array):
    return (sorted(set(array))[-1], sorted(set(array))[-2])

print(best_scores([84,85,86,87,85,90,85,83,23,45,84,1,2,0]))