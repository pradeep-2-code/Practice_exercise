# Given a sentence, use a list comprehension to extract all words that are longer than 5 letters.
# Input:
# sentence = "Python is a powerful and versatile programming language"
# Expected Output:
# ['Python', 'powerful', 'versatile', 'programming', 'language']
sentence = "Python is a powerful and versatile programming language"
print([x for x in sentence.split() if len(x) > 5])
