# Write a function to perform matrix multiplication for two N x N matrices using nested loops.
# Input:
# A = [[1, 2],
#      [3, 4]]

# B = [[5, 6],
#      [7, 8]]
# Expected Output:

# [[19, 22],
#  [43, 50]]
a = [[1, 2], [3, 4]]
b = [[5, 6], [7, 8]]
result = [[0, 0], [0, 0]]
for i in range(2):
    for j in range(2):
        result[i][j] = a[i][0] * b[0][j] + a[i][1] * b[1][j]
print(result)
