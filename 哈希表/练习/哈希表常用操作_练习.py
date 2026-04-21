"""哈希表常用操作练习。

目标：熟悉增删改查与遍历。
要求：自行补全函数体，不要直接在全局脚本中写逻辑。
"""


def build_hash_map() -> dict[int, str]:
    """初始化并返回哈希表。"""
    # 步骤提示：
    # 1) 创建空字典
    # 2) 按给定键值对依次插入
    # 3) 返回字典
    raise NotImplementedError("TODO: 实现 build_hash_map")


def query_name(hmap: dict[int, str], key: int) -> str:
    """按 key 查询 value。"""
    # 步骤提示：
    # 1) 处理 key 不存在的情况
    # 2) 返回查询结果
    raise NotImplementedError("TODO: 实现 query_name")


def remove_key(hmap: dict[int, str], key: int) -> None:
    """删除指定 key。"""
    # 步骤提示：
    # 1) 判断 key 是否存在
    # 2) 删除 key
    raise NotImplementedError("TODO: 实现 remove_key")


def iterate_items(hmap: dict[int, str]) -> list[str]:
    """遍历键值对并返回格式化后的字符串列表。"""
    # 步骤提示：
    # 1) 遍历 hmap.items()
    # 2) 按 "key -> value" 格式拼接
    # 3) 收集并返回
    raise NotImplementedError("TODO: 实现 iterate_items")


def iterate_keys(hmap: dict[int, str]) -> list[int]:
    """遍历并返回全部 key。"""
    raise NotImplementedError("TODO: 实现 iterate_keys")


def iterate_values(hmap: dict[int, str]) -> list[str]:
    """遍历并返回全部 value。"""
    raise NotImplementedError("TODO: 实现 iterate_values")
