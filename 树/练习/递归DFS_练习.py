from __future__ import annotations


class TreeNode:
    """二叉树节点。"""

    def __init__(self, val: int, left: TreeNode | None = None, right: TreeNode | None = None):
        self.val = val
        self.left = left
        self.right = right



def pre_order(root: TreeNode | None) -> list[int]:
    """前序遍历（根-左-右）练习。"""
    
    # 步骤提示：
    # 1) 递归终止条件：节点为空时直接结束当前分支。
    # 2) 先访问当前节点值，再递归左子树，最后递归右子树。
    if root is None:
        return []
    return [root.val] + pre_order(root.left) + pre_order(root.right)

    


def in_order(root: TreeNode | None) -> list[int]:
    """中序遍历（左-根-右）练习。"""
    
    # 步骤提示：
    # 1) 递归先进入左子树。
    # 2) 回到当前节点时记录节点值。
    # 3) 再递归右子树。
    if root is None:
        return []
    return in_order(root.left) + [root.val] + in_order(root.right)
    


def post_order(root: TreeNode | None) -> list[int]:
    """后序遍历（左-右-根）练习。"""
    
    # 步骤提示：
    # 1) 先递归左子树。
    # 2) 再递归右子树。
    # 3) 最后访问当前节点值。
    if root is None:
        return []
    return post_order(root.left) + post_order(root.right) + [root.val]
    
