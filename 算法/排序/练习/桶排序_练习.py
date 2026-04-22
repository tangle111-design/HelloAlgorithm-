def bucket_sort(nums: list[float]):
    """桶排序练习版（假设输入在 [0, 1)）"""
    if len(nums) <= 1:
        return

    # TODO 1: 决定桶数量（此处示例取 n//2）
    k = len(nums) // 2
    k = max(k, 1)
    buckets: list[list[float]] = [[] for _ in range(k)]

    # TODO 2: 把元素映射到桶索引并放入对应桶
    for num in nums:
        idx = int(num * k)
        idx = min(idx, k - 1)
        buckets[idx].append(num)

    # TODO 3: 对每个桶单独排序（可换成你实现的任意排序）
    for bucket in buckets:
        bucket.sort()

    # TODO 4: 按桶顺序回写到原数组
    i = 0
    for bucket in buckets:
        for num in bucket:
            nums[i] = num
            i += 1
