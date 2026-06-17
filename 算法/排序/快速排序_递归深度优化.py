"""快速排序优化 - 尾递归优化控制递归深度。

问题背景：
快速排序的递归深度取决于树的高度，
在最坏情况下（如数组已有序），
递归深度可能达到 O(n)，导致栈溢出。

解决方案：尾递归优化
每次只对较短的子数组进行递归调用，
对较长的子数组通过循环处理。
这样可以保证最大递归深度不超过 O(log n)。

效果：
空间复杂度从最坏 O(n) 降低到 O(log n)
"""


def quick_sort_tail_recursive(nums: list[int], left: int, right: int) -> None:
    """快速排序（尾递归优化版本）。

    核心技巧：
    使用 while 循环替代一次递归调用，
    确保每次递归都处理较短的子数组。
    """
    while left < right:
        pivot = partition_basic(nums, left, right)

        if pivot - left < right - pivot:
            quick_sort_tail_recursive(nums, left, pivot - 1)
            left = pivot + 1
        else:
            quick_sort_tail_recursive(nums, pivot + 1, right)
            right = pivot - 1


def partition_basic(nums: list[int], left: int, right: int) -> int:
    """基础版哨兵划分。"""
    i, j = left, right

    while i < j:
        while i < j and nums[j] >= nums[left]:
            j -= 1
        while i < j and nums[i] <= nums[left]:
            i += 1
        nums[i], nums[j] = nums[j], nums[i]

    nums[i], nums[left] = nums[left], nums[i]
    return i


if __name__ == "__main__":
    test_cases = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
        [4, 1, 3, 1, 5, 2],
    ]

    print("递归深度优化测试")
    print("=" * 50)

    for arr in test_cases:
        original = arr.copy()
        quick_sort_tail_recursive(arr, 0, len(arr) - 1)
        print(f"✅ {original} → {arr}")