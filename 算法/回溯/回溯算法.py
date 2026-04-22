"""回溯算法基础示例。

核心思想：
1. 通过 DFS 遍历解空间。
2. 用“尝试 -> 递归 -> 回退”维护搜索过程。
3. 用约束条件做剪枝，减少无效分支。
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Generic, TypeVar


@dataclass
class TreeNode:
    """二叉树节点。"""

    val: int
    left: TreeNode | None = None
    right: TreeNode | None = None


def find_nodes_with_value_7(root: TreeNode | None) -> list[TreeNode]:
    """例题一：返回所有值为 7 的节点。"""
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
    """例题二：返回根节点到所有值为 7 的节点路径。"""
    res: list[list[TreeNode]] = []
    path: list[TreeNode] = []

    def pre_order(node: TreeNode | None) -> None:
        if node is None:
            return

        # 尝试：将当前节点加入路径
        path.append(node)
        if node.val == 7:
            # 记录解：复制当前路径
            res.append(list(path))

        pre_order(node.left)
        pre_order(node.right)

        # 回退：撤销本层选择
        path.pop()

    pre_order(root)
    return res


def find_paths_to_value_7_without_3(root: TreeNode | None) -> list[list[TreeNode]]:
    """例题三：返回值为 7 的路径，且路径中不允许出现值 3。"""
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
    """通用回溯框架。"""
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