"""基数排序（Radix Sort）- 按位数逐位排序的非比较算法。

核心思想：
按照从低位到高位的顺序，
对每一位使用计数排序进行排序。

特点：
- 线性时间复杂度 O(d×(n+k))
- 只能用于整数（或可按位比较的数据）
- d 是最大数的位数，k 是基数（10进制为10）

时间复杂度：O(d × (n + k))
空间复杂度：O(n + k)
稳定性：稳定排序
"""


def digit(num: int, exp: int) -> int:
    """获取元素 num 的第 k 位数字（exp = 10^(k-1)）。"""
    return (num // exp) % 10


def counting_sort_digit(nums: list[int], exp: int) -> None:
    """根据第 k 位进行计数排序。"""
    counter = [0] * 10
    n = len(nums)

    for i in range(n):
        d = digit(nums[i], exp)
        counter[d] += 1

    for i in range(1, 10):
        counter[i] += counter[i - 1]

    res = [0] * n
    for i in range(n - 1, -1, -1):
        d = digit(nums[i], exp)
        j = counter[d] - 1
        res[j] = nums[i]
        counter[d] -= 1

    for i in range(n):
        nums[i] = res[i]


def radix_sort(nums: list[int]) -> None:
    """基数排序主函数。"""
    m = max(nums)
    exp = 1

    while exp <= m:
        counting_sort_digit(nums, exp)
        exp *= 10


if __name__ == "__main__":
    test_cases = [
        [105, 405, 203, 104, 305, 206, 207],
        [100, 50, 200, 150, 300],
    ]

    print("基数排序测试")
    print("=" * 50)

    for arr in test_cases:
        original = arr.copy()
        radix_sort(arr)
        print(f"✅ {original} → {arr}")