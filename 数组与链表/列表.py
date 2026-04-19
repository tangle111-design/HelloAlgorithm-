# 初始化列表
# 无初始值
nums1: list[int] = []
# 有初始值
nums: list[int] = [1, 3, 2, 5, 4]

# 访问元素
num: int = nums[1]  # 访问索引 1 处的元素

# 更新元素
nums[1] = 0    # 将索引 1 处的元素更新为 0

# 清空列表
nums.clear()

# 在尾部添加元素
nums.append(1)
nums.append(3)
nums.append(2)
nums.append(5)
nums.append(4)

# 在中间插入元素
nums.insert(3, 6)  # 在索引 3 处插入数字 6

# 删除元素
nums.pop(3)        # 删除索引 3 处的元素



class MyList:
    """列表类"""

    def __init__(self):
        """构造方法"""
        self._capacity: int = 10  # 列表容量
        self._arr: list[int] = [0] * self._capacity  # 数组（存储列表元素）
        self._size: int = 0  # 列表长度（当前元素数量）
        self._extend_ratio: int = 2  # 每次列表扩容的倍数

    def size(self) -> int:
        """获取列表长度（当前元素数量）"""
        # 要求：返回当前有效元素数量。
        pass

    def capacity(self) -> int:
        """获取列表容量"""
        # 要求：返回底层数组容量。
        pass

    def get(self, index: int) -> int:
        """访问元素"""
        # 要求：
        # 1) 检查索引是否越界，越界时抛出 IndexError。
        # 2) 返回 index 位置的元素值。
        pass

    def set(self, num: int, index: int):
        """更新元素"""
        # 要求：
        # 1) 检查索引是否越界，越界时抛出 IndexError。
        # 2) 将 index 位置更新为 num。
        pass

    def add(self, num: int):
        """在尾部添加元素"""
        # 要求：
        # 1) 若容量不足，先扩容。
        # 2) 在尾部写入 num。
        # 3) 更新有效元素数量。
        pass

    def insert(self, num: int, index: int):
        """在中间插入元素"""
        # 要求：
        # 1) 检查 index 合法性（按当前实现规则）。
        # 2) 必要时先扩容。
        # 3) 将 index 及其后元素整体后移一位。
        # 4) 在 index 处写入 num，并更新有效元素数量。
        pass

    def remove(self, index: int) -> int:
        """删除元素"""
        # 要求：
        # 1) 检查索引是否越界，越界时抛出 IndexError。
        # 2) 记录被删除元素。
        # 3) 将 index 之后元素整体前移一位。
        # 4) 更新有效元素数量并返回被删除元素。
        pass

    def extend_capacity(self):
        """列表扩容"""
        # 要求：
        # 1) 按 _extend_ratio 对底层数组扩容。
        # 2) 保留原有元素顺序与内容。
        # 3) 更新 _capacity。
        pass

    def to_array(self) -> list[int]:
        """返回有效长度的列表"""
        # 要求：仅返回有效长度范围内的元素切片。
        pass


# =========================
# 参考答案（放在最下面）
# =========================
class MyListAnswer:
    """参考答案：列表类"""

    def __init__(self):
        self._capacity: int = 10
        self._arr: list[int] = [0] * self._capacity
        self._size: int = 0
        self._extend_ratio: int = 2

    def size(self) -> int:
        return self._size

    def capacity(self) -> int:
        return self._capacity

    def get(self, index: int) -> int:
        if index < 0 or index >= self._size:
            raise IndexError("索引越界")
        return self._arr[index]

    def set(self, num: int, index: int):
        if index < 0 or index >= self._size:
            raise IndexError("索引越界")
        self._arr[index] = num

    def add(self, num: int):
        if self.size() == self.capacity():
            self.extend_capacity()
        self._arr[self._size] = num
        self._size += 1

    def insert(self, num: int, index: int):
        if index < 0 or index >= self._size:
            raise IndexError("索引越界")
        if self._size == self.capacity():
            self.extend_capacity()
        for j in range(self._size - 1, index - 1, -1):
            self._arr[j + 1] = self._arr[j]
        self._arr[index] = num
        self._size += 1

    def remove(self, index: int) -> int:
        if index < 0 or index >= self._size:
            raise IndexError("索引越界")
        num = self._arr[index]
        for j in range(index, self._size - 1):
            self._arr[j] = self._arr[j + 1]
        self._size -= 1
        return num

    def extend_capacity(self):
        self._arr = self._arr + [0] * self.capacity() * (self._extend_ratio - 1)
        self._capacity = len(self._arr)

    def to_array(self) -> list[int]:
        return self._arr[: self._size]