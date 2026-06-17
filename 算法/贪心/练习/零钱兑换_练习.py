"""零钱兑换练习版：贪心策略与局限性分析。


问题描述：
给定不同面额的硬币数组 coins 和一个总金额 amt，
计算凑出总金额所需的最少硬币个数。
假设每种硬币的数量无限。

示例分析：
coins = [1, 5, 10, 25], amt = 63
贪心过程：
1. 选 25（剩余38，已用1枚）
2. 选 25（剩余13，已用2枚）
3. 选 10（剩余 3，已用3枚）
4. 选 1（剩余 2，已用4枚）
5. 选 1（剩余 1，已用5枚）
6. 选 1（剩余 0，已用6枚）
结果：6 枚硬币


⚠️ 重要提示：贪心解法的局限性！

贪心不一定能得到最优解！
反例：coins=[1,3,4], amt=6
- 贪心选择：4 + 1 + 1 = 3 枚硬币 ❌
- 实际最优：3 + 3 = 2 枚硬币 ✅

只有当硬币面额满足特定条件时（如标准货币体系），
贪心策略才能保证得到最优解。
一般情况需要使用动态规划求解！
"""


def coin_change_greedy(coins: list[int], amt: int) -> int:
    """使用贪心策略计算最少硬币数量。

    贪心思路：
    从最大面额开始，每次选择不超过剩余金额的最大面额硬币。

    参数说明：
        coins: 硬币面额列表（**必须按升序排列**）
        amt: 目标总金额

    返回值：
        所需的最少硬币数量
        若能成功凑出则返回硬币数量
        若无法凑出则返回 -1

    算法流程：
    1. 从最大面额开始（数组末尾）
    2. 找到不超过剩余金额的最大面额
    3. 选择该面额，更新剩余金额和计数器
    4. 重复直到金额为 0 或无法继续
    """
    # 步骤 1：初始化指针位置
    # TODO: 设置 i = len(coins) - 1
    # 含义：从数组的最后一个元素（最大面额）开始
    i = len(coins) - 1

    # 步骤 2：初始化硬币计数器
    # TODO: 设置 count = 0，用于记录使用的硬币总数
    count = 0

    # 步骤 3：循环进行贪心选择
    # TODO: 使用 while 循环，条件为 amt > 0（还有剩余金额需要凑）
    while amt > 0:

        # 步骤 4：寻找合适面额的硬币
        # TODO: 使用内层 while 循环找到第一个 coins[i] <= amt
        #       如果 coins[i] > amt，则 i -= 1 向左移动
        #       同时确保 i > 0（不能移到负索引）
        while i > 0 and coins[i] > amt:
            i -= 1

        # 步骤 5：选择当前面额的硬币
        # TODO 1: 从剩余金额中减去当前面额（amt -= coins[i]）
        # TODO 2: 硬币计数器加 1（count += 1）
        amt -= coins[i]
        count += 1

    # 步骤 6：返回结果
    # TODO: 判断并返回结果：
    #       若 amt == 0（恰好凑完），返回 count
    #       否则返回 -1（表示失败）
    return count if amt == 0 else -1


if __name__ == "__main__":
    print("=" * 60)
    print("零钱兑换（贪心版本）测试")
    print("=" * 60)

    test_cases = [
        {
            "coins": [1, 5, 10, 25],
            "amt": 63,
            "expected": 6,
            "desc": "标准货币系统（贪心有效）"
        },
        {
            "coins": [1, 2, 5],
            "amt": 11,
            "expected": 3,
            "desc": "5+5+1=11"
        },
        {
            "coins": [1, 3, 4],
            "amt": 6,
            "expected": -1,
            "desc": "贪心失败案例！（最优是2枚但贪心得3枚）"
        },
    ]

    all_passed = True
    for idx, case in enumerate(test_cases, 1):
        coins, amt, expected, desc = case["coins"], case["amt"], case["expected"], case["desc"]
        result = coin_change_greedy(coins, amt)

        passed = result == expected
        status = "✅" if passed else "⚠️"

        print(f"\n{status} 测试 {idx}: {desc}")
        print(f"   面额: {coins}")
        print(f"   金额: {amt}")
        print(f"   结果: {result} 枚硬币 (期望: {expected})")

        if not passed:
            all_passed = False

    print("\n" + "=" * 60)
    if all_passed:
        print("✅ 所有测试符合预期！")
    else:
        print("⚠️  存在贪心失败的案例（这是正常的！）")

    print("\n💡 关键要点回顾：")
    print("1. 贪心从最大面额开始，每次选不超过余额的最大面额")
    print("2. 贪心简单高效但不一定最优！")
    print("3. 对于标准货币体系（如 1,5,10,25），贪心通常有效")
    print("4. 一般情况应使用动态规划保证最优性")
    print("5. 时间复杂度 O(n)，n 为硬币种类数")