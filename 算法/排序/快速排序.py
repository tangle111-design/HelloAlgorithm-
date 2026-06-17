"""快速排序（Quick Sort）- 基于分治的高效排序算法。

核心思想：
1. 选择一个"基准数"（pivot）
2. 将数组分为两部分：小于基准的、大于基准的
3. 递归对两部分分别进行快排

时间复杂度：平均 O(n log n)，最坏 O(n²)
空间复杂度：O(log n)（递归栈）
稳定性：不稳定排序
"""


def partition(nums: list[int], left: int, right: int) -> int:
    """哨兵划分 - 将数组分为两部分。"""
    i, j = left, right

    while i < j:
        while i < j and nums[j] >= nums[left]:
            j -= 1
        while i < j and nums[i] <= nums[left]:
            i += 1
        nums[i], nums[j] = nums[j], nums[i]

    nums[i], nums[left] = nums[left], nums[i]
    return i


def quick_sort(nums: list[int], left: int, right: int) -> None:
    """快速排序主函数。"""
    if left >= right:
        return

    pivot = partition(nums, left, right)
    quick_sort(nums, left, pivot - 1)
    quick_sort(nums, pivot + 1, right)


if __name__ == "__main__":
    test_cases = [
        [4, 1, 3, 1, 5, 2],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
    ]

    print("快速排序测试")
    print("=" * 50)

    for arr in test_cases:
        original = arr.copy()
        quick_sort(arr, 0, len(arr) - 1)
        print(f"✅ {original} → {arr}")