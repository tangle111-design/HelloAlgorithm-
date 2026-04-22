"""DP 问题特性练习。"""


def min_cost_climbing_stairs_dp(cost: list[int]) -> int:
    """最小代价爬楼梯。"""
    # cost[0] 视作地面，目标是到达最后一个台阶 n
    n = len(cost) - 1
    if n <= 0:
        return 0
    if n == 1 or n == 2:
        return cost[n]

    # 1) 定义 dp[i]：到达第 i 阶的最小代价
    dp = [0] * (n + 1)
    # 2) 初始化
    dp[1], dp[2] = cost[1], cost[2]
    # 3) 状态转移
    for i in range(3, n + 1):
        dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]
    return dp[n]


def climbing_stairs_no_consecutive_one_step(n: int) -> int:
    """每步可走 1 或 2，但不能连续两轮走 1，求方案数。"""
    if n < 0:
        return 0
    if n == 0:
        return 1

    # dp[i][1]: 到达 i 且上一跳走了 1 阶的方案数
    # dp[i][2]: 到达 i 且上一跳走了 2 阶的方案数
    dp = [[0, 0, 0] for _ in range(n + 1)]

    # 基础状态
    if n >= 1:
        dp[1][1] = 1
    if n >= 2:
        dp[2][2] = 1

    for i in range(2, n + 1):
        # 上一跳为 1，则本轮一定是从 i-1 且上一跳为 2 走来
        dp[i][1] = dp[i - 1][2]
        # 上一跳为 2，则本轮从 i-2 走来，上一跳可为 1 或 2
        if i - 2 >= 0:
            dp[i][2] = dp[i - 2][1] + dp[i - 2][2]

    return dp[n][1] + dp[n][2]
