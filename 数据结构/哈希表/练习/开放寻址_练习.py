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
        return key % self.capacity

    def load_factor(self) -> float:
        return self.size / self.capacity

    def find_bucket(self, key: int) -> int:
        # 步骤提示：
        # 1) 从 hash 索引开始线性探测
        # 2) 记录第一个墓碑位置 first_tombstone
        # 3) 若找到 key，必要时前移到 first_tombstone
        # 4) 遇到空桶停止；返回空桶或 first_tombstone
        index = self.hash_func(key)
        first_tombstone = -1 # 全局变量
        while self.buckets[index]:
            if self.buckets[index] == self.TOMBSTONE and first_tombstone == -1:
                first_tombstone = index
            if self.buckets[index].key == key:
                if first_tombstone != -1:
                    self.buckets[first_tombstone] = self.buckets[index]
                    self.buckets[index] = self.TOMBSTONE
                    return first_tombstone # 返回移动后的桶索引
                return index
            # 计算桶索引，越过尾部则返回头部
            index = (index + 1) % self.capacity
        # 如果查找过程中没有找到 key，那么我们会返回一个空桶的索引
        #（如果遇到墓碑标记，则返回第一个墓碑标记的索引，这样可以复用这个墓碑标记的位置）
        return first_tombstone if first_tombstone != -1 else index
    
                



        

    def get(self, key: int) -> str | None:
        # 步骤提示：
        # 1) 先用 find_bucket 定位
        # 2) 判断该桶是有效元素还是空/墓碑
        res_index = self.find_bucket(key)
        # return self.buckets[res_index].val if self.buckets[res_index] and self.buckets[res_index].key != -1 else None
        # 更简洁的写法
        return self.buckets[res_index].val if self.buckets[res_index] not in [None, self.TOMBSTONE] else None
        

    def put(self, key: int, val: str) -> None:
        # 步骤提示：
        # 1) 先判断是否需要扩容
        # 2) 定位桶位
        # 3) 若 key 已存在则更新
        # 4) 若不存在则插入并 size += 1
        if self.load_factor() >= self.load_thres:
            self.extend()
        index = self.find_bucket(key)
        # if self.buckets[index] and self.buckets[index].key != -1:
        if self.buckets[index] not in [None, self.TOMBSTONE]: # 更简洁
            self.buckets[index].val = val
            return
        else:
            # new_pair = Pair(key, val)
            # self.buckets[index] = new_pair
            # 更简洁
            self.buckets[index] = Pair(key, val)

            self.size += 1
            return
        
        
        

    def remove(self, key: int) -> None:
        # 步骤提示：
        # 1) 定位 key
        # 2) 若存在则标记为 TOMBSTONE
        # 3) 维护 size
        index =  self.find_bucket(key)
        if self.buckets[index] not in [None, self.TOMBSTONE]:
            self.buckets[index] = self.TOMBSTONE
            self.size -= 1
        return
        

    def extend(self) -> None:
        # 步骤提示：
        # 1) 暂存旧 buckets
        # 2) 扩容并初始化新数组
        # 3) size 归零
        # 4) 重新插入旧元素（跳过 None 和 TOMBSTONE）
        old_buckets: list[Pair | None] = self.buckets
        self.capacity = self.capacity * self.extend_ratio
        self.buckets: list[Pair | None] = [None] * self.capacity
        self.size = 0
        for old_pair in old_buckets:
            if old_pair not in [None, self.TOMBSTONE]:
                self.put(old_pair.key, old_pair.val)
            
            
        

    def print_map(self) -> None:
        # 步骤提示：
        # 1) 逐桶打印
        # 2) 区分 None / TOMBSTONE / 有效 Pair
        for pair in self.buckets:
            if not pair:
                print("None")
            elif pair is self.TOMBSTONE:
                print("TOMBSTONE")
            else:
                print(f"{pair.key} -> {pair.val}")
        
