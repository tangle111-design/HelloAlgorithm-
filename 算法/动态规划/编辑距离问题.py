"""编辑距离问题。

给定字符串 s 和 t，返回将 s 转换为 t 所需的最少编辑步数。
允许三种操作：插入、删除、替换。
"""


def edit_distance_dp(s: str, t: str) -> int:
    """编辑距离：二维动态规划。"""
    n, m = len(s), len(t)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        dp[i][0] = i
    for j in range(1, m + 1):
        dp[0][j] = j

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
    """编辑距离：一维滚动数组优化。"""
    n, m = len(s), len(t)
    dp = [0] * (m + 1)

    for j in range(1, m + 1):
        dp[j] = j

    for i in range(1, n + 1):
        left_up = dp[0]
        dp[0] = i
        for j in range(1, m + 1):
            old_dp_j = dp[j]
            if s[i - 1] == t[j - 1]:
                dp[j] = left_up
            else:
                dp[j] = min(dp[j - 1], dp[j], left_up) + 1
            left_up = old_dp_j

    return dp[m]


if __name__ == "__main__":
    s1, t1 = "kitten", "sitting"
    print(edit_distance_dp(s1, t1))
    print(edit_distance_dp_comp(s1, t1))
