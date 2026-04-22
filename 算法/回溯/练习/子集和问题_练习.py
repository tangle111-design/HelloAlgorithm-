"""子集和问题（练习版）：回溯法。"""


def subset_sum_i_naive(nums: list[int], target: int) -> list[list[int]]:
    """朴素版：允许重复顺序，结果会包含重复组合。"""
    res: list[list[int]] = []
    state: list[int] = []

    def backtrack(total: int) -> None:
        # 步骤 1：若 total 恰好等于 target，记录当前 state 并返回。
        if total == target:
            return

        # 步骤 2：枚举所有 choice。
        for choice in nums:
            # 步骤 3：若 total + choice 超过 target，剪枝跳过。
            if total + choice > target:
                continue

            # 步骤 4（尝试）：将 choice 加入 state。
            state.append(choice)

            # 步骤 5：递归搜索（参数更新为 total + choice）。
            backtrack(total + choice)

            # 步骤 6（回退）：弹出最后一个选择。
            state.pop()

    backtrack(0)
    return res


def subset_sum_i(nums: list[int], target: int) -> list[list[int]]:
    """剪枝版：每个元素可重复使用，但结果不包含重复组合。"""
    choices = sorted(nums)
    res: list[list[int]] = []
    state: list[int] = []

    def backtrack(remaining: int, start: int) -> None:
        # 步骤 1：若 remaining 为 0，记录解并返回。
        if remaining == 0:
            return

        # 步骤 2：从 start 开始遍历，保证索引非递减，避免组合重复。
        for i in range(start, len(choices)):
            choice = choices[i]

            # 步骤 3：若 choice 大于 remaining，后续更大，直接 break。
            if choice > remaining:
                break

            # 步骤 4（尝试）：加入当前 choice。
            state.append(choice)

            # 步骤 5：递归搜索。注意：元素可重复使用，下一层仍从 i 开始。
            backtrack(remaining - choice, i)

            # 步骤 6（回退）：撤销本层选择。
            state.pop()

    backtrack(target, 0)
    return res
