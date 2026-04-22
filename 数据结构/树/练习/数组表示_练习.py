from __future__ import annotations


class ArrayBinaryTree:
    """数组表示下的二叉树练习。"""

    def __init__(self, arr: list[int | None]):
        self._tree = list(arr)
        self.res: list[int] = []

    def size(self) -> int:
        """数组容量。"""
        return len(self._tree)

    def val(self, i: int) -> int | None:
        """获取索引 i 对应节点值。"""
        # 步骤提示：
        # 1) 先判断 i 是否越界。
        # 2) 越界返回 None；否则返回 _tree[i]。
        if 0 <= i < self.size():
            return self._tree[i]
        return None

    def left(self, i: int) -> int:
        """左子节点索引。"""
        return 2 * i + 1

    def right(self, i: int) -> int:
        """右子节点索引。"""
        return 2 * i + 2

    def parent(self, i: int) -> int:
        """父节点索引。"""
        return (i - 1) // 2

    def level_order(self) -> list[int]:
        """层序遍历（直接遍历数组）练习。"""
        self.res = []

        # 步骤提示：
        # 1) 从 0 遍历到 size()-1。
        # 2) 跳过值为 None 的位置。
        # 3) 将有效节点值加入 self.res。
        for i in range(0, self.size()):
            # 错误, self.val(i)为0时误判
            # if self.val(i):
            if self.val(i) is not None:
                self.res.append(self.val(i))
        return self.res

    def dfs(self, i: int, order: str) -> None:
        """统一 DFS:支持 pre/in/post 三种顺序。"""
        # 步骤提示：
        # 1) 递归终止：索引位置为空（或越界）直接返回。
        # 2) pre: 先访问当前节点，再左、右。
        # 3) in: 先左，再访问当前节点，再右。
        # 4) post: 先左、右，最后访问当前节点。

        if self.val(i) is None:
            return
        
        if order == "pre":
            self.res.append(self.val(i))

        self.dfs(self.left(i), order)

        if order == "in":
            self.res.append(self.val(i))

        self.dfs(self.right(i), order)

        if order == "post":
            self.res.append(self.val(i))
        

    def pre_order(self) -> list[int]:
        """前序遍历。"""
        # 每次重置, 避免结果相互污染
        self.res = []
        
        # 步骤提示：调用 dfs(0, "pre")
        self.dfs(0, "pre")

        return self.res

    def in_order(self) -> list[int]:
        """中序遍历。"""
        self.res = []

        # 步骤提示：调用 dfs(0, "in")
        self.dfs(0, "in")

        return self.res

    def post_order(self) -> list[int]:
        """后序遍历。"""
        self.res = []

        # 步骤提示：调用 dfs(0, "post")
        self.dfs(0, "post")

        return self.res
