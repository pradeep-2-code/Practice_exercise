def pascals_triangle(n):
    triangle = []

    for i in range(n):
        row = [1] * (i + 1)

        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        triangle.append(row)

    return triangle


n = 5
output = pascals_triangle(n)
for row in output:
    print(row)
