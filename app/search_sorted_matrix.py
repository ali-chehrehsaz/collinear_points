def search_sorted_matrix(matrix, target):

    if not matrix: return False

    m = len(matrix)  # num of rows
    n = len(matrix[0])  # num of clms

    # Start from bottom left corner
    j = 0  # ptr for clm
    i = m - 1  # ptr for row

    while j < n and i >= 0:
        curr = matrix[i][j]
        if target == curr:
            return True
        if target > curr:
            j += 1
            continue
        else:
            i -= 1
            continue

    return False


if __name__ == "__main__":
    m = [[1, 3, 4, 5], [11, 31, 41, 51]]

    assert search_sorted_matrix(m, 1)
    assert search_sorted_matrix(m, 3)
    assert search_sorted_matrix(m, 4)
    assert search_sorted_matrix(m, 5)
    assert search_sorted_matrix(m, 1)
    assert search_sorted_matrix(m, 31)
    assert search_sorted_matrix(m, 41)
    assert search_sorted_matrix(m, 51)

    assert not search_sorted_matrix(m, 12)
    assert not search_sorted_matrix(m, 413)
    assert not search_sorted_matrix(m, 513)

    m = [[1, 3, 4, 5], [11, 31, 41, 51]]

    assert search_sorted_matrix(m, 5)
    assert not search_sorted_matrix(m, 12)

