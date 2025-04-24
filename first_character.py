# Question:
# Given a string, find the first character that does not repeat in the string using a for loop.
# Input:
# text = "swiss"
# Expected Output:
# "w"
text = "swiss"
for x in text:
    if text.count(x) == 1:
        print(x)
        break
