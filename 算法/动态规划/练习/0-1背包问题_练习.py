"""0-1 背包问题练习。"""


def knapsack_dfs(wgt: list[int], val: list[int], i: int, c: int) -> int:
    """0-1 背包：暴力搜索。"""
    # 物品选完或容量耗尽
    if i == 0 or c == 0:
        return 0
    # 当前物品装不下，只能不选
    if wgt[i - 1] > c:
        return knapsack_dfs(wgt, val, i - 1, c)

    # 枚举：不选 / 选
    no = knapsack_dfs(wgt, val, i - 1, c)
    yes = knapsack_dfs(wgt, val, i - 1, c - wgt[i - 1]) + val[i - 1]
    return max(no, yes)


def knapsack_dfs_mem(wgt: list[int], val: list[int], mem: list[list[int]], i: int, c: int) -> int:
    """0-1 背包：记忆化搜索。"""
    if i == 0 or c == 0:
        return 0
    if mem[i][c] != -1:
        return mem[i][c]

    if wgt[i - 1] > c:
        mem[i][c] = knapsack_dfs_mem(wgt, val, mem, i - 1, c)
        return mem[i][c]

    no = knapsack_dfs_mem(wgt, val, mem, i - 1, c)
    yes = knapsack_dfs_mem(wgt, val, mem, i - 1, c - wgt[i - 1]) + val[i - 1]
    mem[i][c] = max(no, yes)
    return mem[i][c]


def knapsack_dp(wgt: list[int], val: list[int], cap: int) -> int:
    """0-1 背包：动态规划。"""
    n = len(wgt)
    # 1) 定义 dp[i][c]：前 i 个物品在容量 c 下的最大价值
    dp = [[0] * (cap + 1) for _ in range(n + 1)]

    # 2) 状态转移
    for i in range(1, n + 1):
        for c in range(1, cap + 1):
            if wgt[i - 1] > c:
                dp[i][c] = dp[i - 1][c]
            else:
                dp[i][c] = max(dp[i - 1][c], dp[i - 1][c - wgt[i - 1]] + val[i - 1])
    return dp[n][cap]


def knapsack_dp_comp(wgt: list[int], val: list[int], cap: int) -> int:
    """0-1 背包：空间优化。"""
    n = len(wgt)
    dp = [0] * (cap + 1)

    # 关键：0-1 背包必须倒序遍历容量
    for i in range(1, n + 1):
        for c in range(cap, 0, -1):
            if wgt[i - 1] <= c:
                dp[c] = max(dp[c], dp[c - wgt[i - 1]] + val[i - 1])
    return dp[cap]
