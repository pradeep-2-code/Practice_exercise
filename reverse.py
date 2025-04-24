# Write a Python function that reverses a string using only a for loop (without [::-1] or reversed()).
# Input:
# text = "Python"
# Expected Output:
# "nohtyP"


def my_function(st):
    res = ""
    for x in st:
        res = x + res
    return res


print(my_function("Python"))
