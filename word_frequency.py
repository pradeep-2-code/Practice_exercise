# 1.	Word Frequency Counter
# 1.	Tasks Evaluated: String manipulation, dictionaries, loops, functions.
# Description:
# 2.	Write a program that takes a paragraph of text as input and counts the frequency of each word.
# 3.	Use a dictionary to store the word counts.
# 4.	Print the top 5 most frequent words along with their counts.
# 5.	Use string methods to clean the input (e.g., remove punctuation and convert to lowercase).

para = input("Enter your paragraph")
dic = {}
for i in para:
    num = para.count(i)
    print(f"{i}:{num}")
string = input("Enter your para")
dict2 = {}
for i in string:
    dict2[i] = para.count(i)
# print(dict2)
print(dict(sorted(dict2.items(), reverse=True)[0:5]))
