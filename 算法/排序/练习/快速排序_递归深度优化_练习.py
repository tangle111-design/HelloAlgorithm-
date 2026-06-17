"""快速排序优化练习版 - 尾递归优化控制递归深度。

问题背景：
快速排序的递归深度取决于树的高度，
在最坏情况下（如数组已有序），
递归深度可能达到 O(n)，导致栈溢出。

示例（n=10000 的已有序数组）：
- 普通快排：递归深度 ≈ 10000 ❌ 栈溢出
- 尾递归优化：递归深度 ≤ log₂(10000) ≈ 14 ✅ 安全

解决方案：尾递归优化
核心技巧：
每次只对**较短的子数组**进行递归调用，
对较长的子数组通过**循环**处理。

为什么有效？
因为短子数组的递归深度有限，
而长子数组通过循环不断缩短，
最终保证最大递归深度不超过 O(log n)。
"""


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


def quick_sort_tail_recursive(nums: list[int], left: int, right: int) -> None:
    """快速排序（尾递归优化版本）。

    算法步骤：
    1. 使用 while 循环替代一次递归
    2. 每次只对较短的子数组递归
    3. 较长的子数组通过更新边界继续循环

    效果：
    最大递归深度从 O(n) 降低到 O(log n)
    """
    while left < right:
        pivot = partition_basic(nums, left, right)

        # 判断哪个子数组更短
        if pivot - left < right - pivot:
            # 左边较短，递归处理左边
            quick_sort_tail_recursive(nums, left, pivot - 1)
            # 右边较长，通过循环处理（更新 left 边界）
            left = pivot + 1
        else:
            # 右边较短，递归处理右边
            quick_sort_tail_recursive(nums, pivot + 1, right)
            # 左边较长，通过循环处理（更新 right 边界）
            right = pivot - 1


if __name__ == "__main__":
    test_cases = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
        [4, 1, 3, 1, 5, 2],
    ]

    print("=" * 60)
    print("递归深度优化测试（尾递归优化）")
    print("=" * 60)

    for arr in test_cases:
        original = arr.copy()
        quick_sort_tail_recursive(arr, 0, len(arr) - 1)
        print(f"✅ {original} → {arr}")

    print("\n💡 关键要点：")
    print("- 使用 while 替代部分递归")
    print("- 总是优先递归较短的子数组")
    print("- 保证递归深度 ≤ O(log n)")
    print("- 有效防止栈溢出！")