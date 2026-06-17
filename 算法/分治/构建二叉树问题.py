"""构建二叉树问题（LeetCode 105）。

问题描述：
给定二叉树的**前序遍历**和**中序遍历**结果，
重建该二叉树并返回根节点。
假设树中没有重复的节点值。

前序遍历顺序：[根节点] [左子树] [右子树]
中序遍历顺序：[左子树] [根节点] [右子树]

分治策略：
1. 前序遍历的第一个元素是根节点
2. 在中序遍历中找到根节点的位置
3. 根据该位置划分左右子树的范围
4. 递归构建左右子树

时间复杂度：O(n)
空间复杂度：O(n)
"""


class TreeNode:
    """二叉树节点定义。"""

    def __init__(self, val: int):
        self.val = val
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None


def dfs(
    preorder: list[int],
    inorder_map: dict[int, int],
    i: int,
    l: int,
    r: int,
) -> TreeNode | None:
    """分治构建二叉树。

    参数说明：
        preorder: 前序遍历序列
        inorder_map: 中序遍历的值→索引映射（用于快速查找）
        i: 当前在前序序列中的位置（要处理的根节点）
        l: 当前子树在中序序列中的左边界
        r: 当前子树在中序序列中的右边界

    返回：
        构建好的子树根节点
    """
    if r - l < 0:
        return None

    root = TreeNode(preorder[i])
    m = inorder_map[preorder[i]]

    root.left = dfs(preorder, inorder_map, i + 1, l, m - 1)
    root.right = dfs(preorder, inorder_map, i + 1 + m - l, m + 1, r)

    return root


def build_tree(preorder: list[int], inorder: list[int]) -> TreeNode | None:
    """根据前序和中序遍历构建二叉树。

    参数：
        preorder: 前序遍历结果
        inorder: 中序遍历结果

    返回：
        二叉树的根节点
    """
    inorder_map = {val: idx for idx, val in enumerate(inorder)}
    return dfs(preorder, inorder_map, 0, 0, len(inorder) - 1)


if __name__ == "__main__":
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]

    print("构建二叉树测试")
    print("=" * 50)
    print(f"前序遍历: {preorder}")
    print(f"中序遍历: {inorder}")

    root = build_tree(preorder, inorder)
    if root:
        print(f"✅ 构建成功！根节点值: {root.val}")
        if root.left:
            print(f"   左子节点: {root.left.val}")
        if root.right:
            print(f"   右子节点: {root.right.val}")