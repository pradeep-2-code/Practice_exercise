# Filter Dictionary Based on Values (Using Loop)
# Question:
# Filter out students who scored below 80 from a dictionary.
# Input:
grades6 = {"Alice": 85, "Bob": 92, "Charlie": 78, "David": 65}
# Expected Output:
# {"Alice": 85, "Bob": 92}
{k: v for (k, v) in grades6.items() if v > 80}
