# Write a nested loop that generates all prime numbers from 2 to 50.
# Input:

# n = 20
# Expected Output:

# [2, 3, 5, 7, 11, 13, 17, 19]
a = int(input("Enter the number"))
res = []
for i in range(2, a + 1):
    if i <= 1:
        continue
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        res.append(i)

print(res)
