class ListNode:
    """双向链表节点练习壳。"""

    def __init__(self, val: int):
        """初始化节点。

        提示：
        1. 保存当前值。
        2. 预留 next 和 prev 两个引用。
        """


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

    def size(self) -> int:
        """获取双向队列的长度。"""

    def is_empty(self) -> bool:
        """判断双向队列是否为空。"""

    def push(self, num: int, is_front: bool):
        """统一的入队入口。

        提示：
        1. 先创建新节点。
        2. 处理空队列。
        3. 再分别处理队首插入和队尾插入。
        4. 别忘了更新 size。
        """

    def push_first(self, num: int):
        """队首入队。"""

    def push_last(self, num: int):
        """队尾入队。"""

    def pop(self, is_front: bool) -> int:
        """统一的出队入口。

        提示：
        1. 先判断是否为空。
        2. 再分别处理删除头节点和尾节点。
        3. 处理完要更新 front/rear 和 size。
        """

    def pop_first(self) -> int:
        """队首出队。"""

    def pop_last(self) -> int:
        """队尾出队。"""

    def peek_first(self) -> int:
        """访问队首元素。"""

    def peek_last(self) -> int:
        """访问队尾元素。"""

    def to_array(self) -> list[int]:
        """转换为列表，方便打印和调试。

        提示：
        1. 从 front 开始向后遍历。
        2. 遍历长度以 size 为准。
        """