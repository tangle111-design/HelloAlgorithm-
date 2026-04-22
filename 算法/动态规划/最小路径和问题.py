"""最小路径和问题。"""

from math import inf


def min_path_sum_dfs(grid: list[list[int]], i: int, j: int) -> int:
    """最小路径和：暴力搜索。"""
    if i == 0 and j == 0:
        return grid[0][0]
    if i < 0 or j < 0:
        return inf

    up = min_path_sum_dfs(grid, i - 1, j)
    left = min_path_sum_dfs(grid, i, j - 1)
    return min(up, left) + grid[i][j]


def min_path_sum_dfs_mem(grid: list[list[int]], mem: list[list[int]], i: int, j: int) -> int:
    """最小路径和：记忆化搜索。"""
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
    """最小路径和：动态规划。"""
    n, m = len(grid), len(grid[0])
    dp = [[0] * m for _ in range(n)]

    dp[0][0] = grid[0][0]
    for j in range(1, m):
        dp[0][j] = dp[0][j - 1] + grid[0][j]
    for i in range(1, n):
        dp[i][0] = dp[i - 1][0] + grid[i][0]

    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
    return dp[n - 1][m - 1]


def min_path_sum_dp_comp(grid: list[list[int]]) -> int:
    """最小路径和：空间优化。"""
    n, m = len(grid), len(grid[0])
    dp = [0] * m

    dp[0] = grid[0][0]
    for j in range(1, m):
        dp[j] = dp[j - 1] + grid[0][j]

    for i in range(1, n):
        dp[0] += grid[i][0]
        for j in range(1, m):
            dp[j] = min(dp[j], dp[j - 1]) + grid[i][j]
    return dp[m - 1]


if __name__ == "__main__":
    g = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    n1, m1 = len(g), len(g[0])
    mem = [[-1] * m1 for _ in range(n1)]
    print(min_path_sum_dfs(g, n1 - 1, m1 - 1))
    print(min_path_sum_dfs_mem(g, mem, n1 - 1, m1 - 1))
    print(min_path_sum_dp(g))
    print(min_path_sum_dp_comp(g))
