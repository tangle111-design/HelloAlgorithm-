"""全排列问题：回溯法。"""


def permutations_i(nums: list[int]) -> list[list[int]]:
    """全排列 I：输入元素互不相同。"""
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
    """全排列 II：输入可包含重复元素，返回不重复排列。"""
    res: list[list[int]] = []
    state: list[int] = []
    selected = [False] * len(nums)

    def backtrack() -> None:
        if len(state) == len(nums):
            res.append(list(state))
            return

        # 同一层中，相同数值只尝试一次
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