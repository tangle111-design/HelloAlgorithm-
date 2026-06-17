"""二分查找练习版：分治策略在搜索中的应用。


问题描述：
在有序数组中查找目标值 target，
若存在返回其索引，否则返回 -1。

核心思想 - 分治：
每次将搜索区间缩小一半：
1. 取中间位置
2. 与目标比较
3. 决定搜索左半还是右半

时间复杂度：O(log n)
空间复杂度：O(log n)（递归版本）
"""


def binary_search(nums: list[int], target: int) -> int:
    """二分查找实现。

    参数：
        nums: 有序数组（升序）
        target: 目标值

    返回：
        目标索引或 -1
    """
    # 步骤 1：定义递归函数
    def dfs(left: int, right: int) -> int:
        """在 [left, right] 区间内搜索。"""
        # 步骤 2：终止条件 - 区间为空
        # TODO: 若 left > right，返回 -1
        if left > right:
            return -1

        # 步骤 3：计算中间位置
        # TODO: mid = (left + right) // 2
        mid = (left + right) // 2

        # 步骤 4：比较并决定搜索方向
        # TODO 1: 若 nums[mid] < target，搜索右半区（return dfs(mid+1, right)）
        # TODO 2: 若 nums[mid] > target，搜索左半区（return dfs(left, mid-1)）
        # TODO 3: 否则找到目标，返回 mid
        if nums[mid] < target:
            return dfs(mid + 1, right)
        elif nums[mid] > target:
            return dfs(left, mid - 1)
        else:
            return mid

    # 步骤 5：启动搜索
    # TODO: 返回 dfs(0, len(nums)-1)
    return dfs(0, len(nums) - 1)


if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4, 5], 3, 2),
        ([1, 3, 5, 7, 9], 7, 3),
        ([1, 2, 4, 6, 8], 5, -1),
    ]

    print("=" * 60)
    print("二分查找测试")
    print("=" * 60)

    for nums, target, expected in test_cases:
        result = binary_search(nums, target)
        status = "✅" if result == expected else "❌"
        print(f"{status} 数组={nums}, 目标={target}: 索引={result}")

    print("\n💡 关键要点：")
    print("- 必须是有序数组！")
    print("- 每次排除一半元素")
    print("- 时间复杂度 O(log n)，比线性查找快很多")