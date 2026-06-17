"""0-1 背包问题练习版：根据笔记完成代码填空。"""


def knapsack_dfs(wgt: list[int], val: list[int], i: int, c: int) -> int:
    """0-1 背包：暴力搜索（递归实现）。

    思路提示：
    - 每个物品只有两种选择：放入背包或不放入
    - 递归终止条件：物品选完或容量耗尽
    """
    # 步骤 1：递归终止条件
    # TODO: 当 i==0 或 c==0 时返回 0
    if i == 0 or c == 0:
        return 0

    # 步骤 2：当前物品超重处理
    # TODO: 若第 i 个物品重量超过剩余容量 c，只能不选，递归处理前 i-1 个物品
    if wgt[i - 1] > c:
        return knapsack_dfs(wgt, val, i - 1, c)

    # 步骤 3：枚举两种选择
    # TODO 1: 不选当前物品 i，递归求最大价值（状态：i-1 个物品，容量仍为 c）
    no = knapsack_dfs(wgt, val, i - 1, c)

    # TODO 2: 选当前物品 i，递归求最大价值（状态：i-1 个物品，容量减去 wgt[i-1]，价值加上 val[i-1]）
    yes = knapsack_dfs(wgt, val, i - 1, c - wgt[i - 1]) + val[i - 1]

    # 步骤 4：返回两种选择中的较大值
    # TODO: 使用 max() 函数比较 no 和 yes
    return max(no, yes)


def knapsack_dfs_mem(wgt: list[int], val: list[int], mem: list[list[int]], i: int, c: int) -> int:
    """0-1 背包：记忆化搜索（在暴力搜索基础上增加缓存）。

    优化思路：
    - 用 mem[i][c] 缓存子问题结果，避免重复计算
    - 时间复杂度从 O(2^n) 降至 O(n×cap)
    """
    # 步骤 1：递归终止条件
    # TODO: 当 i==0 或 c==0 时返回 0
    if i == 0 or c == 0:
        return 0

    # 步骤 2：查表（缓存命中直接返回）
    # TODO: 若 mem[i][c] != -1，说明已计算过，直接返回缓存值
    if mem[i][c] != -1:
        return mem[i][c]

    # 步骤 3：当前物品超重处理
    # TODO: 与暴力搜索相同逻辑，但需将结果存入 mem[i][c]
    if wgt[i - 1] > c:
        mem[i][c] = knapsack_dfs_mem(wgt, val, mem, i - 1, c)
        return mem[i][c]

    # 步骤 4：枚举两种选择并记录到缓存
    # TODO 1: 不选当前物品
    no = knapsack_dfs_mem(wgt, val, mem, i - 1, c)

    # TODO 2: 选当前物品
    yes = knapsack_dfs_mem(wgt, val, mem, i - 1, c - wgt[i - 1]) + val[i - 1]

    # TODO 3: 将较大值存入 mem[i][c] 并返回
    mem[i][c] = max(no, yes)
    return mem[i][c]


def knapsack_dp(wgt: list[int], val: list[int], cap: int) -> int:
    """0-1 背包：动态规划（自底向上填充 dp 表）。

    状态定义：
    - dp[i][c] 表示：前 i 个物品，在容量为 c 的条件下能获得的最大价值

    状态转移方程：
    - dp[i][c] = max(dp[i-1][c], dp[i-1][c-wgt[i-1]] + val[i-1])
    """
    # 步骤 1：初始化变量
    # TODO: 获取物品数量 n
    n = len(wgt)

    # 步骤 2：创建 dp 表（二维数组）
    # TODO: dp 大小为 (n+1) × (cap+1)，初始值全为 0
    # 提示：dp[0][*] 和 dp[*][0] 都应该是 0（边界条件）
    dp = [[0] * (cap + 1) for _ in range(n + 1)]

    # 步骤 3：遍历所有状态
    # 外层循环：遍历每个物品（从第 1 个到第 n 个）
    for i in range(1, n + 1):
        # 内层循环：遍历每种容量（从 1 到 cap）
        for c in range(1, cap + 1):

            # 步骤 4：判断当前物品能否装入
            # TODO: 若第 i 个物品重量 > 当前容量 c，则无法选择该物品
            if wgt[i - 1] > c:
                # TODO: 只能继承不选的情况：dp[i][c] = dp[i-1][c]
                dp[i][c] = dp[i - 1][c]
            else:
                # TODO: 可以选择，取两种情况的最大值：
                #   1) 不选：dp[i-1][c]
                #   2) 选：dp[i-1][c-wgt[i-1]] + val[i-1]
                dp[i][c] = max(dp[i - 1][c], dp[i - 1][c - wgt[i - 1]] + val[i - 1])

    # 步骤 5：返回最终答案
    # TODO: 返回 dp[n][cap]，即前 n 个物品在容量 cap 下的最大价值
    return dp[n][cap]


def knapsack_dp_comp(wgt: list[int], val: list[int], cap: int) -> int:
    """0-1 背包：空间优化（一维滚动数组）。

    优化原理：
    - 观察发现 dp[i][c] 只依赖上一行 dp[i-1][*]
    - 可以用一维数组 dp[c] 替代二维数组
    - 关键点：必须倒序遍历容量，否则会重复选取同一物品！
    """
    # 步骤 1：初始化变量
    # TODO: 获取物品数量 n
    n = len(wgt)

    # 步骤 2：创建一维 dp 数组
    # TODO: dp 长度为 cap+1，初始值全为 0
    dp = [0] * (cap + 1)

    # 步骤 3：遍历每个物品
    for i in range(1, n + 1):

        # 步骤 4：【关键】倒序遍历容量
        # 原因：倒序可以保证 dp[c-wgt[i-1]] 使用的是上一层（i-1）的值
        # 如果正序遍历，dp[c-wgt[i-1]] 可能已经被更新为本层（i）的值，导致同一物品被多次选取
        # TODO: 从 cap 到 1 倒序遍历（注意：range(cap, 0, -1) 表示倒序）
        for c in range(cap, 0, -1):

            # 步骤 5：判断是否可以选择当前物品
            # TODO: 只有当物品重量 <= 当前容量时才考虑选择
            if wgt[i - 1] <= c:

                # 步骤 6：更新 dp[c]
                # TODO: 取不选和选两种情况的最大值
                #   - 不选：dp[c]（保持原值）
                #   - 选：dp[c-wgt[i-1]] + val[i-1]
                dp[c] = max(dp[c], dp[c - wgt[i - 1]] + val[i - 1])

    # 步骤 7：返回最终答案
    # TODO: 返回 dp[cap]
    return dp[cap]