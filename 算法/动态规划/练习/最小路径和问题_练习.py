"""最小路径和问题练习版：在网格中找从左上到右下的最短路径。


问题描述：
给定一个 m×n 的网格 grid，其中 grid[i][j] 表示该位置的代价。
机器人从左上角 (0,0) 出发，每次只能向右或向下移动一步。
求到达右下角 (m-1,n-1) 的最小路径和。


示例：
grid = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7 (路径: 1→3→1→1→1)
"""


from math import inf


def min_path_sum_dfs(grid: list[list[int]], i: int, j: int) -> int:
    """最小路径和：暴力搜索（递归实现）。

    思路：
    - 从终点 (i,j) 反向递归到起点 (0,0)
    - 每次可以选择向上走或向左走
    - 到达边界时返回特定值（起点返回 grid[0][0]，越界返回无穷大）
    """
    # 步骤 1：递归终止条件 - 已到达起点
    # TODO: 当 i==0 且 j==0 时，返回 grid[0][0]（起点的代价）
    if i == 0 and j == 0:
        return grid[0][0]

    # 步骤 2：越界处理 - 超出网格范围
    # TODO: 当 i<0 或 j<0 时，返回 inf（表示此路不通）
    if i < 0 or j < 0:
        return inf

    # 步骤 3：递归计算两个方向的路径和
    # TODO 1: 向上走到 (i-1, j)，递归求最小路径和
    up = min_path_sum_dfs(grid, i - 1, j)

    # TODO 2: 向左走到 (i, j-1)，递归求最小路径和
    left = min_path_sum_dfs(grid, i, j - 1)

    # 步骤 4：取较小值并加上当前位置的代价
    # TODO: 使用 min() 函数取 up 和 left 的最小值，再加上 grid[i][j]
    return min(up, left) + grid[i][j]


def min_path_sum_dfs_mem(grid: list[list[int]], mem: list[list[int]], i: int, j: int) -> int:
    """最小路径和：记忆化搜索（增加缓存避免重复计算）。

    优化点：
    - 用 mem[i][j] 缓存已经计算过的结果
    - 时间复杂度从 O(2^(m+n)) 降至 O(m×n)
    """
    # 步骤 1：递归终止条件 - 已到达起点
    # TODO: 当 i==0 且 j==0 时返回 grid[0][0]
    if i == 0 and j == 0:
        return grid[0][0]

    # 步骤 2：越界处理
    # TODO: 当 i<0 或 j<0 时返回 inf
    if i < 0 or j < 0:
        return inf

    # 步骤 3：查表（缓存命中）
    # TODO: 若 mem[i][j] != -1，说明已计算过，直接返回缓存值
    if mem[i][j] != -1:
        return mem[i][j]

    # 步骤 4：递归计算（与暴力搜索相同逻辑）
    # TODO 1: 计算向上走的路径和
    up = min_path_sum_dfs_mem(grid, mem, i - 1, j)

    # TODO 2: 计算向左走的路径和
    left = min_path_sum_dfs_mem(grid, mem, i, j - 1)

    # 步骤 5：记录结果到缓存并返回
    # TODO: 将 min(up, left) + grid[i][j] 存入 mem[i][j]，然后返回
    mem[i][j] = min(up, left) + grid[i][j]
    return mem[i][j]


