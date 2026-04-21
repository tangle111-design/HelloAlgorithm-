class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def pre_order_iterative(root: TreeNode | None) -> list:
    """
    前序遍历 - 迭代实现
    访问顺序：根节点 -> 左子树 -> 右子树
    
    算法思路：
    1. 使用栈来模拟递归调用过程
    2. 先将根节点压入栈
    3. 循环直到栈为空：
       - 弹出栈顶节点并访问
       - 先将右子节点压栈，再将左子节点压栈
       - 这样保证左子树先于右子树被访问（栈是后进先出）
    """
    # 处理空树情况
    if not root:
        return []
    
    res = []  # 存储遍历结果
    stack = [root]  # 初始化栈，根节点入栈
    
    while stack:
        # 弹出栈顶节点（当前要访问的节点）
        node = stack.pop()
        res.append(node.val)  # 访问当前节点
        
        # 先将右子树压栈，再将左子树压栈
        # 这样出栈时左子树会先于右子树被处理
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    
    return res

def in_order_iterative(root: TreeNode | None) -> list:
    """
    中序遍历 - 迭代实现
    访问顺序：左子树 -> 根节点 -> 右子树
    
    算法思路：
    1. 使用栈和当前节点指针
    2. 从根节点开始，将所有左子节点压入栈
    3. 当没有左子节点时，弹出栈顶节点并访问
    4. 转向该节点的右子树，重复上述过程
    """
    res = []  # 存储遍历结果
    stack = []  # 初始化空栈
    curr = root  # 当前节点指针，从根节点开始
    
    # 当还有节点需要处理或栈不为空时继续循环
    while curr or stack:
        # 遍历到最左边的节点，沿途所有节点压栈
        while curr:
            stack.append(curr)
            curr = curr.left
        
        # 弹出栈顶节点（当前最左边的节点）
        curr = stack.pop()
        res.append(curr.val)  # 访问该节点
        
        # 转向右子树继续处理
        curr = curr.right
    
    return res

def post_order_iterative(root: TreeNode | None) -> list:
    """
    后序遍历 - 迭代实现
    访问顺序：左子树 -> 右子树 -> 根节点
    
    算法思路（方法一：反转前序遍历）：
    1. 使用类似前序遍历的方法，但访问顺序改为：根 -> 右 -> 左
    2. 最后将结果反转，得到正确的后序遍历：左 -> 右 -> 根
    
    这种方法简单易懂，但需要额外的反转操作
    """
    # 处理空树情况
    if not root:
        return []
    
    res = []  # 存储遍历结果
    stack = [root]  # 初始化栈，根节点入栈
    
    while stack:
        # 弹出栈顶节点
        node = stack.pop()
        res.append(node.val)  # 访问当前节点
        
        # 先将左子树压栈，再将右子树压栈
        # 这样出栈时右子树会先于左子树被处理
        # 最终访问顺序是：根 -> 右 -> 左
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    
    # 反转结果，得到正确的后序遍历顺序：左 -> 右 -> 根
    return res[::-1]

def post_order_iterative_alt(root: TreeNode | None) -> list:
    """
    后序遍历 - 迭代实现（方法二：不使用反转）
    
    算法思路：
    1. 使用栈和记录上一个访问的节点
    2. 从根节点开始，沿着左子树一直压栈
    3. 检查栈顶节点：
       - 如果没有右子树或右子树已被访问，则访问该节点
       - 否则转向右子树继续处理
    """
    if not root:
        return []
    
    res = []
    stack = []
    prev = None  # 记录上一个访问的节点
    curr = root
    
    while curr or stack:
        # 遍历到最左边的节点
        while curr:
            stack.append(curr)
            curr = curr.left
        
        # 查看栈顶节点（不弹出）
        curr = stack[-1]
        
        # 如果右子树存在且未被访问，转向右子树
        if curr.right and curr.right != prev:
            curr = curr.right
        else:
            # 访问当前节点
            res.append(curr.val)
            stack.pop()
            prev = curr
            curr = None  # 设置curr为None，继续处理栈中下一个节点
    
    return res