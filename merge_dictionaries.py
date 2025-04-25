# Question:
# Combine two dictionaries, ensuring that the second dictionary overwrites duplicate keys.
# Input:
dict1 = {"Alice": 85, "Bob": 92}
dict2 = {"Charlie": 88, "Bob": 95}
# Expected Output:
# {"Alice": 85, "Bob": 95, "Charlie": 88}
dict1.update(dict2)
print(dict1)
