class QuickSortDepthOptimized:
    """递归深度优化版快速排序练习壳"""

    def partition(self, nums: list[int], left: int, right: int) -> int:
        """你可以复用基础版 partition，也可自行实现其他分区方案"""
        i, j = left, right
        while i < j:
            while i < j and nums[j] >= nums[left]:
                j -= 1
            while i < j and nums[i] <= nums[left]:
                i += 1
            nums[i], nums[j] = nums[j], nums[i]
        nums[i], nums[left] = nums[left], nums[i]
        return i

    def quick_sort(self, nums: list[int], left: int, right: int):
        """只递归较短子区间，较长子区间改为循环迭代"""
        # 理解重点：
        # - 普通快排最坏递归深度可到 O(n)
        # - 每轮只递归较短那边，可把最大递归深度压到 O(log n)
        while left < right:
            pivot = self.partition(nums, left, right)

            left_len = pivot - left
            right_len = right - pivot

            # TODO 1: 递归较短区间
            # TODO 2: 通过改写 left/right 继续循环处理较长区间
            if left_len < right_len:
                self.quick_sort(nums, left, pivot - 1)
                left = pivot + 1
            else:
                self.quick_sort(nums, pivot + 1, right)
                right = pivot - 1
