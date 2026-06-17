"""计数排序练习版 - 非比较型排序算法。

核心思想：
统计每个元素出现的次数，
然后根据统计结果将元素放回正确的位置。

特点：
- 线性时间复杂度 O(n+k)
- 只能用于整数（或可映射为整数）
- 需要知道数据的范围

两种版本：
1. 简单版：直接按计数输出（不稳定）
2. 完整版：使用前缀和确定位置（稳定）

时间复杂度：O(n + k)
空间复杂度：O(k)
稳定性：可以实现稳定排序
"""


def counting_sort_naive(nums: list[int]) -> None:
    """简单版计数排序（不稳定）。"""
    m = max(nums)

    counter = [0] * (m + 1)

    for num in nums:
        counter[num] += 1

    i = 0
    for num in range(m + 1):
        for _ in range(counter[num]):
            nums[i] = num
            i += 1


def counting_sort(nums: list[int]) -> None:
    """完整版计数排序（稳定排序）。

    关键技巧 - 前缀和：
    将"出现次数"转换为"尾索引"，
    然后倒序遍历以保持稳定性。
    """
    m = max(nums)

    counter = [0] * (m + 1)

    for num in nums:
        counter[num] += 1

    for i in range(m):
        counter[i + 1] += counter[i]

    n = len(nums)
    res = [0] * n

    for i in range(n - 1, -1, -1):
        num = nums[i]
        res[counter[num] - 1] = num
        counter[num] -= 1

    for i in range(n):
        nums[i] = res[i]


if __name__ == "__main__":
    test_cases = [
        [1, 0, 1, 2, 0, 3, 2, 1],
        [5, 4, 3, 2, 1],
    ]

    print("=" * 60)
    print("计数排序测试")
    print("=" * 60)

    for arr in test_cases:
        original = arr.copy()
        counting_sort(arr)
        print(f"✅ {original} → {arr}")

    print("\n💡 关键要点：")
    print("- 统计次数而非比较大小")
    print("- 只适合整数或可离散化的数据")
    print("- 完整版通过前缀和+倒序遍历保持稳定性")