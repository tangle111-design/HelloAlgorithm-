"""分数背包问题（Fractional Knapsack Problem）。

问题描述：
给定 n 个物品，每个物品有重量和价值，以及一个容量有限的背包。
与 0-1 背包不同，分数背包允许选择物品的一部分（按比例计算价值）。

贪心策略：
按照单位重量价值（价值/重量）从高到低排序，
优先选择单位价值最高的物品，尽可能多地装入背包。

适用场景：资源分配、投资组合优化等

时间复杂度：O(n log n)（主要来自排序）
空间复杂度：O(n)
"""

import math


class Item:
    """物品类，包含重量和价值两个属性。"""

    def __init__(self, w: int, v: int):
        self.w = w  # 物品重量
        self.v = v  # 物品价值


def fractional_knapsack(wgt: list[int], val: list[int], cap: int) -> int:
    """分数背包问题求解器。

    参数说明：
        wgt: 各个物品的重量列表
        val: 各个物品的价值列表
        cap: 背包的最大容量

    返回：
        背包能装下的最大总价值

    算法步骤：
    1. 创建物品对象并计算单位价值
    2. 按单位价值降序排序
    3. 贪心地依次选择物品（能装整个就装整个，否则装部分）
    """
    # 创建物品列表
    items = [Item(w, v) for w, v in zip(wgt, val)]

    # 按照单位价值（价值/重量）从高到低排序
    items.sort(key=lambda item: item.v / item.w, reverse=True)

    # 贪心选择过程
    res = 0  # 记录已获得的总价值

    for item in items:
        if item.w <= cap:
            # 剩余容量充足，将整个物品装入背包
            res += item.v
            cap -= item.w
        else:
            # 剩余容量不足，只装物品的一部分
            # 价值 = 单位价值 × 剩余容量
            res += (item.v / item.w) * cap
            break  # 背包已满，结束

    return res


if __name__ == "__main__":
    test_cases = [
        ([10, 20, 30, 20, 10], [60, 100, 120, 80, 50], 50, 240),
        ([20, 30, 10], [100, 120, 60], 50, 240),
    ]

    print("分数背包问题测试结果：")
    print("-" * 50)
    for wgt, val, cap, expected in test_cases:
        result = fractional_knapsack(wgt, val, cap)
        status = "✅" if result == expected else "❌"
        print(f"{status} 容量={cap}: 最大价值={result:.0f} (期望: {expected})")