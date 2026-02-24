def find_kth_largest(nums, k):
    n = len(nums)

    if k > n or k <= 0:
        raise ValueError("k має бути в межах розміру масиву")

    indexed_nums = []

    for i in range(n):
        indexed_nums.append((nums[i], i))

    indexed_nums.sort(reverse=True)

    value, index = indexed_nums[k - 1]

    return value, index