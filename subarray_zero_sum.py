def zero_sum_subarrays(nums):
    result = []
    n = len(nums)

    for start in range(n):
        total = 0

        for end in range(start, n):
            total += nums[end]

            if total == 0:
                result.append(nums[start : end + 1])
    return result


nums = [3, 4, -7, 1, 2, -1, -3, 6]
output = zero_sum_subarrays(nums)
print(output)
