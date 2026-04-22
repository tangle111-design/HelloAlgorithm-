"""完全背包问题。"""


def unbounded_knapsack_dp(wgt: list[int], val: list[int], cap: int) -> int:
    """完全背包：动态规划。"""
    n = len(wgt)
    dp = [[0] * (cap + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for c in range(1, cap + 1):
            if wgt[i - 1] > c:
                dp[i][c] = dp[i - 1][c]
            else:
                dp[i][c] = max(dp[i - 1][c], dp[i][c - wgt[i - 1]] + val[i - 1])
    return dp[n][cap]


def unbounded_knapsack_dp_comp(wgt: list[int], val: list[int], cap: int) -> int:
    """完全背包：空间优化。"""
    n = len(wgt)
    dp = [0] * (cap + 1)

    for i in range(1, n + 1):
        for c in range(1, cap + 1):
            if wgt[i - 1] <= c:
                dp[c] = max(dp[c], dp[c - wgt[i - 1]] + val[i - 1])
    return dp[cap]


def coin_change_dp(coins: list[int], amt: int) -> int:
    """零钱兑换：最少硬币数量。"""
    n = len(coins)
    max_val = amt + 1
    dp = [[0] * (amt + 1) for _ in range(n + 1)]

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
    """零钱兑换：空间优化。"""
    max_val = amt + 1
    dp = [max_val] * (amt + 1)
    dp[0] = 0

    for coin in coins:
        for a in range(coin, amt + 1):
            dp[a] = min(dp[a], dp[a - coin] + 1)
    return dp[amt] if dp[amt] != max_val else -1


def coin_change_ii_dp(coins: list[int], amt: int) -> int:
    """零钱兑换 II：组合数量。"""
    n = len(coins)
    dp = [[0] * (amt + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = 1

    for i in range(1, n + 1):
        for a in range(1, amt + 1):
            if coins[i - 1] > a:
                dp[i][a] = dp[i - 1][a]
            else:
                dp[i][a] = dp[i - 1][a] + dp[i][a - coins[i - 1]]
    return dp[n][amt]


def coin_change_ii_dp_comp(coins: list[int], amt: int) -> int:
    """零钱兑换 II：空间优化。"""
    dp = [0] * (amt + 1)
    dp[0] = 1

    for coin in coins:
        for a in range(coin, amt + 1):
            dp[a] += dp[a - coin]
    return dp[amt]


if __name__ == "__main__":
    w = [1, 3, 4]
    v = [15, 20, 30]
    cap = 4
    print(unbounded_knapsack_dp(w, v, cap))
    print(unbounded_knapsack_dp_comp(w, v, cap))
    print(coin_change_dp([1, 2, 5], 11))
    print(coin_change_dp_comp([1, 2, 5], 11))
    print(coin_change_ii_dp([1, 2, 5], 5))
    print(coin_change_ii_dp_comp([1, 2, 5], 5))
