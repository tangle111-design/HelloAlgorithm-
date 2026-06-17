"""最小路径和问题（LeetCode 64）。

给定一个 m×n 的网格，每个格子包含非负整数。
从左上角出发，每次只能向右或向下移动，求到达右下角的最小路径和。

示例：
输入: grid = [[1,3,1],[1,5,1],[4,2,1]]
输出: 7
解释: 路径 1→3→1→1→1 的和最小
"""

from math import inf


def min_path_sum_dfs(grid: list[list[int]], i: int, j: int) -> int:
    """最小路径和：暴力搜索（指数级时间复杂度）。"""
    if i == 0 and j == 0:
        return grid[0][0]
    if i < 0 or j < 0:
        return inf

    up = min_path_sum_dfs(grid, i - 1, j)
    left = min_path_sum_dfs(grid, i, j - 1)
    return min(up, left) + grid[i][j]


def min_path_sum_dfs_mem(grid: list[list[int]], mem: list[list[int]], i: int, j: int) -> int:
    """最小路径和：记忆化搜索（避免重复计算）。"""
    if i == 0 and j == 0:
        return grid[0][0]
    if i < 0 or j < 0:
        return inf
    if mem[i][j] != -1:
        return mem[i][j]

    up = min_path_sum_dfs_mem(grid, mem, i - 1, j)
    left = min_path_sum_dfs_mem(grid, mem, i, j - 1)
    mem[i][j] = min(up, left) + grid[i][j]
    return mem[i][j]


def min_path_sum_dp(grid: list[list[int]]) -> int:
    """最小路径和：动态规划（二维 dp 表）。

    状态定义：
    - dp[i][j] 表示到达位置 (i, j) 的最小路径和

    状态转移：
    - dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
      只能从上方或左方过来，取较小值加上当前格子值
    """
    n, m = len(grid), len(grid[0])
    dp = [[0] * m for _ in range(n)]

    # 初始化起点
    dp[0][0] = grid[0][0]

    # 初始化首行（只能从左边来）
    for j in range(1, m):
        dp[0][j] = dp[0][j - 1] + grid[0][j]

    # 初始化首列（只能从上边来）
    for i in range(1, n):
        dp[i][0] = dp[i - 1][0] + grid[i][0]

    # 填充其余位置
    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

    return dp[n - 1][m - 1]


def min_path_sum_dp_comp(grid: list[list[int]]) -> int:
    """最小路径和：空间优化（一维数组）。

    优化技巧：
    - dp[j] 保存当前行第 j 列的最小路径和
    - 每行开始时更新 dp[0]
    - 从左到右遍历，dp[j-1] 是左边，dp[j] 是上边（上一轮的值）
    """
    n, m = len(grid), len(grid[0])
    dp = [0] * m

    # 初始化第一行
    dp[0] = grid[0][0]
    for j in range(1, m):
        dp[j] = dp[j - 1] + grid[0][j]

    # 处理后续行
    for i in range(1, n):
        # 更新首列
        dp[0] += grid[i][0]

        # 更新其余列
        for j in range(1, m):
            dp[j] = min(dp[j], dp[j - 1]) + grid[i][j]

    return dp[m - 1]


if __name__ == "__main__":
    g = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    n1, m1 = len(g), len(g[0])
    mem = [[-1] * m1 for _ in range(n1)]

    print(f"暴力搜索结果: {min_path_sum_dfs(g, n1 - 1, m1 - 1)}")
    print(f"记忆化搜索结果: {min_path_sum_dfs_mem(g, mem, n1 - 1, m1 - 1)}")
    print(f"动态规划结果: {min_path_sum_dp(g)}")
    print(f"空间优化结果: {min_path_sum_dp_comp(g)}")