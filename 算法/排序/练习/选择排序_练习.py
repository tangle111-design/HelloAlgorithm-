def selection_sort(nums: list[int]):
    """选择排序练习版（原地排序）"""
    n = len(nums)
    # 每轮在未排序区间 [i, n - 1] 里找最小值
    for i in range(n - 1):
        k = i

        # TODO 1: 找到未排序区间中的最小元素下标 k
        for j in range(i + 1, n):
            if nums[j] < nums[k]:
                k = j

        # TODO 2: 把最小值交换到区间起点 i
        nums[i], nums[k] = nums[k], nums[i]
