from __future__ import annotations

from typing import Optional

# 假设 TreeNode 已定义（代码片段风格）
class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None


def pre_order(root: Optional[TreeNode]) -> list[int]:
    """前序遍历"""
    res: list[int] = []

    def dfs(node: Optional[TreeNode]) -> None:
        if node is None:
            return
        # 访问优先级：根节点 -> 左子树 -> 右子树
        res.append(node.val)
        dfs(node.left)
        dfs(node.right)

    dfs(root)
    return res


def in_order(root: Optional[TreeNode]) -> list[int]:
    """中序遍历"""
    res: list[int] = []

    def dfs(node: Optional[TreeNode]) -> None:
        if node is None:
            return
        # 访问优先级：左子树 -> 根节点 -> 右子树
        dfs(node.left)
        res.append(node.val)
        dfs(node.right)

    dfs(root)
    return res


def post_order(root: Optional[TreeNode]) -> list[int]:
    """后序遍历"""
    res: list[int] = []

    def dfs(node: Optional[TreeNode]) -> None:
        if node is None:
            return
        # 访问优先级：左子树 -> 右子树 -> 根节点
        dfs(node.left)
        dfs(node.right)
        res.append(node.val)

    dfs(root)
    return res