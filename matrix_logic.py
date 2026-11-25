def _validate_matrix(matrix):
    if not matrix or not matrix[0]:
        raise ValueError("Матрица не может быть пустой")


def check_zero_columns(matrix):
    _validate_matrix(matrix)
    n = len(matrix)
    m = len(matrix[0])
    result1 = []

    for k in range(m):
        flag = True
        for i in range(n):
            if matrix[i][k] != 0:
                flag = False
                break
        result1.append(flag)

    return result1


def check_decreasing_rows(matrix):
    _validate_matrix(matrix)
    n = len(matrix)
    m = len(matrix[0])
    result2 = []

    for k in range(n):
        flag = True
        for j in range(m - 1):
            if matrix[k][j] < matrix[k][j + 1]:
                flag = False
                break
        result2.append(flag)

    return result2