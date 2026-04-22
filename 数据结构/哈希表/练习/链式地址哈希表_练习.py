"""链式地址哈希表练习。"""

from dataclasses import dataclass


@dataclass
class Pair:
    key: int
    val: str


class HashMapChaining:
    """链式地址哈希表。"""

    def __init__(self) -> None:
        self.size = 0  # 键值对数量
        self.capacity = 4  # 哈希表容量
        self.load_thres = 2.0 / 3.0  # 触发扩容的负载因子阈值
        self.extend_ratio = 2  # 扩容倍数
        self.buckets = [[] for _ in range(self.capacity)]  # 桶数组

    def hash_func(self, key: int) -> int:
        return key % self.capacity

    def load_factor(self) -> float:
        return self.size / self.capacity
        

    def get(self, key: int) -> str | None:
        # 步骤提示：
        # 1) 定位桶
        # 2) 遍历链表（这里用 list 模拟）
        # 3) 命中 key 返回 val，否则返回 None
        buck = self.buckets[self.hash_func(key)]
        for i in range(len(buck)):
            if buck[i].key == key:
                    return buck[i].val
        return None

        # more Pythonic

        # for pair in self.buckets[self.hash_func(key)]:
        # if pair.key == key:
        #     return pair.val
        # return None
        

    def put(self, key: int, val: str) -> None:
        # 步骤提示：
        # 1) 判断是否需要扩容
        # 2) 定位桶后先查重
        # 3) 有 key 则更新
        # 4) 无 key 则追加并维护 size
        if(self.load_factor()>=self.load_thres):
            self.extend()
        buck = self.buckets[self.hash_func(key)]
        for i in range(len(buck)):
                if buck[i].key == key:
                    buck[i].val = val
                    return None
        buck.append(Pair(key, val))
        self.size += 1
        
                
        

    def remove(self, key: int) -> None:
        # 步骤提示：
        # 1) 定位桶
        # 2) 找到目标 pair 后删除
        # 3) 维护 size
        buck = self.buckets[self.hash_func(key)]
        for i in range(len(buck)):
                if buck[i].key == key:
                    del buck[i]
                    self.size -= 1
                    return

        

    def extend(self) -> None:
        # 步骤提示：
        # 1) 暂存旧 buckets
        # 2) capacity 扩大并重建空桶
        # 3) size 清零
        # 4) 将旧元素重新 put 到新表

        # 若未将 self.size 清零，将导致扩容后 size 异常。
        # 重新 put 旧元素时，put 内部再次递增 size，造成计数错误。
        old_buckets = self.buckets
        self.capacity *= self.extend_ratio
        self.buckets = [[] for _ in range(self.capacity)]
        # here!
        self.size = 0
        for buck in old_buckets:
            for i in range(len(buck)):
                    self.put(buck[i].key, buck[i].val)

        

    def print_map(self) -> None:
        # 步骤提示：
        # 1) 遍历每个桶
        # 2) 将桶内 Pair 转成可读字符串
        for buck in self.buckets:
            for i in range(len(buck)):
                    print(f"{buck[i].key} -> {buck[i].val}")
        
