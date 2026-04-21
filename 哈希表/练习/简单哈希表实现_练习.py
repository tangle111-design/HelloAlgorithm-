"""数组实现哈希表练习。"""

from dataclasses import dataclass


@dataclass
class Pair:
    """键值对。"""

    key: int
    val: str


class ArrayHashMap:
    """基于数组实现的哈希表（不处理冲突）。"""

    def __init__(self) -> None:
        self.buckets: list[Pair | None] = [None] * 100

    def hash_func(self, key: int) -> int:
        # 步骤提示：
        # 1) 使用固定容量
        # 2) 通过取模得到桶索引
        raise NotImplementedError("TODO: 实现 hash_func")

    def get(self, key: int) -> str | None:
        # 步骤提示：
        # 1) 先算索引
        # 2) 取出桶中元素
        # 3) 判断为空与非空两种情况
        raise NotImplementedError("TODO: 实现 get")

    def put(self, key: int, val: str) -> None:
        # 步骤提示：
        # 1) 先构造 Pair
        # 2) 根据索引覆盖桶位
        raise NotImplementedError("TODO: 实现 put")

    def remove(self, key: int) -> None:
        # 步骤提示：
        # 1) 找到索引
        # 2) 将该位置设为 None
        raise NotImplementedError("TODO: 实现 remove")

    def entry_set(self) -> list[Pair]:
        # 步骤提示：
        # 1) 遍历 buckets
        # 2) 跳过 None
        # 3) 收集 Pair
        raise NotImplementedError("TODO: 实现 entry_set")

    def key_set(self) -> list[int]:
        # 步骤提示：
        # 1) 遍历 buckets
        # 2) 仅收集非空 pair.key
        raise NotImplementedError("TODO: 实现 key_set")

    def value_set(self) -> list[str]:
        # 步骤提示：
        # 1) 遍历 buckets
        # 2) 仅收集非空 pair.val
        raise NotImplementedError("TODO: 实现 value_set")

    def print_map(self) -> None:
        # 步骤提示：
        # 1) 遍历 buckets
        # 2) 输出 "key -> value" 形式
        raise NotImplementedError("TODO: 实现 print_map")
