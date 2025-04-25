# Question:
# Swap keys and values in a dictionary.
# Input:
grades7 = {"Alice": 85, "Bob": 92, "Charlie": 78}
# Expected Output:
# {85: "Alice", 92: "Bob", 78: "Charlie"}
dic = {}
for k, v in grades7.items():
    dic[v] = k
print(dic)
