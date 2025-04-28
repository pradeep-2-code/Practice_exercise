def spiral_traversal(matrix):
    result = []
    while matrix:
        result += matrix.pop(0)
        for row in matrix:
            if row:
                result.append(row.pop())
        if matrix:
            result += matrix.pop()[::-1]
        for row in reversed(matrix):
            if row:
                result.append(row.pop(0))
    return result


matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

print(spiral_traversal(matrix))