def min_path_sum_dp(grid: list[list[int]]) -> int:
    """最小路径和：动态规划（自底向上填充二维表）。

    核心思路：
    - 定义 dp[i][j] 为到达位置 (i,j) 的最小路径和
    - 由于只能向右或向下走，所以 (i,j) 只能从 (i-1,j) 或 (i,j-1) 到达
    - 状态转移：dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

    边界处理：
    - 首行 (i=0): 只能从左边来，dp[0][j] = dp[0][j-1] + grid[0][j]
    - 首列 (j=0): 只能从上边来，dp[i][0] = dp[i-1][0] + grid[i][0]
    """
    # 步骤 1：获取网格尺寸
    # TODO: 获取行数 n 和列数 m
    n, m = len(grid), len(grid[0])

    # 步骤 2：创建 dp 表
    # TODO: 创建大小为 n × m 的二维数组，初始值全为 0
    dp = [[0] * m for _ in range(n)]

    # 步骤 3：初始化起点
    # TODO: 设置 dp[0][0] = grid[0][0]
    dp[0][0] = grid[0][0]

    # 步骤 4：初始化首行（第 0 行的所有列）
    # TODO: 遍历 j 从 1 到 m-1，设置 dp[0][j] = dp[0][j-1] + grid[0][j]
    # 提示：首行的每个位置只能从左边到达
    for j in range(1, m):
        dp[0][j] = dp[0][j - 1] + grid[0][j]

    # 步骤 5：初始化首列（第 0 列的所有行）
    # TODO: 遍历 i 从 1 到 n-1，设置 dp[i][0] = dp[i-1][0] + grid[i][0]
    # 提示：首列的每个位置只能从上边到达
    for i in range(1, n):
        dp[i][0] = dp[i - 1][0] + grid[i][0]

    # 步骤 6：填充 dp 表的剩余部分
    # 外层循环：遍历每一行（从第 1 行到第 n-1 行）
    for i in range(1, n):

        # 内层循环：遍历每一列（从第 1 列到第 m-1 列）
        for j in range(1, m):

            # 步骤 7：状态转移
            # TODO: 取上方 (i-1,j) 和左方 (i,j-1) 的最小值，加上当前位置 grid[i][j]
            #   - 上方的值：dp[i-1][j]
            #   - 左方的值：dp[i][j-1]
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

    # 步骤 8：返回最终结果
    # TODO: 返回右下角的值 dp[n-1][m-1]
    return dp[n - 1][m - 1]


def min_path_sum_dp_comp(grid: list[list[int]]) -> int:
    """最小路径和：空间优化（使用一维滚动数组）。

    优化原理：
    - 观察发现 dp[i][j] 只依赖：
      * 左边的值 dp[i][j-1] （同一行，已更新）
      * 上边的值 dp[i-1][j] （上一行，尚未更新）
    - 可以用一维数组 dp[j] 来替代二维数组
    - 空间复杂度从 O(m×n) 降至 O(m)

    关键技巧：
    - 从左到右遍历时，dp[j] 保存的是当前行的值
    - dp[j-1] 已经更新为本轮（左边），dp[j] 还是上一轮（上边）
    - 每行开始时需要单独更新 dp[0]（累加当前列的首元素）
    """
    # 步骤 1：获取网格尺寸
    # TODO: 获取行数 n 和列数 m
    n, m = len(grid), len(grid[0])

    # 步骤 2：创建一维 dp 数组
    # TODO: 创建长度为 m 的一维数组，初始值全为 0
    dp = [0] * m

    # 步骤 3：初始化第一行
    # TODO 1: 设置 dp[0] = grid[0][0]
    dp[0] = grid[0][0]

    # TODO 2: 遍历 j 从 1 到 m-1，设置 dp[j] = dp[j-1] + grid[0][j]
    for j in range(1, m):
        dp[j] = dp[j - 1] + grid[0][j]

    # 步骤 4：处理后续每一行
    # 遍历 i 从 1 到 n-1（从第二行开始）
    for i in range(1, n):

        # 步骤 5：更新首列
        # TODO: dp[0] 需要累加上当前行的第一个元素 grid[i][0]
        # 因为首列只能从正上方到达，所以是 dp[0] += grid[i][0]
        dp[0] += grid[i][0]

        # 步骤 6：更新其余列
        # 遍历 j 从 1 到 m-1
        for j in range(1, m):

            # 步骤 7：状态转移（一维版本）
            # TODO: 取两种情况的最小值 + 当前格子的值：
            #   - 上方：dp[j]（未更新的旧值，代表上一行同列）
            #   - 左方：dp[j-1]（已更新的新值，代表当前行前一列）
            dp[j] = min(dp[j], dp[j - 1]) + grid[i][j]

    # 步骤 8：返回最终结果
    # TODO: 返回 dp[m-1]，即最后一列的值
    return dp[m - 1]