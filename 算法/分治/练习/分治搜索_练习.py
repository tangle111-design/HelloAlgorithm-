def dfs(nums: list[int], target: int, i: int, j: int) -> int:
    """二分查找：求解子问题 f(i, j)"""
    # 步骤 1：先处理区间为空的情况（递归终止条件）。
    # 步骤 2：计算中点索引 m。
    # 步骤 3：比较 nums[m] 和 target 的大小：
    #   - 若 nums[m] < target，递归右半区间。
    #   - 若 nums[m] > target，递归左半区间。
    #   - 若相等，返回 m。
    """在此处完成代码"""


def binary_search(nums: list[int], target: int) -> int:
    """二分查找"""
    # 步骤 1：获取数组长度 n。
    # 步骤 2：调用 dfs 求解区间 [0, n-1]。
    """在此处完成代码"""
