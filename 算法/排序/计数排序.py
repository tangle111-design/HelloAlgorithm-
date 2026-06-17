"""计数排序（Counting Sort）- 非比较型排序算法。

核心思想：
统计每个元素出现的次数，
然后根据统计结果将元素放回正确的位置。

特点：
- 线性时间复杂度 O(n+k)
- 只能用于整数排序（或可映射为整数）
- 需要知道数据的范围

时间复杂度：O(n + k)（k 为数据范围）
空间复杂度：O(k)
稳定性：可以实现稳定排序
"""


def counting_sort_naive(nums: list[int]) -> None:
    """简单版计数排序（无法保持稳定性）。"""
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

    关键技巧：
    使用前缀和来确定每个元素的最终位置，
    并倒序遍历以保持相同元素的相对顺序。
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

    print("计数排序测试")
    print("=" * 50)

    for arr in test_cases:
        original = arr.copy()
        counting_sort(arr)
        print(f"✅ {original} → {arr}")