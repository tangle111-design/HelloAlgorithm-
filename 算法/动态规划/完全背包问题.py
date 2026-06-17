"""完全背包问题：每个物品可以重复选取，求最大价值。
相关变体：零钱兑换（最少硬币数）、零钱兑换II（组合数）。"""


def unbounded_knapsack_dp(wgt: list[int], val: list[int], cap: int) -> int:
    """完全背包：动态规划（二维 dp 表）。

    与0-1背包的区别：
    - 状态转移中选当前物品时使用 dp[i][...] 而非 dp[i-1][...]
    - 表示可以选择多次同一物品
    """
    n = len(wgt)
    dp = [[0] * (cap + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for c in range(1, cap + 1):
            if wgt[i - 1] > c:
                dp[i][c] = dp[i - 1][c]
            else:
                # 关键差异：dp[i][c-wgt[i-1]] 允许重复选取
                dp[i][c] = max(dp[i - 1][c], dp[i][c - wgt[i - 1]] + val[i - 1])
    return dp[n][cap]


def unbounded_knapsack_dp_comp(wgt: list[int], val: list[int], cap: int) -> int:
    """完全背包：空间优化（一维数组，正序遍历）。

    注意：与0-1背包相反，这里必须正序遍历！
    原因：正序允许同一物品被多次选取
    """
    n = len(wgt)
    dp = [0] * (cap + 1)

    for i in range(1, n + 1):
        # 正序遍历容量
        for c in range(1, cap + 1):
            if wgt[i - 1] <= c:
                dp[c] = max(dp[c], dp[c - wgt[i - 1]] + val[i - 1])
    return dp[cap]


def coin_change_dp(coins: list[int], amt: int) -> int:
    """零钱兑换 I：最少硬币数量（完全背包的特例）。

    特点：
    - 目标是"恰好凑出"目标金额
    - 求最小值而非最大值
    """
    n = len(coins)
    max_val = amt + 1
    dp = [[0] * (amt + 1) for _ in range(n + 1)]

    # 初始化：无硬币时，除了金额0都不可达
    for a in range(1, amt + 1):
        dp[0][a] = max_val

    for i in range(1, n + 1):
        for a in range(1, amt + 1):
            if coins[i - 1] > a:
                dp[i][a] = dp[i - 1][a]
            else:
                dp[i][a] = min(dp[i - 1][a], dp[i][a - coins[i - 1]] + 1)
    return dp[n][amt] if dp[n][amt] != max_val else -1


def coin_change_dp_comp(coins: list[int], amt: int) -> int:
    """零钱兑换 I：空间优化版本。"""
    max_val = amt + 1
    dp = [max_val] * (amt + 1)
    dp[0] = 0

    for coin in coins:
        for a in range(coin, amt + 1):
            dp[a] = min(dp[a], dp[a - coin] + 1)
    return dp[amt] if dp[amt] != max_val else -1


def coin_change_ii_dp(coins: list[int], amt: int) -> int:
    """零钱兑换 II：计算组合数量。

    问法变化：不是求最小值，而是求方案总数
    """
    n = len(coins)
    dp = [[0] * (amt + 1) for _ in range(n + 1)]

    # 凑出金额0的方式只有一种：什么都不选
    for i in range(n + 1):
        dp[i][0] = 1

    for i in range(1, n + 1):
        for a in range(1, amt + 1):
            if coins[i - 1] > a:
                dp[i][a] = dp[i - 1][a]
            else:
                # 组合数：不选的方案数 + 选的方案数
                dp[i][a] = dp[i - 1][a] + dp[i][a - coins[i - 1]]
    return dp[n][amt]


def coin_change_ii_dp_comp(coins: list[int], amt: int) -> int:
    """零钱兑换 II：空间优化版本。"""
    dp = [0] * (amt + 1)
    dp[0] = 1

    for coin in coins:
        for a in range(coin, amt + 1):
            dp[a] += dp[a - coin]
    return dp[amt]


if __name__ == "__main__":
    # 测试完全背包
    w = [1, 3, 4]
    v = [15, 20, 30]
    cap = 4
    print(f"完全背包 DP 结果: {unbounded_knapsack_dp(w, v, cap)}")
    print(f"完全背包优化结果: {unbounded_knapsack_dp_comp(w, v, cap)}")

    # 测试零钱兑换 I
    print(f"\n零钱兑换 I (coins=[1,2,5], amt=11): {coin_change_dp([1, 2, 5], 11)}")
    print(f"零钱兑换 I 优化版: {coin_change_dp_comp([1, 2, 5], 11)}")

    # 测试零钱兑换 II
    print(f"\n零钱兑换 II (coins=[1,2,5], amt=5): {coin_change_ii_dp([1, 2, 5], 5)}")
    print(f"零钱兑换 II 优化版: {coin_change_ii_dp_comp([1, 2, 5], 5)}")