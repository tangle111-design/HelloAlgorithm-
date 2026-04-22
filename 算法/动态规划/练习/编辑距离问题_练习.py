"""编辑距离问题练习。"""


def edit_distance_dp(s: str, t: str) -> int:
    """编辑距离：动态规划。"""
    n, m = len(s), len(t)
    # 1) 定义 dp[i][j]：s 前 i 个字符转换为 t 前 j 个字符的最少操作数
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # 2) 初始化边界
    for i in range(1, n + 1):
        dp[i][0] = i
    for j in range(1, m + 1):
        dp[0][j] = j

    # 3) 状态转移
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                insert_cost = dp[i][j - 1] + 1
                delete_cost = dp[i - 1][j] + 1
                replace_cost = dp[i - 1][j - 1] + 1
                dp[i][j] = min(insert_cost, delete_cost, replace_cost)

    return dp[n][m]


def edit_distance_dp_comp(s: str, t: str) -> int:
    """编辑距离：空间优化。"""
    n, m = len(s), len(t)
    dp = [0] * (m + 1)

    # 初始化首行（空串转为 t[:j]）
    for j in range(1, m + 1):
        dp[j] = j

    for i in range(1, n + 1):
        # leftup 对应旧的 dp[i-1][j-1]
        leftup = dp[0]
        dp[0] = i
        for j in range(1, m + 1):
            old_dp_j = dp[j]
            if s[i - 1] == t[j - 1]:
                dp[j] = leftup
            else:
                dp[j] = min(dp[j - 1], dp[j], leftup) + 1
            leftup = old_dp_j

    return dp[m]
