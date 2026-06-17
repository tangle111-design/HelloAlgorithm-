"""快速排序练习版 - 基于分治的高效排序算法。

核心思想：
1. 选择一个"基准数"（pivot）
2. 将数组分为两部分：小于基准的、大于基准的
3. 递归对两部分分别进行快排

时间复杂度：平均 O(n log n)，最坏 O(n²)
空间复杂度：O(log n)（递归栈）
稳定性：不稳定排序
"""


def partition(nums: list[int], left: int, right: int) -> int:
    """哨兵划分 - 将数组以基准数为界分为两部分。

    算法步骤：
    1. 以 nums[left] 作为基准数
    2. 使用双指针 i, j 从两端向中间扫描
    3. i 从左向右找第一个 > 基准的元素
    4. j 从右向左找第一个 < 基准的元素
    5. 交换这两个元素
    6. 当 i == j 时，将基准数交换到该位置

    返回：
        基准数的最终索引位置
    """
    # 步骤 1：初始化双指针
    # TODO: i = left, j = right
    i, j = left, right

    while i < j:
        # 步骤 2：j 从右向左找 < 基准的元素
        while i < j and nums[j] >= nums[left]:
            j -= 1

        # 步骤 3：i 从左向右找 > 基准的元素
        while i < j and nums[i] <= nums[left]:
            i += 1

        # 步骤 4：交换两个元素
        # TODO: nums[i], nums[j] = nums[j], nums[i]
        nums[i], nums[j] = nums[j], nums[i]

    # 步骤 5：将基准数放到最终位置
    # TODO: nums[i], nums[left] = nums[left], nums[i]
    nums[i], nums[left] = nums[left], nums[i]

    return i


def quick_sort(nums: list[int], left: int, right: int) -> None:
    """快速排序主函数。

    参数：
        nums: 待排序列表（原地修改）
        left: 当前区间的左边界
        right: 当前区间的右边界
    """
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

    print("=" * 60)
    print("快速排序测试")
    print("=" * 60)

    for arr in test_cases:
        original = arr.copy()
        quick_sort(arr, 0, len(arr) - 1)
        print(f"✅ {original} → {arr}")

    print("\n💡 关键要点：")
    print("- 分治策略：选基准→分区→递归")
    print("- 平均性能优秀 O(n log n)")
    print("- 最坏情况 O(n²)（可通过优化避免）")