 """分数背包问题练习版：允许部分选择的背包优化问题。


问题描述：
给定 n 个物品，每个物品有重量和价值，
以及一个容量有限的背包。
与 0-1 背包不同，**分数背包可以选择物品的一部分**。
目标是在不超过背包容量的前提下，最大化背包中物品的总价值。

与 0-1 背包的区别：
- 0-1 背包：物品只能完整地选或不选（0 或 1）
- 分数背包：物品可以拆分成任意比例选择（0 到 1 之间）


示例分析：
物品:   A    B    C
重量:  10   20   30
价值:  60  120  120
单位价值:6    6    4

背包容量 = 50
最优方案：
1. 选 A（重10，价值60），剩余40
2. 选 B（重20，价值120），剩余20
3. 选 C 的 20/30 = 2/3，价值 80
总价值 = 60 + 120 + 80 = 260


贪心策略：
按单位重量价值（价值÷重量）降序排列，
优先选择单位价值最高的物品！
"""

import math


class Item:
    """物品类，用于存储物品的重量和价值信息。

    属性说明：
        w: 物品的重量（正整数）
        v: 物品的价值（正整数）
    """

    def __init__(self, w: int, v: int):
        self.w = w  # 物品重量
        self.v = v  # 物品价值


def fractional_knapsack(wgt: list[int], val: list[int], cap: int) -> int:
    """分数背包问题的求解函数。

    算法流程：
    1. 将重量和价值配对创建物品对象列表
    2. 计算每个物品的单位价值（价值 / 重量）
    3. 按单位价值从高到低排序
    4. 依次尝试装入每个物品：
       - 能装整个就装整个
       - 不能装整个就装一部分（填满剩余空间）

    参数说明：
        wgt: 各个物品的重量列表 [w1, w2, ..., wn]
        val: 各个物品的价值列表 [v1, v2, ..., vn]
        cap: 背包的最大容量（正整数）

    返回值：
        在容量限制下能获得的最大总价值
    """
    # 步骤 1：创建物品对象列表
    # TODO: 使用列表推导式，将 wgt 和 val 配对创建 Item 对象列表
    # 提示：[Item(w, v) for w, v in zip(wgt, val)]
    items = [Item(w, v) for w, v in zip(wgt, val)]

    # 步骤 2：按单位价值排序（贪心的核心！）
    # TODO: 对 items 进行排序，排序依据是 item.v / item.w（单位价值）
    #       使用 reverse=True 表示降序排列（单位价值高的排前面）
    items.sort(key=lambda item: item.v / item.w, reverse=True)

    # 步骤 3：初始化总价值和剩余容量
    # TODO 1: 创建变量 res = 0，表示已获得的总价值
    # TODO 2: 注意 cap 参数本身就是剩余容量，不需要额外变量
    res = 0

    # 步骤 4：遍历所有物品进行贪心选择
    # TODO: 使用 for 循环遍历 items 列表中的每一个 item
    for item in items:

        # 步骤 5：判断是否能完整装入
        # TODO: 如果 item.w <= cap（物品重量不超过剩余容量）：
        if item.w <= cap:

            # 步骤 6：完整装入该物品
            # TODO 1: 将物品的完整价值加到 res 上（res += item.v）
            # TODO 2: 从剩余容量中减去物品重量（cap -= item.w）
            res += item.v
            cap -= item.w

        else:
            # 步骤 7：只能装入物品的一部分
            # TODO: 计算并添加部分物品的价值：
            #       value_to_add = (item.v / item.w) * cap
            #       解释：单位价值 × 剩余容量 = 可获得的价值
            res += (item.v / item.w) * cap

            # 步骤 8：背包已满，结束循环
            # TODO: 执行 break 语句跳出循环
            break

    # 步骤 9：返回最终的总价值
    # TODO: 返回 res
    return res


if __name__ == "__main__":
    print("=" * 60)
    print("分数背包问题测试")
    print("=" * 60)

    test_cases = [
        {
            "wgt": [10, 20, 30, 20, 10],
            "val": [60, 100, 120, 80, 50],
            "cap": 50,
            "expected": 240,
        },
        {
            "wgt": [20, 30, 10],
            "val": [100, 120, 60],
            "cap": 50,
            "expected": 240,
        },
    ]

    all_passed = True
    for idx, case in enumerate(test_cases, 1):
        wgt, val, cap, expected = case["wgt"], case["val"], case["cap"], case["expected"]
        result = fractional_knapsack(wgt, val, cap)

        passed = abs(result - expected) < 0.01
        status = "✅" if passed else "❌"

        print(f"\n{status} 测试 {idx}:")
        print(f"   重量: {wgt}")
        print(f"   价值: {val}")
        print(f"   容量: {cap}")
        print(f"   结果: {result:.1f}, 期望: {expected}")

        if not passed:
            all_passed = False

    print("\n" + "=" * 60)
    if all_passed:
        print("🎉 所有测试通过！")
    else:
        print("⚠️  存在测试失败，请检查代码")

    print("\n💡 关键要点回顾：")
    print("1. 分数背包的核心是计算'单位重量价值'")
    print("2. 贪心策略：优先选择单位价值最高的物品")
    print("3. 允许部分选择是分数背包与 0-1 背包的本质区别")
    print("4. 排序时间复杂度 O(n log n)，选择过程 O(n)")