class QuickSortMedianOfThree:
    """三数取中优化版快速排序练习壳"""

    def median_three(self, nums: list[int], left: int, mid: int, right: int) -> int:
        """返回 left/mid/right 三者中值对应的下标"""
        # 练习目标：理解“中位数作基准”如何降低近乎有序数组的退化概率
        l, m, r = nums[left], nums[mid], nums[right]

        # TODO 1: 判断 m 是否为中位数
        if (l <= m <= r) or (r <= m <= l):
            return mid

        # TODO 2: 判断 l 是否为中位数
        if (m <= l <= r) or (r <= l <= m):
            return left

        # TODO 3: 否则 r 为中位数
        return right

    def partition(self, nums: list[int], left: int, right: int) -> int:
        """哨兵分区 + 三数取中"""
        # 步骤提示：
        # 1) 先在 left/mid/right 里找中位数下标 med
        # 2) 把 nums[med] 交换到 left，作为基准
        # 3) 再执行标准双指针分区
        med = self.median_three(nums, left, (left + right) // 2, right)
        nums[left], nums[med] = nums[med], nums[left]

        i, j = left, right
        while i < j:
            while i < j and nums[j] >= nums[left]:
                j -= 1
            while i < j and nums[i] <= nums[left]:
                i += 1
            nums[i], nums[j] = nums[j], nums[i]

        nums[i], nums[left] = nums[left], nums[i]
        return i
