"""爬楼梯问题练习。"""


def backtrack(choices: list[int], state: int, n: int, res: list[int]) -> None:
    """回溯统计方案数。"""
    # 当到达第 n 阶时，记录 1 种方案
    if state == n:
        res[0] += 1
        return

    # 遍历下一步可选决策
    for choice in choices:
        # 剪枝：不允许越过第 n 阶
        if state + choice > n:
            continue
        backtrack(choices, state + choice, n, res)


def climbing_stairs_backtrack(n: int) -> int:
    """爬楼梯：回溯。"""
    if n <= 0:
        return 0
    choices = [1, 2]
    res = [0]
    backtrack(choices, 0, n, res)
    return res[0]


def dfs(i: int) -> int:
    """暴力搜索。"""
    # 已知最小子问题
    if i == 1 or i == 2:
        return i
    # 状态转移：dp[i] = dp[i-1] + dp[i-2]
    return dfs(i - 1) + dfs(i - 2)


def climbing_stairs_dfs(n: int) -> int:
    """爬楼梯：搜索。"""
    if n <= 0:
        return 0
    if n <= 2:
        return n
    return dfs(n)


def dfs_mem(i: int, mem: list[int]) -> int:
    """记忆化搜索。"""
    if i == 1 or i == 2:
        return i
    # 若已有记录，直接返回
    if mem[i] != -1:
        return mem[i]
    mem[i] = dfs_mem(i - 1, mem) + dfs_mem(i - 2, mem)
    return mem[i]


def climbing_stairs_dfs_mem(n: int) -> int:
    """爬楼梯：记忆化搜索。"""
    if n <= 0:
        return 0
    if n <= 2:
        return n
    mem = [-1] * (n + 1)
    return dfs_mem(n, mem)


def climbing_stairs_dp(n: int) -> int:
    """爬楼梯：动态规划。"""
    if n <= 0:
        return 0
    if n <= 2:
        return n

    # 1) 定义 dp[i] 为到达第 i 阶的方法数
    dp = [0] * (n + 1)
    # 2) 初始化边界
    dp[1], dp[2] = 1, 2
    # 3) 状态转移
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


def climbing_stairs_dp_comp(n: int) -> int:
    """爬楼梯：空间优化。"""
    if n <= 0:
        return 0
    if n <= 2:
        return n

    # 使用滚动变量保存最近两项
    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b
