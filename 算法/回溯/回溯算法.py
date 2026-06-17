"""回溯算法基础示例：从二叉树搜索到通用框架。

核心思想：
1. 通过 DFS 遍历解空间树
2. 用"尝试 → 递归 → 回退"维护搜索过程
3. 用约束条件做剪枝，减少无效分支

本文件包含三个递进式示例：
- 例1：简单遍历（查找节点）
- 例2：路径记录（记录根到目标路径）
- 例3：带约束剪枝（路径中不能包含某些值）
- 例4：通用回溯框架
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Generic, TypeVar


@dataclass
class TreeNode:
    """二叉树节点定义。"""

    val: int
    left: TreeNode | None = None
    right: TreeNode | None = None


def find_nodes_with_value_7(root: TreeNode | None) -> list[TreeNode]:
    """例题一：返回所有值为 7 的节点。

    这是最基础的 DFS 遍历，不涉及状态管理。
    时间复杂度：O(n)，空间复杂度：O(h)（h为树高）
    """
    res: list[TreeNode] = []

    def pre_order(node: TreeNode | None) -> None:
        if node is None:
            return
        if node.val == 7:
            res.append(node)
        pre_order(node.left)
        pre_order(node.right)

    pre_order(root)
    return res


def find_paths_to_value_7(root: TreeNode | None) -> list[list[TreeNode]]:
    """例题二：返回根节点到所有值为 7 的节点的完整路径。

    引入状态管理的概念：
    - 使用 path 列表记录当前从根节点到当前节点的路径
    - 在进入子节点前将当前节点加入 path（尝试）
    - 在处理完子节点后移除当前节点（回退）
    - 找到目标时保存 path 的深拷贝

    这是回溯法的雏形！
    """
    res: list[list[TreeNode]] = []
    path: list[TreeNode] = []

    def pre_order(node: TreeNode | None) -> None:
        if node is None:
            return

        # 尝试：将当前节点加入路径
        path.append(node)

        # 检查是否找到目标
        if node.val == 7:
            res.append(list(path))  # 保存深拷贝

        # 继续搜索左右子树
        pre_order(node.left)
        pre_order(node.right)

        # 回退：撤销本层选择（关键！）
        path.pop()

    pre_order(root)
    return res


def find_paths_to_value_7_without_3(root: TreeNode | None) -> list[list[TreeNode]]:
    """例题三：返回值为 7 的路径，且路径中不允许出现值 3。

    剪枝策略：
    - 在递归开始前检查约束条件
    - 如果当前节点违反约束（val==3），直接返回，不再深入
    - 这样可以大幅减少不必要的搜索

    剪枝是回溯法提高效率的核心手段！
    """
    res: list[list[TreeNode]] = []
    path: list[TreeNode] = []

    def pre_order(node: TreeNode | None) -> None:
        # 剪枝：空节点或值为 3 的节点不继续搜索
        if node is None or node.val == 3:
            return

        path.append(node)
        if node.val == 7:
            res.append(list(path))

        pre_order(node.left)
        pre_order(node.right)

        path.pop()

    pre_order(root)
    return res


StateT = TypeVar("StateT")
ChoiceT = TypeVar("ChoiceT")


def backtrack(
    state: StateT,
    choices: list[ChoiceT],
    res: list[StateT],
    is_solution: Callable[[StateT], bool],
    record_solution: Callable[[StateT, list[StateT]], None],
    is_valid: Callable[[StateT, ChoiceT], bool],
    make_choice: Callable[[StateT, ChoiceT], None],
    undo_choice: Callable[[StateT, ChoiceT], None],
) -> None:
    """通用回溯算法框架。

    将回溯法的各个步骤抽象为函数参数，适用于各种回溯问题。

    参数说明：
        state: 当前状态
        choices: 当前的选择列表
        res: 结果存储列表
        is_solution: 判断是否为合法解的函数
        record_solution: 记录解的函数
        is_valid: 判断选择是否合法的函数（用于剪枝）
        make_choice: 执行选择的函数
        undo_choice: 撤销选择的函数（回溯）

    框架流程：
    1. 检查是否为解 → 是则记录并返回
    2. 遍历所有选择
    3. 对每个选择：检查合法性 → 做选择 → 递归 → 撤销选择
    """
    if is_solution(state):
        record_solution(state, res)
        return

    for choice in choices:
        if not is_valid(state, choice):
            continue

        make_choice(state, choice)
        backtrack(
            state,
            choices,
            res,
            is_solution,
            record_solution,
            is_valid,
            make_choice,
            undo_choice,
        )
        undo_choice(state, choice)


if __name__ == "__main__":
    # 构建测试用的二叉树
    #       1
    #      / \
    #     2   3
    #    / \   \
    #   4   7   5
    #      /
    #     7
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(7)
    root.right.right = TreeNode(5)
    root.left.right.left = TreeNode(7)

    print("回溯算法基础示例测试：")
    print("-" * 50)

    nodes = find_nodes_with_value_7(root)
    print(f"\n例1 - 值为7的节点数: {len(nodes)}")

    paths = find_paths_to_value_7(root)
    print(f"例2 - 到值为7的路径数: {len(paths)}")
    for i, path in enumerate(paths):
        print(f"  路径{i+1}: {[n.val for n in path]}")

    filtered_paths = find_paths_to_value_7_without_3(root)
    print(f"例3 - 不含3的路径数: {len(filtered_paths)}")
    for i, path in enumerate(filtered_paths):
        print(f"  路径{i+1}: {[n.val for n in path]}")