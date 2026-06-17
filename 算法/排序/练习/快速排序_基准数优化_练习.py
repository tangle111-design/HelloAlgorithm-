"""快速排序优化练习版 - 三数取中法选择基准数。

问题背景：
当数组已经有序或接近有序时，
如果总是选择第一个元素作为基准，
会导致分区极度不平衡（一边为空），
最坏情况下时间复杂度退化为 O(n²)。

示例（已升序数组 [1,2,3,4,5]）：
- 选第一个元素 1 作为基准
- 左边为空，右边是 [2,3,4,5]
- 递归深度达到 n，性能极差！

解决方案：三数取中法
从左端、中间、右端三个元素中选取**中位数**作为基准，
可以有效避免最坏情况。
"""


def median_three(nums: list[int], left: int, mid: int, right: int) -> int:
    """选取三个候选元素的中位数索引。

    参数：
        nums: 数组
        left: 左端索引
        mid: 中间索引
        right: 右端索引

    返回：
        中位数的索引
    """
    l, m, r = nums[left], nums[mid], nums[right]

    # 判断 m 是否在 l 和 r 之间
    if (l <= m <= r) or (r <= m <= l):
        return mid

    # 判断 l 是否在 m 和 r 之间
    if (m <= l <= r) or (r <= l <= m):
        return left

    # 否则 r 是中位数
    return right


def partition_optimized(nums: list[int], left: int, right: int) -> int:
    """哨兵划分（使用三数取中法优化）。

    算法步骤：
    1. 调用 median_three 获取基准的最佳位置
    2. 将基准交换到最左端
    3. 执行标准的哨兵划分操作
    """
    med = median_three(nums, left, (left + right) // 2, right)

    # 步骤 1：将中位数交换到左端作为基准
    # TODO: nums[left], nums[med] = nums[med], nums[left]
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

    print("=" * 60)
    print("基准数优化测试（三数取中法）")
    print("=" * 60)

    for arr in test_cases:
        original = arr.copy()
        pivot_idx = partition_optimized(arr, 0, len(arr) - 1)
        print(f"✅ {original}")
        print(f"   基准位置={pivot_idx}, 基准值={arr[pivot_idx]}")

    print("\n💡 关键要点：")
    print("- 避免已有序数组的最坏情况")
    print("- 选择更合理的基准数")
    print("- 显著提升实际性能")