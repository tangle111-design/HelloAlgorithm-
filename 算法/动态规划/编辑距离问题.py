"""编辑距离问题（Levenshtein Distance）。

给定字符串 s 和 t，返回将 s 转换为 t 所需的最少编辑步数。
允许三种操作：
1. 插入一个字符
2. 删除一个字符
3. 替换一个字符

应用场景：拼写检查、DNA序列比对、文本相似度计算等。
"""


def edit_distance_dp(s: str, t: str) -> int:
    """编辑距离：二维动态规划。

    状态定义：
    - dp[i][j] 表示：s 的前 i 个字符转换为 t 的前 j 个字符所需的最少编辑步数

    边界条件：
    - dp[i][0] = i：s 的前 i 个字符需要删除 i 次变为空串
    - dp[0][j] = j：空串需要插入 j 次变为 t 的前 j 个字符

    状态转移：
    - 若 s[i-1] == t[j-1]：dp[i][j] = dp[i-1][j-1] （无需操作）
    - 否则：dp[i][j] = min(插入, 删除, 替换) + 1
      - 插入：dp[i][j-1] + 1  (在 s 中插入 t[j-1])
      - 删除：dp[i-1][j] + 1  (删除 s[i-1])
      - 替换：dp[i-1][j-1] + 1  (将 s[i-1] 替换为 t[j-1])
    """
    n, m = len(s), len(t)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # 初始化首列和首行
    for i in range(1, n + 1):
        dp[i][0] = i
    for j in range(1, m + 1):
        dp[0][j] = j

    # 填充 dp 表
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s[i - 1] == t[j - 1]:
                # 字符相同，无需额外操作
                dp[i][j] = dp[i - 1][j - 1]
            else:
                # 三种操作取最小值
                insert_cost = dp[i][j - 1] + 1
                delete_cost = dp[i - 1][j] + 1
                replace_cost = dp[i - 1][j - 1] + 1
                dp[i][j] = min(insert_cost, delete_cost, replace_cost)

    return dp[n][m]


def edit_distance_dp_comp(s: str, t: str) -> int:
    """编辑距离：空间优化版本（一维滚动数组）。

    优化技巧：
    - 用变量 left_up 保存左上角的值（dp[i-1][j-1]）
    - 每行开始时更新 left_up 和 dp[0]
    - 时间复杂度 O(n×m)，空间复杂度从 O(n×m) 降至 O(m)
    """
    n, m = len(s), len(t)
    dp = [0] * (m + 1)

    # 初始化首行（空串转为 t[:j] 需要 j 次插入）
    for j in range(1, m + 1):
        dp[j] = j

    for i in range(1, n + 1):
        # 保存上一行的 dp[0]（即 dp[i-1][0]）作为本轮的左上角起点
        left_up = dp[0]

        # 更新首列（s[:i] 转为空串需要 i 次删除）
        dp[0] = i

        for j in range(1, m + 1):
            # 暂存当前 dp[j]，下一轮会变成新的 left_up
            old_dp_j = dp[j]

            if s[i - 1] == t[j - 1]:
                # 字符相同，直接使用左上角的值
                dp[j] = left_up
            else:
                # 三种操作取最小值 + 1
                # dp[j-1]: 左侧（插入）
                # dp[j]: 上方（删除，尚未更新，仍是上一行的值）
                # left_up: 左上角（替换）
                dp[j] = min(dp[j - 1], dp[j], left_up) + 1

            # 更新 left_up 为下一轮的 dp[i-1][j-1]
            left_up = old_dp_j

    return dp[m]


if __name__ == "__main__":
    # 测试用例 1：经典例子 kitten -> sitting
    s1, t1 = "kitten", "sitting"
    print(f"编辑距离 ('{s1}' -> '{t1}'): {edit_distance_dp(s1, t1)}")
    print(f"空间优化版结果: {edit_distance_dp_comp(s1, t1)}")

    # 测试用例 2：完全相同的字符串
    print(f"\n相同字符串 'hello' -> 'hello': {edit_distance_dp('hello', 'hello')}")

    # 测试用例 3：一个为空串
    print(f"空串 '' -> 'abc': {edit_distance_dp('', 'abc')}")