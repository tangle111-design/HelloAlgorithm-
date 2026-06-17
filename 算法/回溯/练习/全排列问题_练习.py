"""全排列问题练习版：生成数组的所有排列组合。


问题描述：
给定一个整数数组 nums，返回其所有可能的排列（全排列）。
- 全排列 I：数组中的元素互不相同
- 全排列 II：数组中可能包含重复元素，结果需去重


示例分析（全排列 I）：
输入: nums = [1, 2, 3]
输出:
[1, 2, 3]
[1, 3, 2]
[2, 1, 3]
[2, 3, 1]
[3, 1, 2]
[3, 2, 1]

共 3! = 6 种排列


示例分析（全排列 II）：
输入: nums = [1, 1, 2]
输出:
[1, 1, 2]
[1, 2, 1]
[2, 1, 1]

共 3 种去重后的排列


核心概念：
1. **排列 vs 组合**：排列考虑顺序，组合不考虑
2. **选择标记**：使用 selected 数组记录哪些元素已被选
3. **剪枝去重**：在同一层避免选择相同值的元素
"""


def permutations_i(nums: list[int]) -> list[list[int]]:
    """全排列 I：生成无重复元素数组的所有排列。

    算法框架：
    - 维护一个 state 列表，保存当前正在构建的排列
    - 使用 selected 布尔数组标记每个元素是否已被选中
    - 每次从未选择的元素中挑选一个加入 state
    - 当 state 长度等于 nums 长度时，找到一个完整排列

    回溯过程示例（nums=[1,2,3]）：
    state=[] → 选1 → state=[1] → 选2 → state=[1,2] → 选3 → 找到 [1,2,3]
                                                    → 回溯，撤销3
                                           → 回溯，撤销2
                                    → 选3 → state=[1,3] → 选2 → 找到 [1,3,2]
    ...
    """
    # 步骤 1：创建结果列表
    # TODO: 创建空列表 res，用于存储所有找到的排列
    res: list[list[int]] = []

    # 步骤 2：创建状态列表（当前正在构建的排列）
    # TODO: 创建空列表 state
    state: list[int] = []

    # 步骤 3：创建选择标记数组
    # TODO: 创建长度为 len(nums) 的布尔列表 selected，初始值全为 False
    # 含义：selected[i] = True 表示第 i 个元素已被选入当前排列
    selected = [False] * len(nums)

    # 步骤 4：定义回溯函数
    def backtrack() -> None:
        """尝试构建完整的排列。"""
        # 步骤 5：检查是否完成（终止条件）
        # TODO: 若 len(state) == len(nums)，表示已经选满了所有元素
        #       将 state 的深拷贝添加到 res 中，然后 return
        if len(state) == len(nums):
            res.append(list(state))
            return

        # 步骤 6：遍历所有可选元素
        # TODO: 使用 enumerate 遍历 nums，同时获取索引 i 和值 choice
        for i, choice in enumerate(nums):

            # 步骤 7：检查是否已选择（剪枝）
            # TODO: 若 selected[i] 为 True，跳过这个元素（continue）
            if selected[i]:
                continue

            # 步骤 8：做选择
            # TODO 1: 将 selected[i] 标记为 True
            selected[i] = True

            # TODO 2: 将 choice 添加到 state
            state.append(choice)

            # 步骤 9：递归调用（进入下一层）
            # TODO: 调用 backtrack()
            backtrack()

            # 步骤 10：撤销选择（回溯！）
            # TODO 1: 从 state 移除最后一个元素（state.pop()）
            state.pop()

            # TODO 2: 将 selected[i] 恢复为 False
            selected[i] = False

    # 步骤 11：启动回溯搜索
    # TODO: 调用 backtrack()
    backtrack()

    # 步骤 12：返回结果
    # TODO: 返回 res
    return res


