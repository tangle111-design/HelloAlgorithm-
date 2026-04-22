class QuickSortBasic:
    """快速排序基础版练习壳（哨兵分区）"""

    def partition(self, nums: list[int], left: int, right: int) -> int:
        """对区间 [left, right] 做一次分区，返回基准最终下标"""
        # 思路提示：
        # 1) 取 nums[left] 作为基准值 pivot
        # 2) 右指针 j 先走，找第一个 < pivot 的元素
        # 3) 左指针 i 再走，找第一个 > pivot 的元素
        # 4) 若 i < j，交换二者
        # 5) 当 i == j，把 pivot 放到分界点
        i, j = left, right

        while i < j:
            # TODO 1: j 从右向左扫描，停在第一个 < pivot 的位置
            while i < j and nums[j] >= nums[left]:
                j -= 1

            # TODO 2: i 从左向右扫描，停在第一个 > pivot 的位置
            while i < j and nums[i] <= nums[left]:
                i += 1

            # TODO 3: 交换错位元素
            nums[i], nums[j] = nums[j], nums[i]

        # TODO 4: 把基准值交换到最终位置 i
        nums[i], nums[left] = nums[left], nums[i]
        return i

    def quick_sort(self, nums: list[int], left: int, right: int):
        """快速排序练习壳（原地排序）"""
        # 递归边界：子区间长度为 0 或 1 时天然有序
        if left >= right:
            return

        # 第一步：分区，把数组切成“左小右大”两部分
        pivot = self.partition(nums, left, right)

        # 第二步：递归处理左半区
        self.quick_sort(nums, left, pivot - 1)

        # 第三步：递归处理右半区
        self.quick_sort(nums, pivot + 1, right)
