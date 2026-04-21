from __future__ import annotations


class TreeNode:
    """AVL 树节点。"""

    def __init__(self, val: int):
        self.val = val
        self.height = 0
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None


class AVLTree:
    """AVL 树练习。"""

    def __init__(self):
        self._root: TreeNode | None = None

    def height(self, node: TreeNode | None) -> int:
        """获取节点高度。"""
        # 步骤提示：空节点高度为 -1。
        return -1

    def update_height(self, node: TreeNode | None) -> None:
        """更新节点高度。"""
        # 步骤提示：
        # 1) 先取左右子树高度。
        # 2) 当前节点高度 = max(左高, 右高) + 1。

        """请在这里补充高度更新逻辑。"""

    def balance_factor(self, node: TreeNode | None) -> int:
        """获取平衡因子。"""
        # 步骤提示：平衡因子 = 左子树高度 - 右子树高度。
        if node is None:
            return self.height(None) - self.height(None)
        return self.height(node.left) - self.height(node.right)

    def right_rotate(self, node: TreeNode | None) -> TreeNode | None:
        """右旋。"""
        # 步骤提示：
        # 1) 记录 child=node.left 与 grand_child=child.right。
        # 2) 执行旋转重连：child.right=node, node.left=grand_child。
        # 3) 先更新 node 高度，再更新 child 高度。
        # 4) 返回旋转后子树根 child。

        return node

    def left_rotate(self, node: TreeNode | None) -> TreeNode | None:
        """左旋。"""
        # 步骤提示与 right_rotate 镜像对称。

        return node

    def rotate(self, node: TreeNode | None) -> TreeNode | None:
        """根据平衡因子执行 LL/LR/RR/RL 旋转。"""
        # 步骤提示：
        # 1) 先计算当前节点平衡因子 bf。
        # 2) bf > 1: 左偏，区分 LL 与 LR。
        # 3) bf < -1: 右偏，区分 RR 与 RL。
        # 4) 其余情况直接返回 node。

        return node

    def insert(self, val: int) -> None:
        """插入入口。"""
        # 步骤提示：调用递归辅助函数并更新根节点。

        """请在这里补充插入入口逻辑。"""

    def insert_helper(self, node: TreeNode | None, val: int) -> TreeNode:
        """递归插入并回溯平衡。"""
        # 步骤提示：
        # 1) 递归定位插入位置；空节点时创建新节点。
        # 2) 遇到重复值可直接返回原节点。
        # 3) 回溯时先更新高度，再执行 rotate。

        return TreeNode(val)

    def remove(self, val: int) -> None:
        """删除入口。"""
        # 步骤提示：调用递归辅助函数并更新根节点。

        """请在这里补充删除入口逻辑。"""

    def remove_helper(self, node: TreeNode | None, val: int) -> TreeNode | None:
        """递归删除并回溯平衡。"""
        # 步骤提示：
        # 1) 先按 BST 规则查找待删节点。
        # 2) 删除阶段分三类：0 子节点、1 子节点、2 子节点。
        # 3) 两子节点时：找到右子树最小节点（中序后继）替换。
        # 4) 回溯阶段：若当前节点非空，更新高度并执行 rotate。

        return node
