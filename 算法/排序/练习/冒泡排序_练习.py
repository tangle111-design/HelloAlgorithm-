def bubble_sort(nums: list[int]):
    """冒泡排序练习版（原地排序）"""
    n = len(nums)
    # 外层控制未排序区间的右边界 i
    for i in range(n - 1, 0, -1):
        # 内层把当前未排序区间 [0, i] 的最大值“冒泡”到 i
        for j in range(i):
            # TODO 1: 比较相邻元素
            if nums[j] > nums[j + 1]:
                # TODO 2: 交换相邻元素
                nums[j], nums[j + 1] = nums[j], nums[j + 1]


def bubble_sort_with_flag(nums: list[int]):
    """冒泡排序练习版（带提前结束标志）"""
    n = len(nums)
    for i in range(n - 1, 0, -1):
        flag = False
        for j in range(i):
            # TODO 1: 比较相邻元素
            if nums[j] > nums[j + 1]:
                # TODO 2: 交换相邻元素，并标记本轮发生了交换
                nums[j], nums[j + 1] = nums[j], nums[j + 1]
                # TODO 3: 将 flag 置为 True
        # TODO 4: 如果整轮没有发生交换，说明数组已有序，可直接结束
