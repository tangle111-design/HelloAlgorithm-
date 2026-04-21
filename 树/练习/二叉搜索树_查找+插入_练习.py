from __future__ import annotations


class TreeNode:
    """二叉搜索树节点。"""

    def __init__(self, val: int):
        self.val = val
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None


class BinarySearchTree:
    """二叉搜索树：查找 + 插入练习。"""

    def __init__(self):
        self._root: TreeNode | None = None

    def search(self, num: int) -> TreeNode | None:
        """查找节点。"""
        cur = self._root

        # 步骤提示：
        # 1) 从根节点开始循环。
        # 2) 若 num 大于当前值，走右子树。
        # 3) 若 num 小于当前值，走左子树。
        # 4) 相等时返回当前节点；遍历结束返回 None。

        return None

    def insert(self, num: int) -> None:
        """插入节点（不插入重复值）。"""
        # 步骤提示：
        # 1) 若根为空，直接创建根节点。
        # 2) 否则用 cur/pre 双指针向下查找插入位置。
        # 3) 遇到重复值直接结束。
        # 4) 在 pre 的左或右位置接入新节点。

        """请在这里补充迭代插入逻辑。"""
