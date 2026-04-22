def insertion_sort(nums: list[int]):
    """插入排序练习版（原地排序）"""
    # 已排序区间初始为 [0, 0]，从第 2 个元素开始向前插入
    for i in range(1, len(nums)):
        base = nums[i]
        j = i - 1

        # TODO 1: 在已排序区间 [0, i - 1] 中从右向左寻找插入位置
        while j >= 0 and nums[j] > base:
            # TODO 2: 把较大元素右移，给 base 腾位置
            nums[j + 1] = nums[j]
            j -= 1

        # TODO 3: 将 base 放入最终插入位置
        nums[j + 1] = base
