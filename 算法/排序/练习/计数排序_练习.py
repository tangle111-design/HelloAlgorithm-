def counting_sort_naive(nums: list[int]):
    """计数排序简化版练习壳（仅适用于非负整数）"""
    if not nums:
        return

    # TODO 1: 找到最大值，开辟计数数组
    m = max(nums)
    counter = [0] * (m + 1)

    # TODO 2: 统计每个数字出现次数
    for num in nums:
        counter[num] += 1

    # TODO 3: 按计数结果回填原数组
    i = 0
    for num in range(m + 1):
        for _ in range(counter[num]):
            nums[i] = num
            i += 1


def counting_sort(nums: list[int]):
    """计数排序完整练习壳（稳定版）"""
    if not nums:
        return

    m = max(nums)
    counter = [0] * (m + 1)

    # TODO 1: 统计频次
    for num in nums:
        counter[num] += 1

    # TODO 2: 前缀和，把“频次”转为“末尾下标 + 1”
    for i in range(m):
        counter[i + 1] += counter[i]

    # TODO 3: 倒序遍历原数组，写入结果数组（保证稳定性）
    n = len(nums)
    res = [0] * n
    for i in range(n - 1, -1, -1):
        num = nums[i]
        res[counter[num] - 1] = num
        counter[num] -= 1

    # TODO 4: 覆盖回原数组
    for i in range(n):
        nums[i] = res[i]
