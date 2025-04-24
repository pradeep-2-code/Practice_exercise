# Question:
# Given a nested list of integers, flatten it into a single list using a nested for loop in one line.
# Input:
# nested_list = [[1, 2, 3], [4, 5], [6, 7, 8]]
# Expected Output:
# [1, 2, 3, 4, 5, 6, 7, 8]
nested_list = [[1, 2, 3], [4, 5], [6, 7, 8]]
print([w for s in nested_list for w in s])
