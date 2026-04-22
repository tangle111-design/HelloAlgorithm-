"""0-1 背包问题。"""


def knapsack_dfs(wgt: list[int], val: list[int], i: int, c: int) -> int:
    """0-1 背包：暴力搜索。"""
    if i == 0 or c == 0:
        return 0
    if wgt[i - 1] > c:
        return knapsack_dfs(wgt, val, i - 1, c)

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
    dp = [[0] * (cap + 1) for _ in range(n + 1)]

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

    for i in range(1, n + 1):
        for c in range(cap, 0, -1):
            if wgt[i - 1] <= c:
                dp[c] = max(dp[c], dp[c - wgt[i - 1]] + val[i - 1])
    return dp[cap]


if __name__ == "__main__":
    w = [2, 3, 4]
    v = [3, 4, 5]
    cap = 6
    mem = [[-1] * (cap + 1) for _ in range(len(w) + 1)]
    print(knapsack_dfs(w, v, len(w), cap))
    print(knapsack_dfs_mem(w, v, mem, len(w), cap))
    print(knapsack_dp(w, v, cap))
    print(knapsack_dp_comp(w, v, cap))
