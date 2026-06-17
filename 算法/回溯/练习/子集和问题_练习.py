"""子集和问题练习版：回溯算法+剪枝优化。


问题描述：
给定一个正整数数组 nums 和一个目标值 target，
从数组中选取若干个元素（每个元素可以重复使用），
使得这些元素的和恰好等于 target。
找出所有可能的组合（组合不考虑顺序，即 [2,2,3] 和 [2,3,2] 视为相同）。


示例分析：
输入: nums = [2, 3, 6, 7], target = 7
输出:
- [2, 2, 3] (2+2+3=7)
- [7]       (7=7)

输入: nums = [2, 3, 5], target = 8
输出:
- [2, 2, 2, 2]
- [2, 3, 3]
- [3, 5]


关键概念：
1. **回溯法**：通过递归穷举所有可能的选择，并在不满足条件时返回
2. **剪枝**：提前终止不可能的分支，减少不必要的计算
3. **组合 vs 排列**：组合不考虑顺序，需要通过索引控制避免重复
"""


def subset_sum_i_naive(nums: list[int], target: int) -> list[list[int]]:
    """子集和问题：朴素版实现。

    特点说明：
    - 这是一个基础的回溯框架
    - 每次从数组的第一个元素开始遍历
    - 不控制顺序，所以会产生重复的组合

    为什么会产生重复？
    例如 target=4, nums=[1,3]:
    - 第一次选择 1，然后选择 3 → 得到 [1,3]
    - 第一次选择 3，然后选择 1 → 得到 [3,1]
    这两个其实是相同的组合！

    本函数用于理解回溯的基本结构，
    实际应用中应该使用下面的剪枝优化版本。
    """
    # 步骤 1：创建结果列表
    # TODO: 创建空列表 res，用于存储找到的所有组合
    res: list[list[int]] = []

    # 步骤 2：创建状态列表（当前正在构建的组合）
    # TODO: 创建空列表 state，用于临时保存当前选择的元素
    state: list[int] = []

    # 步骤 3：定义回溯函数
    def backtrack(total: int) -> None:
        """尝试凑出目标和。

        参数：
            total: 当前已选元素的总和
        """
        # 步骤 4：检查是否达到目标（终止条件）
        # TODO: 若 total == target，表示找到了一个有效组合
        #       将 state 的深拷贝添加到 res 中，然后 return
        if total == target:
            res.append(list(state))
            return

        # 步骤 5：遍历所有可选数字
        # TODO: 使用 for 循环遍历 nums 中的每一个 choice
        for choice in nums:

            # 步骤 6：剪枝判断
            # TODO: 如果 total + choice > target，则跳过这个 choice（continue）
            # 解释：加上这个数字后超过目标值了，不能选
            if total + choice > target:
                continue

            # 步骤 7：做选择（将 choice 添加到 state）
            # TODO: 调用 state.append(choice)
            state.append(choice)

            # 步骤 8：递归调用（进入下一层决策）
            # TODO: 调用 backtrack(total + choice)，传入新的总和
            backtrack(total + choice)

            # 步骤 9：撤销选择（回溯！移除最后一个元素）
            # TODO: 调用 state.pop()，恢复 state 到之前的状态
            state.pop()

    # 步骤 10：启动回溯搜索
    # TODO: 调用 backtrack(0)，从总和为 0 开始搜索
    backtrack(0)

    # 步骤 11：返回结果
    # TODO: 返回 res
    return res


def subset_sum_i(nums: list[int], target: int) -> list[list[int]]:
    """子集和问题：剪枝优化版（推荐使用）。

    相比朴素版的三大改进：

    改进1 - 排序预处理：
    将数组排序后，可以使用更高效的剪枝策略。
    当遇到一个数字 > 剩余目标时，后面的数字更大，可以直接 break。

    改进2 - 索引控制（核心！）：
    引入 start 参数，每层只从 start 位置开始遍历。
    这样保证了选择的顺序是非递减的，避免了重复组合。
    例如：只能得到 [2,3]，不会同时得到 [2,3] 和 [3,2]

    改进3 - 提前终止：
    由于数组已排序，当 choice > remaining 时直接 break（不是 continue），
    因为后续数字更大，都不可能满足条件。
    这比朴素版的 continue 更高效。
    """
    # 步骤 1：排序预处理
    # TODO: 对 nums 进行排序，赋值给 choices
    # 提示：使用 sorted(nums) 函数
    choices = sorted(nums)

    # 步骤 2：初始化结果和状态列表
    # TODO 1: 创建空列表 res
    # TODO 2: 创建空列表 state
    res: list[list[int]] = []
    state: list[int] = []

    # 步骤 3：定义带参数的回溯函数
    def backtrack(remaining: int, start: int) -> None:
        """优化的回溯函数。

        参数：
            remaining: 还需要凑够的目标值
            start: 从数组的哪个位置开始尝试（控制顺序的关键！）
        """
        # 步骤 4：检查是否完成
        # TODO: 若 remaining == 0，保存当前组合并 return
        if remaining == 0:
            res.append(list(state))
            return

        # 步骤 5：从 start 位置开始遍历
        # TODO: 使用 for 循环遍历 i 从 start 到 len(choices)-1
        for i in range(start, len(choices)):

            # 步骤 6：获取当前候选数字
            # TODO: 获取 choices[i]，赋值给 choice
            choice = choices[i]

            # 步骤 7：高效剪枝（提前终止）
            # TODO: 如果 choice > remaining，直接 break（不是 continue！）
            # 解释：因为数组已排序，后续数字都 >= choice，都不可能满足条件
            if choice > remaining:
                break

            # 步骤 8：做选择
            # TODO: 调用 state.append(choice)
            state.append(choice)

            # 步骤 9：递归调用（注意参数！）
            # TODO: 调用 backtrack(remaining - choice, i)
            # 关键点：第三个参数是 i（不是 i+1），因为元素可以重复使用！
            backtrack(remaining - choice, i)

            # 步骤 10：撤销选择
            # TODO: 调用 state.pop()
            state.pop()

    # 步骤 11：启动搜索
    # TODO: 调用 backtrack(target, 0)，初始剩余值为 target，从位置0开始
    backtrack(target, 0)

    # 步骤 12：返回结果
    # TODO: 返回 res
    return res


if __name__ == "__main__":
    print("=" * 60)
    print("子集和问题测试")
    print("=" * 60)

    test_cases = [
        ([2, 3, 6, 7], 7, 2),   # 预期有2种组合
        ([2, 3, 5], 8, 3),      # 预期有3种组合
        ([1], 1, 1),            # 只有1种组合
    ]

    all_passed = True
    for nums, target, expected_count in test_cases:
        result = subset_sum_i(nums, target)
        actual_count = len(result)

        passed = actual_count == expected_count
        status = "✅" if passed else "❌"

        print(f"\n{status} nums={nums}, target={target}")
        print(f"   找到 {actual_count} 种组合 (期望 {expected_count})")

        if not passed:
            all_passed = False

        # 显示具体组合
        for i, combo in enumerate(result):
            print(f"     组合{i+1}: {combo} (和={sum(combo)})")

    print("\n" + "=" * 60)
    if all_passed:
        print("🎉 所有测试通过！")
    else:
        print("⚠️  存在测试失败，请检查代码")