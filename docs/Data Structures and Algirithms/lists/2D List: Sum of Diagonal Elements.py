def diagonal_element_sum(arrary):
    sum = 0
    for i in range(len(arrary)):
        sum+= arrary[i][i]
    return sum

print(diagonal_element_sum([[1,2,3],[4,5,6],[7,8,9]]))