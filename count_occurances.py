# Count Occurrences of Characters in a String (Using Dictionary & Loop)
# Question:
# Write a function that counts how many times each character appears in a given string.
# Input:
# text = "banana"
# Expected Output:
# {'b': 1, 'a': 3, 'n': 2}
def function_count(str):
    dict = {}
    for i in str:
        dict[i] = str.count(i)
    return dict


print(function_count("Banana"))
