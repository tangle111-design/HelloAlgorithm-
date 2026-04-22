def digit(num: int, exp: int) -> int:
    """取 num 在 exp 位上的数字（exp=1,10,100...）"""
    return (num // exp) % 10


def counting_sort_digit(nums: list[int], exp: int):
    """按某一位执行稳定计数排序"""
    n = len(nums)
    counter = [0] * 10

    # TODO 1: 统计当前位 0~9 的出现次数
    for i in range(n):
        d = digit(nums[i], exp)
        counter[d] += 1

    # TODO 2: 前缀和，得到每个数字对应的放置边界
    for i in range(1, 10):
        counter[i] += counter[i - 1]

    # TODO 3: 倒序写入结果数组，保持稳定性
    res = [0] * n
    for i in range(n - 1, -1, -1):
        d = digit(nums[i], exp)
        j = counter[d] - 1
        res[j] = nums[i]
        counter[d] -= 1

    # TODO 4: 覆盖回原数组
    for i in range(n):
        nums[i] = res[i]


def radix_sort(nums: list[int]):
    """基数排序练习版（LSD，从低位到高位）"""
    if not nums:
        return

    # TODO 1: 找到最大值，确定需要处理的位数
    m = max(nums)
    exp = 1

    # TODO 2: 从个位开始逐位进行稳定计数排序
    while exp <= m:
        counting_sort_digit(nums, exp)
        exp *= 10
