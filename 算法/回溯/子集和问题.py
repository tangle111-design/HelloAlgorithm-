"""子集和问题：回溯法。"""


def subset_sum_i_naive(nums: list[int], target: int) -> list[list[int]]:
    """朴素版：允许重复顺序，结果会包含重复组合。"""
    res: list[list[int]] = []
    state: list[int] = []

    def backtrack(total: int) -> None:
        if total == target:
            res.append(list(state))
            return

        for choice in nums:
            if total + choice > target:
                continue

            state.append(choice)
            backtrack(total + choice)
            state.pop()

    backtrack(0)
    return res


def subset_sum_i(nums: list[int], target: int) -> list[list[int]]:
    """剪枝版：每个元素可重复使用，但结果不包含重复组合。"""
    choices = sorted(nums)
    res: list[list[int]] = []
    state: list[int] = []

    def backtrack(remaining: int, start: int) -> None:
        if remaining == 0:
            res.append(list(state))
            return

        # 从 start 开始遍历，保证索引非递减，避免重复组合
        for i in range(start, len(choices)):
            choice = choices[i]
            if choice > remaining:
                break

            state.append(choice)
            # 元素可重复使用，因此下一层仍从 i 开始
            backtrack(remaining - choice, i)
            state.pop()

    backtrack(target, 0)
    return res