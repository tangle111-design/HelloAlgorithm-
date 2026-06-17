# 二叉树的数组表示
# 使用 None 来表示空位
tree = [1, 2, 3, 4, None, 6, 7, 8, 9, None, None, 12, None, None, 15]


class ArrayBinaryTree:
    """数组表示下的二叉树类"""

    def __init__(self, arr: list[int | None]):
        """构造方法"""
        self._tree = list(arr)
        self.res: list[int] = []

    def size(self):
        """列表容量"""
        return len(self._tree)

    def val(self, i: int) -> int | None:
        """获取索引为 i 节点的值"""
        # 若索引越界，则返回 None ，代表空位
        if i < 0 or i >= self.size():
            return None
        return self._tree[i]

    def left(self, i: int) -> int | None:
        """获取索引为 i 节点的左子节点的索引"""
        return 2 * i + 1

    def right(self, i: int) -> int | None:
        """获取索引为 i 节点的右子节点的索引"""
        return 2 * i + 2

    def parent(self, i: int) -> int | None:
        """获取索引为 i 节点的父节点的索引"""
        return (i - 1) // 2

    def level_order(self) -> list[int]:
        """层序遍历"""
        self.res = []
        # 直接遍历数组
        for i in range(self.size()):
            if self.val(i) is not None:
                self.res.append(self.val(i))
        return self.res

    def dfs(self, i: int, order: str):
        """递归遍历

        这个函数的巧妙之处在于通过单个递归函数和条件判断，统一实现了三种不同的遍历方式。

        前序遍历：根节点 -> 左子树 -> 右子树
        中序遍历：左子树 -> 根节点 -> 右子树
        后序遍历：左子树 -> 右子树 -> 根节点

                    1
                   / \
                  2   3
                 / \
                4   5
        前序遍历： 1, 2, 4, 5, 3
        中序遍历： 4, 2, 5, 1, 3
        后序遍历： 4, 5, 2, 3, 1
        """
        # 基本情况：如果当前节点为空，则直接返回，结束递归
        if self.val(i) is None:
            return

        # 前序遍历：在递归访问左右子树之前访问当前节点
        if order == "pre":
            self.res.append(self.val(i))

        # 递归遍历左子树
        self.dfs(self.left(i), order)

        # 中序遍历：在递归访问左子树之后、右子树之前访问当前节点
        if order == "in":
            self.res.append(self.val(i))

        # 递归遍历右子树
        self.dfs(self.right(i), order)

        # 后序遍历：在递归访问左右子树之后访问当前节点
        if order == "post":
            self.res.append(self.val(i))

    def pre_order(self) -> list[int]:
        """前序遍历"""
        self.res = []
        self.dfs(0, order="pre")
        return self.res

    def in_order(self) -> list[int]:
        """中序遍历"""
        self.res = []
        self.dfs(0, order="in")
        return self.res

    def post_order(self) -> list[int]:
        """后序遍历"""
        self.res = []
        self.dfs(0, order="post")
        return self.res