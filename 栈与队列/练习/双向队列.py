class ListNode:
    """双向链表节点练习壳。"""

    def __init__(self, val: int):
        """初始化节点。

        提示：
        1. 保存当前值。
        2. 预留 next 和 prev 两个引用。
        """
        self.val: int = val
        self.next: ListNode | None = None
        self.prev: ListNode | None = None


class LinkedListDeque:
    """练习版：基于双向链表实现的双向队列。

    提示：
    1. 始终维护 front 和 rear 两个端点。
    2. 空队列、仅一个节点、多节点三种情况都要单独检查。
    3. 头尾插入和删除时，前驱/后继指针要同步更新。
    """

    def __init__(self):
        """初始化双向队列。

        提示：
        1. front 和 rear 都从空开始。
        2. size 初始化为 0。
        """
        self._size: int = 0
        self._front: ListNode | None = None
        self._rear: ListNode | None = None

    def size(self) -> int:
        """获取双向队列的长度。"""
        return self._size

    def is_empty(self) -> bool:
        """判断双向队列是否为空。"""
        return self.size() == 0

    def push(self, num: int, is_front: bool):
        """统一的入队入口。

        提示：
        1. 先创建新节点。
        2. 处理空队列。
        3. 再分别处理队首插入和队尾插入。
        4. 别忘了更新 size。
        """
        newnode: ListNode = ListNode(num)
        if self.is_empty():
            self._front = newnode
            self._rear = newnode
            # 下面是错误的
            # self._front.next = self._rear
            # self._rear.prev = self._front
        else:
            if is_front:
                newnode.next = self._front
                self._front.prev = newnode
                self._front = newnode
            else:
                newnode.prev = self._rear
                self._rear.next = newnode
                self._rear = newnode
        self._size += 1

    def push_first(self, num: int):
        """队首入队。"""
        self.push(num, True)

    def push_last(self, num: int):
        """队尾入队。"""
        self.push(num, False)

    def pop(self, is_front: bool) -> int:
        """统一的出队入口。

        提示：
        1. 先判断是否为空。
        2. 再分别处理删除头节点和尾节点。
        3. 处理完要更新 front/rear 和 size。
        """
        if self.is_empty():
            raise IndexError("empty")
        if is_front:
            res: int = self._front.val
            front_next: ListNode | None = self._front.next
            if front_next != None:
                # 先解掉一条边
                front_next.prev = None
                # 再解掉另一条边
                self._front.next = None
            # 最后修改点
            self._front = front_next
        else:
            res: int = self._rear.val
            rear_prev: ListNode | None = self._rear.prev
            if rear_prev != None:
                rear_prev.next = None
                self._rear.prev = None
            self._rear = rear_prev
        self._size -= 1
        # 重要, 不应遗漏单节点pop情况
        # 否则self._rear/self._front指向已经出队的node
        # 例如is_front == 1时, self._fornt置为None, 然而self._rear仍指向已经出队的单节点
        if self._size == 0:
            self._rear = self._front = None
        return res

    def pop_first(self) -> int:
        """队首出队。"""
        return self.pop(True)

    def pop_last(self) -> int:
        """队尾出队。"""
        return self.pop(False)

    def peek_first(self) -> int:
        """访问队首元素。"""
        if self.is_empty():
            raise IndexError("empty")
        return self._front.val

    def peek_last(self) -> int:
        """访问队尾元素。"""
        if self.is_empty():
            raise IndexError("empty")
        return self._rear.val

    def to_array(self) -> list[int]:
        """转换为列表，方便打印和调试。

        提示：
        1. 从 front 开始向后遍历。
        2. 遍历长度以 size 为准。
        """
        # 错误, 修改了self._front
        # res: list[int] = []
        # for i in range(self.size()):
        #     res.append(self._front.val)
        #     self._front = self._front.next
        # return res

        res: list[int] = []
        go_ahead: ListNode | None = self._front
        for i in range(self.size()):
            res.append(go_ahead.val)
            go_ahead = go_ahead.next
        return res
