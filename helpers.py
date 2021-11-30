def matrix_mult(matrix, vector):
    #matrix will be dictionary of dictionaries
    #vector will be list
    new_dict = {}
    row_names = list(matrix.keys())
    for i in range(len(row_names)):
        num = 0
        column_names = list(matrix[row_names[i]].keys())
        for j in range(len(column_names)):
            num = num + vector[j]*matrix[row_names[i]][column_names[j]]
        new_dict[row_names[i]] = num
    return new_dict
