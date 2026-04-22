"""回溯算法基础示例（练习版）。

练习目标：
1. 按“尝试 -> 递归 -> 回退”补全每个例题。
2. 理解何时记录解、何时剪枝。
3. 复用通用 backtrack 框架。
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, TypeVar


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

        # 步骤 1：判断当前节点是否满足条件（值为 7）。
        # 步骤 2：满足则加入 res。

        # 步骤 3：递归遍历左右子树。
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

        # 步骤 1（尝试）：将当前节点加入 path。
        path.append(node)

        # 步骤 2（记录解）：若当前节点值为 7，复制 path 到 res。

        # 步骤 3：递归搜索左右子树。
        pre_order(node.left)
        pre_order(node.right)

        # 步骤 4（回退）：撤销当前层选择（弹出 path 末尾节点）。
        path.pop()

    pre_order(root)
    return res


def find_paths_to_value_7_without_3(root: TreeNode | None) -> list[list[TreeNode]]:
    """例题三：返回值为 7 的路径，且路径中不允许出现值 3。"""
    res: list[list[TreeNode]] = []
    path: list[TreeNode] = []

    def pre_order(node: TreeNode | None) -> None:
        # 步骤 1（剪枝）：空节点或值为 3 的节点直接结束当前分支。
        if node is None:
            return

        # 步骤 2：补全“值为 3 时直接 return”的剪枝逻辑。

        # 步骤 3（尝试）：加入 path。
        path.append(node)

        # 步骤 4（记录解）：若当前节点值为 7，复制 path 到 res。

        # 步骤 5：递归搜索左右子树。
        pre_order(node.left)
        pre_order(node.right)

        # 步骤 6（回退）：撤销当前层选择。
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
    """通用回溯框架（练习版）。"""
    # 步骤 1：若当前状态已是解，调用 record_solution 并返回。
    if is_solution(state):
        return

    # 步骤 2：遍历所有可选 choice。
    for choice in choices:
        # 步骤 3：若当前 choice 不合法，跳过。
        if not is_valid(state, choice):
            continue

        # 步骤 4（尝试）：make_choice。
        make_choice(state, choice)

        # 步骤 5（递归）：继续搜索下一层。
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

        # 步骤 6（回退）：undo_choice，恢复现场。
        undo_choice(state, choice)

