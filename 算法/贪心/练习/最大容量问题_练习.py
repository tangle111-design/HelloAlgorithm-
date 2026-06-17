 """最大容量问题练习版：双指针+贪心策略的经典应用。


问题描述：
给定一个整数数组 height，数组中的每个元素代表一个垂直隔板的高度。
选择两个隔板使得它们与x轴组成的容器容量最大。

容器容量的计算公式：
容量 = min(高度[i], 高度[j]) × |j - i|
- 高度由两个隔板中较短的那个决定
- 宽度是两个隔板之间的距离


示例分析：
输入: height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
输出: 49
解释: 选择第2个位置(高8)和第9个位置(高7)
     容量 = min(8, 7) × (9-2) = 7 × 7 = 49


核心思想 - 为什么使用双指针？
暴力解法需要 O(n²) 时间（枚举所有两两组合）。
通过数学证明可以得出：
- 移动短板可能使面积增大（因为宽度减小但高度可能增加）
- 移动长板不可能使面积增大（宽度减小且高度受限于短板）
因此每次移动短板是安全的贪心选择！
"""


def max_capacity(ht: list[int]) -> int:
    """计算容器的最大容量。

    算法框架：
    1. 初始化双指针 i=0（左端）, j=len(ht)-1（右端）
    2. 计算当前指针形成的容器面积
    3. 更新最大面积
    4. 比较两个指针的高度，移动较短的指针
    5. 重复步骤2-4直到 i >= j

    参数说明：
        ht: 隔板的高度数组

    返回值：
        容器的最大容量
    """
    # 步骤 1：初始化双指针
    # TODO 1: 设置左指针 i = 0（指向数组的第一个元素）
    # TODO 2: 设置右指针 j = len(ht) - 1（指向数组的最后一个元素）
    i, j = 0, len(ht) - 1

    # 步骤 2：初始化结果变量
    # TODO: 创建变量 res = 0，用于记录找到的最大容量
    res = 0

    # 步骤 3：开始循环（当左指针小于右指针时继续）
    # TODO: 使用 while 循环，条件为 i < j
    while i < j:

        # 步骤 4：计算当前容器的容量
        # TODO: 计算 cap = min(ht[i], ht[j]) * (j - i)
        # 解释：
        #   - min(ht[i], ht[j]): 取两个隔板中较短的高度
        #   - (j - i): 两个隔板之间的宽度（索引差）
        cap = min(ht[i], ht[j]) * (j - i)

        # 步骤 5：更新最大容量
        # TODO: 使用 max 函数更新 res = max(res, cap)
        res = max(res, cap)

        # 步骤 6：贪心决策 - 移动指针（关键步骤！）
        # TODO: 比较 ht[i] 和 ht[j]：
        #   若 ht[i] < ht[j]: 左边更短，执行 i += 1（向右移动左指针）
        #   否则: 右边更短或相等，执行 j -= 1（向左移动右指针）
        if ht[i] < ht[j]:
            i += 1
        else:
            j -= 1

    # 步骤 7：返回最终结果
    # TODO: 返回 res（即找到的最大容量）
    return res


if __name__ == "__main__":
    print("=" * 60)
    print("最大容量问题测试")
    print("=" * 60)

    test_cases = [
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
        ([1, 1], 1),
        ([4, 3, 2, 1, 4], 16),
        ([1, 2, 1], 2),
    ]

    all_passed = True
    for heights, expected in test_cases:
        result = max_capacity(heights)

        passed = result == expected
        status = "✅" if passed else "❌"

        print(f"\n{status} 输入: {heights}")
        print(f"   结果: {result}, 期望: {expected}")

        if not passed:
            all_passed = False

    print("\n" + "=" * 60)
    if all_passed:
        print("🎉 所有测试通过！")
    else:
        print("⚠️  存在测试失败，请检查代码")

    print("\n💡 关键要点回顾：")
    print("1. 双指针从两端向中间收缩")
    print("2. 每次移动较短的指针（贪心核心）")
    print("3. 时间复杂度 O(n)，比暴力法的 O(n²) 快很多")