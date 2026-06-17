"""二分查找（Binary Search）- 分治策略的经典应用。

问题描述：
在**有序数组**中查找目标值 target，
若存在则返回其索引，否则返回 -1。

分治思想：
每次将搜索区间缩小一半：
1. 计算中间位置
2. 比较中间值与目标值
3. 根据比较结果决定搜索左半区还是右半区

时间复杂度：O(log n) - 每次减半
空间复杂度：O(log n) - 递归版本（迭代版为 O(1)）
"""


def dfs(nums: list[int], target: int, i: int, j: int) -> int:
    """二分查找的递归实现。

    参数说明：
        nums: 有序数组
        target: 目标值
        i: 当前搜索区间的左边界（包含）
        j: 当前搜索区间的右边界（包含）

    返回：
        目标值的索引，若不存在则返回 -1

    递归结构：
    f(i, j) =
        若 i > j: 返回 -1（区间为空）
        若 nums[m] < target: 递归 f(m+1, j)
        若 nums[m] > target: 递归 f(i, m-1)
        否则: 返回 m（找到目标）
    """
    if i > j:
        return -1

    m = (i + j) // 2

    if nums[m] < target:
        return dfs(nums, target, m + 1, j)
    elif nums[m] > target:
        return dfs(nums, target, i, m - 1)
    else:
        return m


def binary_search(nums: list[int], target: int) -> int:
    """二分查找主函数。

    参数：
        nums: 有序数组（升序排列）
        target: 要查找的目标值

    返回：
        目标值的索引，或 -1（未找到）
    """
    n = len(nums)
    return dfs(nums, target, 0, n - 1)


if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4, 5], 3, 2),
        ([1, 3, 5, 7, 9], 7, 3),
        ([1, 2, 4, 6, 8], 5, -1),
    ]

    print("二分查找测试结果：")
    print("-" * 50)
    for nums, target, expected in test_cases:
        result = binary_search(nums, target)
        status = "✅" if result == expected else "❌"
        print(f"{status} 在 {nums} 中找 {target}: 索引={result}, 期望={expected}")