"""全排列问题（LeetCode 46/47）。

经典回溯算法应用：生成数组的所有排列。
包含两个版本：
- 全排列 I：输入元素互不相同
- 全排列 II：输入可包含重复元素，需去重

核心技巧：
- 使用 selected 数组标记已选元素
- 全排列 II 需要在同一层避免选择相同值
"""


def permutations_i(nums: list[int]) -> list[list[int]]:
    """全排列 I：元素互不相同的数组。

    算法思路：
    - 使用 selected 数组标记哪些元素已被选入当前排列
    - 每次从未选择的元素中挑选一个加入 state
    - 当 state 长度等于 nums 长度时，找到一个完整排列

    时间复杂度：O(n × n!)
    空间复杂度：O(n)
    """
    res: list[list[int]] = []
    state: list[int] = []
    selected = [False] * len(nums)

    def backtrack() -> None:
        if len(state) == len(nums):
            res.append(list(state))
            return

        for i, choice in enumerate(nums):
            if selected[i]:
                continue

            selected[i] = True
            state.append(choice)
            backtrack()
            state.pop()
            selected[i] = False

    backtrack()
    return res


def permutations_ii(nums: list[int]) -> list[list[int]]:
    """全排列 II：输入可包含重复元素。

    去重策略：
    在同一层递归中，如果某个值已经被尝试过，则跳过后续相同值。
    使用 set 记录本层已尝试的值，保证每个值只被选一次。

    例如 nums=[1,1,2]：
    - 第一层选第1个1后，第2个1会被跳过（因为值重复）
    - 但不同层可以选择相同的1（因为它们在不同位置）
    """
    res: list[list[int]] = []
    state: list[int] = []
    selected = [False] * len(nums)

    def backtrack() -> None:
        if len(state) == len(nums):
            res.append(list(state))
            return

        # 同一层中，相同数值只尝试一次（关键去重逻辑）
        duplicated: set[int] = set()
        for i, choice in enumerate(nums):
            if selected[i] or choice in duplicated:
                continue

            duplicated.add(choice)
            selected[i] = True
            state.append(choice)
            backtrack()
            state.pop()
            selected[i] = False

    backtrack()
    return res


if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3], 6),      # 3! = 6 种排列
        ([1, 1, 2], 3),      # 去重后有3种排列
    ]

    print("全排列问题测试结果：")
    print("-" * 50)
    for nums, expected_count in test_cases:
        result_i = permutations_i(nums)
        result_ii = permutations_ii(nums)
        print(f"\nnums={nums}:")
        print(f"  全排列I: {len(result_i)} 种 (无去重)")
        print(f"  全排列II: {len(result_ii)} 种 (去重)")
        for perm in result_ii[:5]:
            print(f"    {perm}")