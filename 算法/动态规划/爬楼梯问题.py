"""爬楼梯问题（LeetCode 70）。

经典动态规划入门题，本质是斐波那契数列。
问题描述：有 n 阶楼梯，每次可以走 1 阶或 2 阶，求到达楼顶的方法数。

示例：
- n=1: 1 种 (1)
- n=2: 2 种 (1+1, 2)
- n=3: 3 种 (1+1+1, 1+2, 2+1)
"""


def backtrack(choices: list[int], state: int, n: int, res: list[int]) -> None:
    """回溯法统计方案数。"""
    if state == n:
        res[0] += 1
        return
    for choice in choices:
        if state + choice > n:
            continue
        backtrack(choices, state + choice, n, res)


def climbing_stairs_backtrack(n: int) -> int:
    """爬楼梯：回溯解法（暴力枚举所有路径）。"""
    if n <= 0:
        return 0
    choices = [1, 2]
    res = [0]
    backtrack(choices, 0, n, res)
    return res[0]


def dfs(i: int) -> int:
    """暴力搜索（递归，指数级时间复杂度）。"""
    if i == 1 or i == 2:
        return i
    return dfs(i - 1) + dfs(i - 2)


def climbing_stairs_dfs(n: int) -> int:
    """爬楼梯：递归搜索。"""
    if n <= 0:
        return 0
    if n <= 2:
        return n
    return dfs(n)


def dfs_mem(i: int, mem: list[int]) -> int:
    """记忆化搜索（带缓存）。"""
    if i == 1 or i == 2:
        return i
    if mem[i] != -1:
        return mem[i]
    mem[i] = dfs_mem(i - 1, mem) + dfs_mem(i - 2, mem)
    return mem[i]


def climbing_stairs_dfs_mem(n: int) -> int:
    """爬楼梯：记忆化搜索（避免重复计算）。"""
    if n <= 0:
        return 0
    if n <= 2:
        return n
    mem = [-1] * (n + 1)
    return dfs_mem(n, mem)


def climbing_stairs_dp(n: int) -> int:
    """爬楼梯：动态规划（一维数组）。

    状态定义：
    - dp[i] 表示到达第 i 阶的方法数

    状态转移：
    - dp[i] = dp[i-1] + dp[i-2]
      可以从第 i-1 阶走 1 步，或从第 i-2 阶走 2 步

    边界条件：
    - dp[1] = 1, dp[2] = 2
    """
    if n <= 0:
        return 0
    if n <= 2:
        return n

    dp = [0] * (n + 1)
    dp[1], dp[2] = 1, 2

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


def climbing_stairs_dp_comp(n: int) -> int:
    """爬楼梯：空间优化（只用两个变量）。

    优化技巧：
    - 发现 dp[i] 只依赖前两个状态 dp[i-1] 和 dp[i-2]
    - 用两个变量 a, b 滚动更新即可
    - 空间复杂度从 O(n) 降至 O(1)

    类似斐波那契数列的滚动数组优化
    """
    if n <= 0:
        return 0
    if n <= 2:
        return n

    a, b = 1, 2  # a=dp[1], b=dp[2]

    for _ in range(3, n + 1):
        a, b = b, a + b  # 滚动更新

    return b


if __name__ == "__main__":
    test_cases = [1, 2, 3, 4, 5, 10]

    print("爬楼梯问题测试结果：")
    print("-" * 50)
    for n in test_cases:
        result_dp = climbing_stairs_dp(n)
        result_comp = climbing_stairs_dp_comp(n)
        print(f"n={n:2d}: DP结果={result_dp}, 优化版={result_comp}")