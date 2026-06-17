"""构建二叉树练习版：从前序和中序遍历重建二叉树。


问题描述：
给定二叉树的前序遍历和中序遍历结果，
重建该二叉树并返回根节点。

遍历顺序说明：
前序遍历：根 → 左 → 右
中序遍历：左 → 根 → 右

示例：
前序: [3, 9, 20, 15, 7]
中序: [9, 3, 15, 20, 7]

构建过程：
1. 前序第一个是 3 → 根节点是 3
2. 在中序找到 3 的位置（索引1）
3. 中序左边 [9] 是左子树，右边 [15,20,7] 是右子树
4. 递归构建左右子树

结果树结构：
      3
     / \\
    9   20
       / \\
      15  7
"""

class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None


def build_tree(preorder: list[int], inorder: list[int]) -> TreeNode | None:
    """根据遍历序列构建二叉树。

    参数：
        preorder: 前序遍历列表
        inorder: 中序遍历列表

    返回：
        根节点
    """
    # 步骤 1：建立中序遍历的值→索引映射
    # TODO: 创建字典 inorder_map = {val: idx for idx, val in enumerate(inorder)}
    inorder_map = {val: idx for idx, val in enumerate(inorder)}

    # 步骤 2：定义递归函数
    def dfs(pre_idx: int, in_left: int, in_right: int) -> TreeNode | None:
        """递归构建子树。

        参数：
            pre_idx: 当前根节点在前序中的位置
            in_left: 当前子树在中序中的左边界
            in_right: 当前子树在中序中的右边界
        """
        # 步骤 3：检查边界条件
        # TODO: 若 in_left > in_right，返回 None（空区间）
        if in_left > in_right:
            return None

        # 步骤 4：创建当前根节点
        # TODO: root = TreeNode(preorder[pre_idx])
        root = TreeNode(preorder[pre_idx])

        # 步骤 5：在中序中找到根节点的位置
        # TODO: m = inorder_map[root.val]
        m = inorder_map[root.val]

        # 步骤 6：递归构建左子树
        # TODO: root.left = dfs(pre_idx+1, in_left, m-1)
        root.left = dfs(pre_idx + 1, in_left, m - 1)

        # 步骤 7：递归构建右子树
        # TODO: pre_idx + (m - in_left) + 1 计算右子树根节点在前序中的位置
        root.right = dfs(pre_idx + 1 + m - in_left, m + 1, in_right)

        return root

    # 步骤 8：启动递归
    # TODO: 返回 dfs(0, 0, len(inorder)-1)
    return dfs(0, 0, len(inorder) - 1)


if __name__ == "__main__":
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]

    print("=" * 60)
    print("构建二叉树测试")
    print("=" * 60)

    print(f"\n前序遍历: {preorder}")
    print(f"中序遍历: {inorder}")

    root = build_tree(preorder, inorder)

    if root:
        print(f"\n✅ 构建成功!")
        print(f"根节点: {root.val}")
        if root.left:
            print(f"左子树根: {root.left.val}")
        if root.right:
            print(f"右子树根: {root.right.val}")

    print("\n💡 关键要点：")
    print("- 前序确定根节点位置")
    print("- 中序划分左右子树范围")
    print("- 使用哈希表加速查找（O(1)）")