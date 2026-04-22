"""全排列问题（练习版）：回溯法。"""


def permutations_i(nums: list[int]) -> list[list[int]]:
    """全排列 I：输入元素互不相同。"""
    res: list[list[int]] = []
    state: list[int] = []
    selected = [False] * len(nums)

    def backtrack() -> None:
        # 步骤 1：当 state 长度等于 nums 长度时，记录一个完整排列并返回。
        if len(state) == len(nums):
            return

        # 步骤 2：遍历每个候选元素。
        for i, choice in enumerate(nums):
            # 步骤 3：若该元素已被使用，跳过。
            if selected[i]:
                continue

            # 步骤 4（尝试）：标记已使用，并加入 state。
            selected[i] = True
            state.append(choice)

            # 步骤 5：递归进入下一层。
            backtrack()

            # 步骤 6（回退）：弹出 state，并恢复 selected。
            state.pop()
            selected[i] = False

    backtrack()
    return res


def permutations_ii(nums: list[int]) -> list[list[int]]:
    """全排列 II：输入可包含重复元素，返回不重复排列。"""
    res: list[list[int]] = []
    state: list[int] = []
    selected = [False] * len(nums)

    def backtrack() -> None:
        # 步骤 1：完成排列时，复制 state 到 res。
        if len(state) == len(nums):
            return

        # 步骤 2：同一层去重集合（用于跳过重复数值分支）。
        duplicated: set[int] = set()

        for i, choice in enumerate(nums):
            # 步骤 3：若元素已使用，或该数值在当前层已尝试，跳过。
            if selected[i] or choice in duplicated:
                continue

            # 步骤 4：把当前数值加入 duplicated。
            duplicated.add(choice)

            # 步骤 5（尝试）：更新 selected 与 state。
            selected[i] = True
            state.append(choice)

            # 步骤 6：递归。
            backtrack()

            # 步骤 7（回退）：恢复 state 与 selected。
            state.pop()
            selected[i] = False

    backtrack()
    return res
