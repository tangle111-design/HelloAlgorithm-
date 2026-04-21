from __future__ import annotations


class TreeNode:
    """二叉树节点。"""

    def __init__(self, val: int, left: TreeNode | None = None, right: TreeNode | None = None):
        self.val = val
        self.left = left
        self.right = right


def pre_order_iterative(root: TreeNode | None) -> list[int]:
    """前序遍历（迭代）练习。"""
    if root is None:
        return []

    res: list[int] = []
    stack: list[TreeNode] = [root]

    # 步骤提示：
    # 1) 栈顶弹出节点并访问。
    # 2) 先压右子节点，再压左子节点（保证左先处理）。
    # 3) 循环直到栈为空。

    return res


def in_order_iterative(root: TreeNode | None) -> list[int]:
    """中序遍历（迭代）练习。"""
    res: list[int] = []
    stack: list[TreeNode] = []
    curr = root

    # 步骤提示：
    # 1) 沿左链持续入栈。
    # 2) 无左节点时弹栈并访问。
    # 3) 访问后转向右子树继续。
    # 4) 条件是 curr 不空或 stack 不空。

    return res


def post_order_iterative(root: TreeNode | None) -> list[int]:
    """后序遍历（迭代，反转法）练习。"""
    if root is None:
        return []

    res: list[int] = []
    stack: list[TreeNode] = [root]

    # 步骤提示：
    # 1) 按“根-右-左”顺序收集结果。
    # 2) 最后整体反转，得到“左-右-根”。

    return res


def post_order_iterative_alt(root: TreeNode | None) -> list[int]:
    """后序遍历（迭代，不反转）练习。"""
    if root is None:
        return []

    res: list[int] = []
    stack: list[TreeNode] = []
    prev: TreeNode | None = None
    curr = root

    # 步骤提示：
    # 1) 先一路向左入栈。
    # 2) 查看栈顶节点：
    #    - 若右子树存在且未访问，转向右子树。
    #    - 否则访问栈顶并弹栈，同时更新 prev。

    return res
