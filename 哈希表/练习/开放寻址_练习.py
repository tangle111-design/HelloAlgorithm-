"""开放寻址哈希表练习（线性探测 + 墓碑删除）。"""

from dataclasses import dataclass


@dataclass
class Pair:
    key: int
    val: str


class HashMapOpenAddressing:
    """开放寻址哈希表。"""

    def __init__(self) -> None:
        self.size = 0
        self.capacity = 4
        self.load_thres = 2.0 / 3.0
        self.extend_ratio = 2
        self.buckets: list[Pair | None] = [None] * self.capacity
        self.TOMBSTONE = Pair(-1, "-1")

    def hash_func(self, key: int) -> int:
        raise NotImplementedError("TODO: 实现 hash_func")

    def load_factor(self) -> float:
        raise NotImplementedError("TODO: 实现 load_factor")

    def find_bucket(self, key: int) -> int:
        # 步骤提示：
        # 1) 从 hash 索引开始线性探测
        # 2) 记录第一个墓碑位置 first_tombstone
        # 3) 若找到 key，必要时前移到 first_tombstone
        # 4) 遇到空桶停止；返回空桶或 first_tombstone
        raise NotImplementedError("TODO: 实现 find_bucket")

    def get(self, key: int) -> str | None:
        # 步骤提示：
        # 1) 先用 find_bucket 定位
        # 2) 判断该桶是有效元素还是空/墓碑
        raise NotImplementedError("TODO: 实现 get")

    def put(self, key: int, val: str) -> None:
        # 步骤提示：
        # 1) 先判断是否需要扩容
        # 2) 定位桶位
        # 3) 若 key 已存在则更新
        # 4) 若不存在则插入并 size += 1
        raise NotImplementedError("TODO: 实现 put")

    def remove(self, key: int) -> None:
        # 步骤提示：
        # 1) 定位 key
        # 2) 若存在则标记为 TOMBSTONE
        # 3) 维护 size
        raise NotImplementedError("TODO: 实现 remove")

    def extend(self) -> None:
        # 步骤提示：
        # 1) 暂存旧 buckets
        # 2) 扩容并初始化新数组
        # 3) size 归零
        # 4) 重新插入旧元素（跳过 None 和 TOMBSTONE）
        raise NotImplementedError("TODO: 实现 extend")

    def print_map(self) -> None:
        # 步骤提示：
        # 1) 逐桶打印
        # 2) 区分 None / TOMBSTONE / 有效 Pair
        raise NotImplementedError("TODO: 实现 print_map")
