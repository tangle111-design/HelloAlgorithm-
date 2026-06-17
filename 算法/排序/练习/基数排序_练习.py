"""基数排序练习版 - 按位数逐位排序的非比较算法。

核心思想：
按照从低位到高位的顺序，
对每一位使用计数排序进行排序。

为什么有效？
因为对于任意两位数 a 和 b：
如果十位数不同，无论个位数如何，最终顺序由十位数决定；
如果十位数相同，则由个位数决定。
所以从低位开始逐位排序，最终会得到正确结果！

特点：
- 时间复杂度 O(d×(n+k))，d 是最大数的位数
- 只能用于整数（或可按位比较的数据）
- 稳定排序

时间复杂度：O(d × (n + k))
空间复杂度：O(n + k)
稳定性：稳定排序
"""


def digit(num: int, exp: int) -> int:
    """获取数字的第 k 位（exp = 10^(k-1)）。

    示例：
    digit(12345, 100) → 3 （百位）
    digit(12345, 10) → 4 （十位）
    digit(12345, 1) → 5 （个位）
    """
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
    """基数排序主函数。

    算法步骤：
    1. 找出数组中的最大值，确定最大位数
    2. 从低位到高位，对每一位执行计数排序
    3. exp 从 1 开始，每次乘以 10（个位→十位→百位...）
    """
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

    print("=" * 60)
    print("基数排序测试")
    print("=" * 60)

    for arr in test_cases:
        original = arr.copy()
        radix_sort(arr)
        print(f"✅ {original} → {arr}")

    print("\n💡 关键要点：")
    print("- 从低位到高位逐位排序")
    print("- 每一位都使用稳定的计数排序")
    print("- 适合整数或固定长度的字符串")