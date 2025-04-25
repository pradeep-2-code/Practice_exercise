def most_frequent_element(nums):
    freq = {}

    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    max_freq = max(freq.values())
    for num, count in freq.items():
        if count == max_freq:
            return num
