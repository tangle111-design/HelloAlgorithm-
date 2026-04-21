"""链式地址哈希表练习。"""

from dataclasses import dataclass


@dataclass
class Pair:
    key: int
    val: str


class HashMapChaining:
    """链式地址哈希表。"""

    def __init__(self) -> None:
        self.size = 0
        self.capacity = 4
        self.load_thres = 2.0 / 3.0
        self.extend_ratio = 2
        self.buckets: list[list[Pair]] = [[] for _ in range(self.capacity)]

    def hash_func(self, key: int) -> int:
        raise NotImplementedError("TODO: 实现 hash_func")

    def load_factor(self) -> float:
        raise NotImplementedError("TODO: 实现 load_factor")

    def get(self, key: int) -> str | None:
        # 步骤提示：
        # 1) 定位桶
        # 2) 遍历链表（这里用 list 模拟）
        # 3) 命中 key 返回 val，否则返回 None
        raise NotImplementedError("TODO: 实现 get")

    def put(self, key: int, val: str) -> None:
        # 步骤提示：
        # 1) 判断是否需要扩容
        # 2) 定位桶后先查重
        # 3) 有 key 则更新
        # 4) 无 key 则追加并维护 size
        raise NotImplementedError("TODO: 实现 put")

    def remove(self, key: int) -> None:
        # 步骤提示：
        # 1) 定位桶
        # 2) 找到目标 pair 后删除
        # 3) 维护 size
        raise NotImplementedError("TODO: 实现 remove")

    def extend(self) -> None:
        # 步骤提示：
        # 1) 暂存旧 buckets
        # 2) capacity 扩大并重建空桶
        # 3) size 清零
        # 4) 将旧元素重新 put 到新表
        raise NotImplementedError("TODO: 实现 extend")

    def print_map(self) -> None:
        # 步骤提示：
        # 1) 遍历每个桶
        # 2) 将桶内 Pair 转成可读字符串
        raise NotImplementedError("TODO: 实现 print_map")
