"""零钱兑换问题（Coin Change）- 贪心策略版本。

问题描述：
给定不同面额的硬币和一个总金额，
计算凑出总金额所需的最少硬币个数。
假设每种硬币的数量无限。

注意：
- 贪心解法不一定能得到最优解！
- 只有当硬币面额特殊时（如 1,5,10,25），贪心才有效
- 一般情况需要使用动态规划求解

本实现使用贪心策略（假设硬币已排序）

时间复杂度：O(n)（n 为硬币种类数）
空间复杂度：O(1)
"""


def coin_change_greedy(coins: list[int], amt: int) -> int:
    """使用贪心策略计算最少硬币数量。

    贪心思路：
    每次选择不超过剩余金额的最大面额硬币。

    参数说明：
        coins: 硬币面额列表（需要按升序排列）
        amt: 目标金额

    返回：
        所需的最少硬币数量，若无法凑出则返回 -1

    局限性：
    对于 coins=[1,3,4], amt=6 的情况：
    - 贪心会选择 4+1+1 = 3 枚硬币
    - 但最优解是 3+3 = 2 枚硬币
    """
    i = len(coins) - 1  # 从最大面额开始
    count = 0           # 硬币计数器

    # 循环进行贪心选择，直到金额被凑完或无法继续
    while amt > 0:

        # 找到小于等于剩余金额的最大面额硬币
        while i > 0 and coins[i] > amt:
            i -= 1

        # 选择当前面额的硬币
        amt -= coins[i]
        count += 1

    # 返回结果（如果金额恰好为 0 则成功，否则失败）
    return count if amt == 0 else -1


if __name__ == "__main__":
    test_cases = [
        ([1, 5, 10, 25], 63, 6),   # 25+25+10+1+1+1 = 6枚
        ([1, 2, 5], 11, 3),       # 5+5+1 = 3枚
        ([1, 3, 4], 6, -1),      # 贪心失败案例！最优是2枚但贪心得3枚
    ]

    print("零钱兑换（贪心版本）测试结果：")
    print("-" * 50)
    for coins, amt, expected in test_cases:
        result = coin_change_greedy(coins, amt)
        status = "✅" if result == expected else "⚠️"
        print(f"{status} 面额={coins}, 金额={amt}: {result}枚 (期望:{expected})")