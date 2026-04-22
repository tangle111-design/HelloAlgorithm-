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
    while stack:
        node = stack.pop()
        res.append(node.val)
        # 先压右子节点，再压左子节点（保证左先处理）
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

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
    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.left
        
        curr = stack.pop()
        res.append(curr.val)
        # 错误, 若curr最终不能为None, 则外层的while stack or curr:不能进行下一轮
        # if curr.right:
        #     curr = curr.right
        curr = curr.right
        

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
    while stack:
        node = stack.pop()
        res.append(node.val)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

    return res[::-1]


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
    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.left
    
        curr = stack[-1] # 不弹出, 仅查看
        if curr.right and prev != curr.right: # 右子树存在 and 不是从右边回溯上来的
            curr = curr.right
        else:
            curr = stack.pop()
            res.append(curr.val)
            prev = curr # 状态是 正在从右子树回溯
            curr = None # 触发下一轮


    return res
