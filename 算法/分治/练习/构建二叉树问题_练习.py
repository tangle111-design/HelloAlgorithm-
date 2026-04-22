class TreeNode:
    """二叉树节点"""

    def __init__(self, val: int, left: "TreeNode | None" = None, right: "TreeNode | None" = None):
        self.val = val
        self.left = left
        self.right = right


def dfs(
    preorder: list[int],
    inorder_map: dict[int, int],
    i: int,
    l: int,
    r: int,
) -> TreeNode | None:
    """构建二叉树：求解子树区间 [l, r]"""
    # 步骤 1：处理子树区间为空的情况（递归终止条件）。
    # 步骤 2：用 preorder[i] 创建当前子树根节点。
    # 步骤 3：在 inorder_map 中找到根节点位置 m。
    # 步骤 4：递归构建左子树：
    #   - 左子树根在 preorder 的下一个位置。
    #   - 区间为 [l, m-1]。
    # 步骤 5：递归构建右子树：
    #   - 右子树根索引要跳过左子树节点数。
    #   - 区间为 [m+1, r]。
    # 步骤 6：返回当前根节点。
    """在此处完成代码"""


def build_tree(preorder: list[int], inorder: list[int]) -> TreeNode | None:
    """根据前序和中序遍历构建二叉树"""
    # 步骤 1：构建 inorder 值到索引的映射表，便于 O(1) 查位置。
    # 步骤 2：调用 dfs 构建整棵树（区间 [0, len(inorder)-1]）。
    # 步骤 3：返回根节点。
    """在此处完成代码"""
