"""完全背包问题练习。"""


def unbounded_knapsack_dp(wgt: list[int], val: list[int], cap: int) -> int:
    """完全背包：动态规划。"""
    n = len(wgt)
    # 1) 定义 dp[i][c]：前 i 个物品在容量 c 下的最大价值
    dp = [[0] * (cap + 1) for _ in range(n + 1)]

    # 2) 状态转移
    for i in range(1, n + 1):
        for c in range(1, cap + 1):
            if wgt[i - 1] > c:
                dp[i][c] = dp[i - 1][c]
            else:
                # 与 0-1 背包差异：选当前物品后仍可继续选当前物品，因此是 dp[i][...]
                dp[i][c] = max(dp[i - 1][c], dp[i][c - wgt[i - 1]] + val[i - 1])
    return dp[n][cap]


def unbounded_knapsack_dp_comp(wgt: list[int], val: list[int], cap: int) -> int:
    """完全背包：空间优化。"""
    n = len(wgt)
    dp = [0] * (cap + 1)

    # 关键：完全背包需要正序遍历容量
    for i in range(1, n + 1):
        for c in range(1, cap + 1):
            if wgt[i - 1] <= c:
                dp[c] = max(dp[c], dp[c - wgt[i - 1]] + val[i - 1])
    return dp[cap]


def coin_change_dp(coins: list[int], amt: int) -> int:
    """零钱兑换：最少硬币数。"""
    n = len(coins)
    max_val = amt + 1

    # dp[i][a]：前 i 种硬币凑出金额 a 的最少硬币数
    dp = [[0] * (amt + 1) for _ in range(n + 1)]

    # 首行（无硬币可用）除了金额 0 都不可达
    for a in range(1, amt + 1):
        dp[0][a] = max_val

    for i in range(1, n + 1):
        for a in range(1, amt + 1):
            if coins[i - 1] > a:
                dp[i][a] = dp[i - 1][a]
            else:
                dp[i][a] = min(dp[i - 1][a], dp[i][a - coins[i - 1]] + 1)

    return dp[n][amt] if dp[n][amt] != max_val else -1


def coin_change_ii_dp(coins: list[int], amt: int) -> int:
    """零钱兑换 II：组合数量。"""
    n = len(coins)
    # dp[i][a]：前 i 种硬币凑出金额 a 的组合数
    dp = [[0] * (amt + 1) for _ in range(n + 1)]

    # 凑出金额 0 的方式始终为 1（什么都不选）
    for i in range(n + 1):
        dp[i][0] = 1

    for i in range(1, n + 1):
        for a in range(1, amt + 1):
            if coins[i - 1] > a:
                dp[i][a] = dp[i - 1][a]
            else:
                dp[i][a] = dp[i - 1][a] + dp[i][a - coins[i - 1]]

    return dp[n][amt]
