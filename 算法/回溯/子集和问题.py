"""子集和问题（LeetCode 39/40 变体）。

经典回溯+剪枝问题：从数组中选取若干元素，使它们的和等于目标值。
包含两个版本：
- 朴素版：允许重复顺序，会产生重复组合
- 剪枝版：通过排序和索引控制避免重复组合

应用场景：组合求和、零钱兑换、背包问题等
"""


def subset_sum_i_naive(nums: list[int], target: int) -> list[list[int]]:
    """子集和问题：朴素版（允许重复组合）。

    特点：
    - 每个元素可以重复使用
    - 不控制遍历顺序，结果会包含重复的组合
    - 例如 target=4, nums=[2,3] 可能得到 [2,2] 和 [2,2]（相同但顺序不同）

    适用场景：理解回溯的基本框架
    """
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
    """子集和问题：剪枝优化版（无重复组合）。

    优化技巧：
    1. **排序预处理**：将数组排序，便于剪枝
    2. **索引控制**：每层递归从 start 开始，保证组合非递减
       避免了 [2,3] 和 [3,2] 这样的重复
    3. **提前终止**：当当前数字 > 剩余目标时直接 break
       因为后续数字更大，不可能满足条件

    时间复杂度：O(2^n × n)（最坏情况）
    空间复杂度：O(n)（递归深度）
    """
    choices = sorted(nums)
    res: list[list[int]] = []
    state: list[int] = []

    def backtrack(remaining: int, start: int) -> None:
        """回溯函数。

        参数：
            remaining: 还需要凑够的目标值
            start: 从数组的哪个位置开始尝试（避免重复）
        """
        if remaining == 0:
            res.append(list(state))
            return

        for i in range(start, len(choices)):
            choice = choices[i]

            # 剪枝：如果当前数字已经超过剩余目标，后面更大的数字更不行
            if choice > remaining:
                break

            state.append(choice)
            backtrack(remaining - choice, i)  # 元素可重复使用，仍从 i 开始
            state.pop()

    backtrack(target, 0)
    return res


if __name__ == "__main__":
    test_cases = [
        ([2, 3, 6, 7], 7),
        ([2, 3, 5], 8),
        ([1], 1),
    ]

    print("子集和问题测试结果：")
    print("-" * 50)
    for nums, target in test_cases:
        result = subset_sum_i(nums, target)
        print(f"\nnums={nums}, target={target}")
        print(f"找到 {len(result)} 种组合:")
        for combo in result[:5]:  # 只显示前5种
            print(f"  {combo} (和={sum(combo)})")
        if len(result) > 5:
            print(f"  ... 还有 {len(result)-5} 种")