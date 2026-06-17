"""快速排序优化 - 三数取中法选择基准数。

问题背景：
当数组已经有序或接近有序时，
如果总是选择第一个元素作为基准，
会导致分区极度不平衡（一边为空），
最坏情况下时间复杂度退化为 O(n²)。

解决方案：三数取中法
从左端、中间、右端三个元素中
选取中间值作为基准数，
可以有效避免最坏情况。
"""


def median_three(nums: list[int], left: int, mid: int, right: int) -> int:
    """选取三个候选元素的中位数索引。"""
    l, m, r = nums[left], nums[mid], nums[right]

    if (l <= m <= r) or (r <= m <= l):
        return mid
    if (m <= l <= r) or (r <= l <= m):
        return left
    return right


def partition_optimized(nums: list[int], left: int, right: int) -> int:
    """哨兵划分（使用三数取中法）。"""
    med = median_three(nums, left, (left + right) // 2, right)
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


if __name__ == "__main__":
    test_cases = [
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [4, 1, 3, 1, 5, 2],
    ]

    print("基准数优化测试")
    print("=" * 50)

    for arr in test_cases:
        original = arr.copy()
        pivot_idx = partition_optimized(arr, 0, len(arr) - 1)
        print(f"✅ {original} → 基准位置={pivot_idx}, 基准值={arr[pivot_idx]}")