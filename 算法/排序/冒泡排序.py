"""冒泡排序（Bubble Sort）- 简单直观的排序算法。

核心思想：
通过连续比较和交换相邻元素，
每一轮将最大的元素"冒泡"到数组末尾。
就像水中的气泡一样，大的气泡会浮到水面。

时间复杂度：O(n²)
空间复杂度：O(1)
稳定性：稳定排序
"""


def bubble_sort(nums: list[int]) -> None:
    """基础版冒泡排序。

    算法步骤：
    1. 外循环控制未排序区间的右边界
    2. 内循环在 [0, i] 区间内两两比较
    3. 若前一个元素大于后一个，则交换
    4. 每轮结束后最大元素到达位置 i

    参数：
        nums: 待排序的列表（原地修改）
    """
    n = len(nums)

    for i in range(n - 1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]


def bubble_sort_with_flag(nums: list[int]) -> None:
    """优化版冒泡排序（带提前终止标志）。

    优化思路：
    如果某轮遍历中没有发生任何交换，
    说明数组已经有序，可以提前结束。

    最佳情况（已有序）：O(n) - 只需一轮遍历
    """
    n = len(nums)

    for i in range(n - 1, 0, -1):
        flag = False

        for j in range(i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                flag = True

        if not flag:
            break


if __name__ == "__main__":
    test_cases = [
        [4, 1, 3, 1, 5, 2],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
    ]

    print("冒泡排序测试")
    print("=" * 50)

    for arr in test_cases:
        original = arr.copy()
        bubble_sort_with_flag(arr)
        print(f"✅ {original} → {arr}")