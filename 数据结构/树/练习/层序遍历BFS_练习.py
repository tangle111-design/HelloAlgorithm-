from __future__ import annotations

from collections import deque


class TreeNode:
    """二叉树节点。"""

    def __init__(self, val: int, left: TreeNode | None = None, right: TreeNode | None = None):
        self.val = val
        self.left = left
        self.right = right


def level_order(root: TreeNode | None) -> list[int]:
    """层序遍历BFS练习。"""
    if root is None:
        return []

    queue: deque[TreeNode] = deque([root])
    res: list[int] = []

    # 步骤提示：
    # 1) 循环直到队列为空。
    # 2) 每轮先从队首弹出一个节点。
    # 3) 记录该节点值到 res。
    # 4) 若左子节点存在则入队。
    # 5) 若右子节点存在则入队。
    while queue:
        node = queue.popleft()
        res.append(node.val)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return res
