"""DP 问题特性示例：展示动态规划的核心要素。

动态规划的三大特性：
1. **最优子结构**：大问题的最优解包含子问题的最优解
2. **重叠子问题**：递归过程中会重复计算相同的子问题（需要记忆化或DP表）
3. **无后效性**：一旦某个状态确定，之后的过程只与当前状态有关

本文件包含两个经典变体问题来演示这些特性。
"""


def min_cost_climbing_stairs_dp(cost: list[int]) -> int:
    """最小代价爬楼梯（LeetCode 746 变体）。

    问题描述：
    - 给定一个整数数组 cost，其中 cost[i] 表示从第 i 阶台阶向上爬的代价
    - 一旦支付代价，可以爬 1 或 2 个台阶
    - 求到达楼顶的最小代价

    状态定义：
    - dp[i] 表示到达第 i 阶的最小累计代价
    - 可以从 i-1 或 i-2 过来，取较小者 + 当前代价

    状态转移：
    - dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
    """
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
    """带约束的爬楼梯问题（状态扩展示例）。

    问题描述：
    - 每次可以走 1 或 2 步
    - 但不能连续两轮都走 1 步
    - 求到达第 n 阶的方法数

    状态扩展技巧：
    - 普通DP：dp[i] 只记录方法数
    - 扩展DP：dp[i][j] 记录最后一步的状态
      - j=0: 最后一步走的是 1 步
      - j=1: 最后一步走的是 2 步

    这样可以避免连续两次走 1 步的情况
    """
    if n < 0:
        return 0
    if n == 0:
        return 1

    # dp[i][0]: 到达第i阶且最后一步是1步的方法数
    # dp[i][1]: 到达第i阶且最后一步是2步的方法数
    dp = [[0, 0] for _ in range(n + 1)]

    if n >= 1:
        dp[1][0] = 1  # 第1阶只能走1步到达
    if n >= 2:
        dp[2][1] = 1  # 第2阶只能走2步到达（因为不能连续两个1步）

    for i in range(3, n + 1):
        # 最后一步是1步 → 上一步必须是2步
        dp[i][0] = dp[i - 1][1]

        # 最后一步是2步 → 上一步可以是1步或2步
        if i - 2 >= 0:
            dp[i][1] = dp[i - 2][0] + dp[i - 2][1]

    return dp[n][0] + dp[n][1]


if __name__ == "__main__":
    # 测试最小代价爬楼梯
    cost = [0, 1, 10, 2, 7, 3]
    print(f"最小代价爬楼梯结果: {min_cost_climbing_stairs_dp(cost)}")

    # 测试带约束的爬楼梯
    print(f"不连续走1步的方法数 (n=6): {climbing_stairs_no_consecutive_one_step(6)}")