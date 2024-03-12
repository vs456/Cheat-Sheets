def rotate_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in matrix:
        row.reverse()
    
    return(matrix)

print(rotate_matrix([[1,2,3],[4,5,6],[7,8,9]]))