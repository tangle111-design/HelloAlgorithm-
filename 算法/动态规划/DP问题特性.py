"""DP 问题特性示例。"""


def min_cost_climbing_stairs_dp(cost: list[int]) -> int:
    """最小代价爬楼梯。"""
    n = len(cost) - 1
    if n <= 0:
        return 0
    if n == 1 or n == 2:
        return cost[n]

    dp = [0] * (n + 1)
    dp[1], dp[2] = cost[1], cost[2]
    for i in range(3, n + 1):
        dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]
    return dp[n]


def climbing_stairs_no_consecutive_one_step(n: int) -> int:
    """每步可走 1 或 2，但不能连续两轮走 1，求方案数。"""
    if n < 0:
        return 0
    if n == 0:
        return 1

    dp = [[0, 0, 0] for _ in range(n + 1)]

    if n >= 1:
        dp[1][1] = 1
    if n >= 2:
        dp[2][2] = 1

    for i in range(2, n + 1):
        dp[i][1] = dp[i - 1][2]
        if i - 2 >= 0:
            dp[i][2] = dp[i - 2][1] + dp[i - 2][2]

    return dp[n][1] + dp[n][2]


if __name__ == "__main__":
    cost = [0, 1, 10, 2, 7, 3]
    print(min_cost_climbing_stairs_dp(cost))
    print(climbing_stairs_no_consecutive_one_step(6))
