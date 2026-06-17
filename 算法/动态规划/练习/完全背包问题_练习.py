"""完全背包问题练习版：每个物品可无限次选取，求最大价值及变体问题。"""


def unbounded_knapsack_dp(wgt: list[int], val: list[int], cap: int) -> int:
    """完全背包：动态规划（二维 dp 表）。

    核心区别（与0-1背包对比）：
    - 0-1背包：dp[i][c] = max(dp[i-1][c], dp[i-1][c-wgt] + val)  ← 选时用 i-1
    - 完全背包：dp[i][c] = max(dp[i-1][c], dp[i][c-wgt] + val)    ← 选时用 i（可重复选）
    """
    # 步骤 1：初始化变量
    # TODO: 获取物品数量 n
    n = len(wgt)

    # 步骤 2：创建二维 dp 表
    # TODO: dp[i][c] 表示前 i 个物品在容量 c 下的最大价值
    # 提示：大小为 (n+1) × (cap+1)，初始值全为 0
    dp = [[0] * (cap + 1) for _ in range(n + 1)]

    # 步骤 3：双重循环遍历所有状态
    # 外层：遍历每个物品（从第 1 个到第 n 个）
    for i in range(1, n + 1):
        # 内层：遍历每种容量（从 1 到 cap）
        for c in range(1, cap + 1):

            # 步骤 4：判断当前物品能否装入
            # TODO: 若第 i 个物品重量 > 当前容量 c
            if wgt[i - 1] > c:

                # TODO: 无法选择，只能继承上一行的结果
                dp[i][c] = dp[i - 1][c]
            else:
                # TODO: 【关键】可以选择时，取两种情况的最大值：
                #   1) 不选物品 i：dp[i-1][c] （继承）
                #   2) 选物品 i：dp[i][c-wgt[i-1]] + val[i-1] （注意这里是 dp[i]，不是 dp[i-1]！）
                # 原因：用 dp[i] 表示可以继续选择当前物品（完全背包的核心特征）
                dp[i][c] = max(dp[i - 1][c], dp[i][c - wgt[i - 1]] + val[i - 1])

    # 步骤 5：返回最终结果
    # TODO: 返回 dp[n][cap]
    return dp[n][cap]


def unbounded_knapsack_dp_comp(wgt: list[int], val: list[int], cap: int) -> int:
    """完全背包：空间优化（一维数组）。

    【重要】与0-1背包的空间优化对比：
    - 0-1背包：倒序遍历容量（range(cap, 0, -1)），防止重复选取
    - 完全背包：正序遍历容量（range(1, cap+1)），允许重复选取！

    为什么正序可以？
    因为正序更新时，dp[c-wgt] 已经是本轮（考虑了当前物品）的结果，
    相当于在当前物品的基础上再选一次当前物品，实现了"无限次选取"
    """
    # 步骤 1：初始化变量
    # TODO: 获取物品数量 n
    n = len(wgt)

    # 步骤 2：创建一维 dp 数组
    # TODO: 长度为 cap+1，初始值全为 0
    dp = [0] * (cap + 1)

    # 步骤 3：遍历每个物品
    for i in range(1, n + 1):

        # 步骤 4：【关键区别】正序遍历容量！
        # TODO: 从 1 到 cap 正序遍历（注意：range(1, cap + 1) 表示正序）
        # 对比0-1背包用的是 range(cap, 0, -1) 倒序
        for c in range(1, cap + 1):

            # 步骤 5：判断是否可以选择
            # TODO: 只有当物品重量 <= 当前容量时才考虑
            if wgt[i - 1] <= c:

                # 步骤 6：更新 dp[c]
                # TODO: 取不选和选的最大值：
                #   - 不选：dp[c]（保持原值）
                #   - 选：dp[c-wgt[i-1]] + val[i-1]（这里的 dp[c-wgt] 可能已被本轮更新过）
                dp[c] = max(dp[c], dp[c - wgt[i - 1]] + val[i - 1])

    # 步骤 7：返回结果
    # TODO: 返回 dp[cap]
    return dp[cap]


