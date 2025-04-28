def zero_sum_subarrays(num):
    res = []
    n = len(num)
    for start in range(n):
        total = 0
        for end in range(start, n):
            total += num[end]
            if total == 0:
                res.append(num[start : end + 1])
    return res


nums = [3, 4, -7, 1, 2, -1, -3, 6]
print(zero_sum_subarrays(nums))