def permutations_ii(nums: list[int]) -> list[list[int]]:
    """全排列 II：处理包含重复元素的数组。

    新增挑战：
    当数组包含重复元素时（如 [1,1,2]），朴素的全排列算法会产生重复结果。
    例如：交换两个 1 的位置会得到"不同"但实际相同的排列。

    解决方案 - 同层去重：
    在每一层递归中，使用一个集合 duplicated 记录已经尝试过的值。
    如果当前值已经在 duplicated 中，则跳过它。

    关键理解：
    - 这个 set 是在每层递归开始时重新创建的（局部变量）
    - 它只防止同一层中选择相同值
    - 不同层可以选择相同的值（因为它们在排列的不同位置）

    示例（nums=[1,1,2]）：
    第一层：尝试第1个1 → duplicated={1}
           尝试第2个1 → 发现 1 在 duplicated 中 → 跳过！（去重成功）
           尝试 2 → 正常处理
    """
    # 步骤 1：初始化数据结构
    # TODO 1: 创建空列表 res
    # TODO 2: 创建空列表 state
    # TODO 3: 创建布尔列表 selected，长度为 len(nums)，初始值全为 False
    res: list[list[int]] = []
    state: list[int] = []
    selected = [False] * len(nums)

    # 步骤 2：定义带去重逻辑的回溯函数
    def backtrack() -> None:
        """带有同层去重的回溯函数。"""
        # 步骤 3：终止条件（与上面相同）
        # TODO: 若 len(state) == len(nums)，保存并 return
        if len(state) == len(nums):
            res.append(list(state))
            return

        # 步骤 4：创建本层的去重集合（关键！）
        # TODO: 创建空集合 duplicated，用于记录本层已尝试过的值
        duplicated: set[int] = set()

        # 步骤 5：遍历所有可选元素
        # TODO: 使用 enumerate 遍历 nums
        for i, choice in enumerate(nums):

            # 步骤 6：双重剪枝判断
            # TODO: 如果以下任一条件成立，则 continue 跳过：
            #   条件1: selected[i] == True（该元素已被选）
            #   条件2: choice in duplicated（该值在本层已尝试过）
            if selected[i] or choice in duplicated:
                continue

            # 步骤 7：记录已尝试的值（去重关键步骤！）
            # TODO: 将 choice 添加到 duplicated 集合中
            duplicated.add(choice)

            # 步骤 8：做选择（与上面相同）
            # TODO 1: selected[i] = True
            # TODO 2: state.append(choice)
            selected[i] = True
            state.append(choice)

            # 步骤 9：递归调用
            # TODO: 调用 backtrack()
            backtrack()

            # 步骤 10：撤销选择
            # TODO 1: state.pop()
            # TODO 2: selected[i] = False
            state.pop()
            selected[i] = False

    # 步骤 11：启动搜索
    # TODO: 调用 backtrack()
    backtrack()

    # 步骤 12：返回结果
    # TODO: 返回 res
    return res


if __name__ == "__main__":
    print("=" * 60)
    print("全排列问题测试")
    print("=" * 60)

    # 测试全排列 I
    print("\n【测试1】全排列 I（无重复元素）")
    nums1 = [1, 2, 3]
    result_i = permutations_i(nums1)
    print(f"输入: {nums1}")
    print(f"排列数: {len(result_i)} (期望: {len(set(tuple(p) for p in result_i))})")
    for i, perm in enumerate(result_i):
        print(f"  {i+1}. {perm}")

    # 测试全排列 II
    print("\n【测试2】全排列 II（有重复元素）")
    test_cases = [
        ([1, 1, 2], 3),
        ([1, 2, 2], 3),
    ]

    all_passed = True
    for nums, expected_count in test_cases:
        result_ii = permutations_ii(nums)
        actual_count = len(result_ii)

        passed = actual_count == expected_count
        status = "✅" if passed else "❌"

        print(f"\n{status} 输入: {nums}")
        print(f"   排列数: {actual_count} (期望: {expected_count})")

        if not passed:
            all_passed = False

        for perm in result_ii:
            print(f"     {perm}")

    print("\n" + "=" * 60)
    if all_passed:
        print("🎉 所有测试通过！")
    else:
        print("⚠️  存在测试失败，请检查代码")