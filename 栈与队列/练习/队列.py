class ArrayQueue:
    """练习版：基于环形数组实现的队列。

    提示：
    1. 维护底层数组、队首指针和当前长度。
    2. 队尾索引可以通过 (front + size) % capacity 计算。
    3. 注意空队列和满队列的边界处理。
    """
    
    def __init__(self, size: int):
        """初始化练习结构。

        提示：
        1. 分配固定长度数组。
        2. 将队首指针和长度初始化为 0。
        """

    def capacity(self) -> int:
        """获取队列的容量。"""

    def size(self) -> int:
        """获取队列的长度。"""

    def is_empty(self) -> bool:
        """判断队列是否为空。"""

    def push(self, num: int):
        """入队。

        提示：
        1. 先判断是否已满。
        2. 根据 front 和 size 计算队尾位置。
        3. 写入元素后再更新 size。
        """

    def pop(self) -> int:
        """出队。

        提示：
        1. 先访问队首元素。
        2. 再移动队首指针。
        3. 最后减少 size。
        """

    def peek(self) -> int:
        """访问队首元素。

        提示：
        1. 先判断队列是否为空。
        2. 返回 front 位置的元素。
        """

    def to_list(self) -> list[int]:
        """转换为列表，方便打印和调试。

        提示：
        1. 从 front 开始遍历 size 个元素。
        2. 使用取余处理环形数组回绕。
        """