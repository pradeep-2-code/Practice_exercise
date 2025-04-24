# Write a Python program to print the following pattern using nested loops:
# markdown

# *
# **
# ***
# ****
# *****
z = int(input("Enter the number of rows"))
for q in range(0, z):
    for k in range(0, q):
        print("*", end=" ")
    print("*")