def coin_change_dp(coins: list[int], amt: int) -> int:
    """零钱兑换 I：最少硬币数量（完全背包的最小化版本）。

    问题特点：
    - 每种硬币可以无限使用
    - 求"恰好凑出"目标金额的最少硬币数
    - 如果无法凑出，返回 -1

    与标准完全背包的差异：
    - 目标从最大化价值 → 最小化硬币数量
    - 从"不超过容量" → "恰好等于金额"
    - 使用 min() 而非 max()
    """
    # 步骤 1：初始化变量
    # TODO: 获取硬币种类数 n
    n = len(coins)

    # 步骤 2：定义一个表示"不可达"的大数值
    # TODO: 使用 amt + 1 作为无效解标记（避免溢出）
    max_val = amt + 1

    # 步骤 3：创建 dp 表
    # TODO: dp[i][a] 表示前 i 种硬币凑出金额 a 的最少硬币数
    dp = [[0] * (amt + 1) for _ in range(n + 1)]

    # 步骤 4：初始化首行（边界条件）
    # TODO: 当没有硬币可用时（i=0），除了金额0外都不可达
    # 提示：将 dp[0][1...amt] 设为 max_val（表示需要无限多枚硬币，即不可达）
    for a in range(1, amt + 1):
        dp[0][a] = max_val

    # 步骤 5：状态转移
    for i in range(1, n + 1):  # 遍历每种硬币
        for a in range(1, amt + 1):  # 遍历每种金额

            # 步骤 6：判断当前硬币面额是否超过目标金额
            # TODO: 若硬币面额 > 当前金额 a
            if coins[i - 1] > a:

                # TODO: 无法使用该硬币，只能继承前 i-1 种硬币的结果
                dp[i][a] = dp[i - 1][a]
            else:
                # TODO: 可以使用，取两种情况的最小值：
                #   1) 不用第 i 种硬币：dp[i-1][a]
                #   2) 用第 i 种硬币：dp[i][a-coins[i-1]] + 1（注意是 dp[i]，可重复使用）
                dp[i][a] = min(dp[i - 1][a], dp[i][a - coins[i - 1]] + 1)

    # 步骤 7：返回结果
    # TODO: 判断是否可达：
    #   - 若 dp[n][amt] == max_val，说明无法凑出，返回 -1
    #   - 否则返回 dp[n][amt]
    return dp[n][amt] if dp[n][amt] != max_val else -1


def coin_change_ii_dp(coins: list[int], amt: int) -> int:
    """零钱兑换 II：计算组合数量。

    问题变化：
    - 不再求最少硬币数，而是问有多少种不同的组合方式
    - 组合不考虑顺序（{1,2} 和 {2,1} 视为同一种）

    状态转移变化：
    - 用加法代替 min/max：dp[i][a] = dp[i-1][a] + dp[i][a-coins[i-1]]
    """
    # 步骤 1：初始化变量
    # TODO: 获取硬币种类数 n
    n = len(coins)

    # 步骤 2：创建 dp 表
    # TODO: dp[i][a] 表示前 i 种硬币凑出金额 a 的组合数
    dp = [[0] * (amt + 1) for _ in range(n + 1)]

    # 步骤 3：初始化首列（关键边界条件）
    # TODO: 凑出金额 0 的方式只有一种：什么硬币都不选
    # 提示：对于所有 i，dp[i][0] = 1
    for i in range(n + 1):
        dp[i][0] = 1

    # 步骤 4：状态转移
    for i in range(1, n + 1):
        for a in range(1, amt + 1):

            # 步骤 5：判断是否可以使用当前硬币
            # TODO: 若硬币面额 > 金额 a
            if coins[i - 1] > a:

                # TODO: 只能继承不使用该硬币的组合数
                dp[i][a] = dp[i - 1][a]
            else:
                # TODO: 组合数 = 不用的组合数 + 用的组合数
                #   - 不用：dp[i-1][a]
                #   - 用：dp[i][a-coins[i-1]]（可重复使用当前硬币）
                dp[i][a] = dp[i - 1][a] + dp[i][a - coins[i - 1]]

    # 步骤 6：返回结果
    # TODO: 返回 dp[n][amt]
    return dp[n][amt]