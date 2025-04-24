# Question:
# Write a Python program that takes a list of integers and returns the sum of all even numbers using a one-liner for loop.
# Input:
# numbers = [3, 8, 12, 5, 9, 14, 7]
# Expected Output:
# 34  # (8 + 12 + 14)
numbers = [3, 8, 12, 5, 9, 14, 7]
print(sum([x for x in numbers if x % 2 == 0]))
