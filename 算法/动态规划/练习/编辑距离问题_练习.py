"""编辑距离问题练习版：求两个字符串之间的最少编辑步数。


问题描述：
给定两个字符串 s 和 t，返回将 s 转换为 t 所需的最少编辑步数。
你可以对一个字符串进行三种操作：
1. 插入一个字符
2. 删除一个字符
3. 替换一个字符


示例：
输入: s = "kitten", t = "sitting"
输出: 3
解释:
kitten -> sitten (替换 k 为 s)
sitten -> sittin (替换 e 为 i)
sittin -> sitting (插入 g)
"""


def edit_distance_dp(s: str, t: str) -> int:
    """编辑距离：二维动态规划实现。

    核心思路：
    - 定义 dp[i][j] 表示 s 的前 i 个字符转换为 t 的前 j 个字符的最少步数
    - 通过比较 s[i-1] 和 t[j-1] 决定是否需要操作
    """
    # 步骤 1：获取字符串长度
    # TODO: 分别获取 s 和 t 的长度，赋值给 n 和 m
    n, m = len(s), len(t)

    # 步骤 2：创建二维 dp 表
    # TODO: 创建大小为 (n+1) × (m+1) 的二维数组，初始值全为 0
    # 提示：dp[i][j] 表示 s[:i] 转换为 t[:j] 的最少操作数
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # 步骤 3：初始化边界条件（首列）
    # TODO: 首列 dp[i][0] 表示 s[:i] 转换为空串，需要 i 次删除操作
    # 提示：遍历 i 从 1 到 n，设置 dp[i][0] = i
    for i in range(1, n + 1):
        dp[i][0] = i

    # 步骤 4：初始化边界条件（首行）
    # TODO: 首行 dp[0][j] 表示空串转换为 t[:j]，需要 j 次插入操作
    # 提示：遍历 j 从 1 到 m，设置 dp[0][j] = j
    for j in range(1, m + 1):
        dp[0][j] = j

    # 步骤 5：填充 dp 表（状态转移）
    # 外层循环：遍历 s 的每个字符位置（从第 1 个到第 n 个）
    for i in range(1, n + 1):

        # 内层循环：遍历 t 的每个字符位置（从第 1 个到第 m 个）
        for j in range(1, m + 1):

            # 步骤 6：判断当前字符是否相等
            # TODO: 比较 s 的第 i-1 个字符和 t 的第 j-1 个字符
            if s[i - 1] == t[j - 1]:

                # TODO: 字符相同，无需任何操作！
                # 直接继承左上角的结果：dp[i][j] = dp[i-1][j-1]
                dp[i][j] = dp[i - 1][j - 1]
            else:

                # 步骤 7：字符不同，考虑三种操作，取最小值
                # 操作 1：在 s 中插入 t[j-1]
                # 对应状态：dp[i][j-1] + 1（左侧的值 + 1次插入）
                insert_cost = dp[i][j - 1] + 1

                # 操作 2：删除 s 中的 s[i-1]
                # 对应状态：dp[i-1][j] + 1（上方的值 + 1次删除）
                delete_cost = dp[i - 1][j] + 1

                # 操作 3：将 s[i-1] 替换为 t[j-1]
                # 对应状态：dp[i-1][j-1] + 1（左上角的值 + 1次替换）
                replace_cost = dp[i - 1][j - 1] + 1

                # TODO: 取三种操作中的最小值作为 dp[i][j]
                dp[i][j] = min(insert_cost, delete_cost, replace_cost)

    # 步骤 8：返回最终结果
    # TODO: 返回 dp[n][m]，即整个 s 转换为整个 t 的最少操作数
    return dp[n][m]


def edit_distance_dp_comp(s: str, t: str) -> int:
    """编辑距离：空间优化版本（使用一维数组）。

    优化原理：
    - 二维 dp 表中，dp[i][j] 只依赖三个值：
      * 左边：dp[i][j-1]
      * 上边：dp[i-1][j]
      * 左上：dp[i-1][j-1]
    - 可以用一维数组 + 一个临时变量保存左上角的值
    - 空间复杂度从 O(n×m) 降低到 O(m)

    关键技巧：
    - 用 left_up 变量暂存 dp[i-1][j-1]
    - 每次更新前保存旧的 dp[j]，用于下一轮的 left_up
    """
    # 步骤 1：获取字符串长度
    # TODO: 获取 s 和 t 的长度
    n, m = len(s), len(t)

    # 步骤 2：创建一维 dp 数组
    # TODO: 创建长度为 m+1 的一维数组，初始值全为 0
    # 这个数组对应 dp 表的一行
    dp = [0] * (m + 1)

    # 步骤 3：初始化首行（相当于 dp[0][j]）
    # TODO: 空串转换为 t[:j] 需要 j 次插入
    # 提示：遍历 j 从 1 到 m，设置 dp[j] = j
    for j in range(1, m + 1):
        dp[j] = j

    # 步骤 4：遍历 s 的每个字符（外层循环）
    for i in range(1, n + 1):

        # 步骤 5：保存左上角的初始值
        # TODO: 在处理每行之前，先保存当前的 dp[0] 作为 left_up
        # 这里的 dp[0] 实际上是上一行的 dp[i-1][0]
        left_up = dp[0]

        # 步骤 6：更新首列的值
        # TODO: s[:i] 转换为空串需要 i 次删除
        # 设置 dp[0] = i
        dp[0] = i

        # 步骤 7：遍历 t 的每个字符（内层循环）
        for j in range(1, m + 1):

            # 步骤 8：暂存当前 dp[j] 的旧值
            # TODO: 在更新之前，先保存当前的 dp[j]
            # 这个值在下一轮会变成新的 left_up（即 dp[i-1][j-1]）
            old_dp_j = dp[j]

            # 步骤 9：判断字符是否相同
            # TODO: 比较 s[i-1] 和 t[j-1]
            if s[i - 1] == t[j - 1]:

                # TODO: 字符相同，直接使用左上角的值
                dp[j] = left_up
            else:

                # 步骤 10：字符不同，取三种操作的最小值 + 1
                # 注意这里的含义：
                #   - dp[j-1]: 左边的值（已更新为本轮，对应插入操作）
                #   - dp[j]: 上边的值（未更新，仍是上一轮，对应删除操作）
                #   - left_up: 左上角的值（对应替换操作）
                # TODO: 使用 min() 函数取三者最小值再加 1
                dp[j] = min(dp[j - 1], dp[j], left_up) + 1

            # 步骤 11：更新 left_up 为下一轮做准备
            # TODO: 将刚才保存的旧值赋给 left_up
            # 这样在下一次循环时，left_up 就是正确的 dp[i-1][j-1]
            left_up = old_dp_j

    # 步骤 12：返回最终结果
    # TODO: 返回 dp[m]，即完整的编辑距离
    return dp[m]