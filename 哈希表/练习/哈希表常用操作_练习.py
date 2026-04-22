"""哈希表常用操作练习。

目标：熟悉增删改查与遍历。
要求：自行补全函数体，不要直接在全局脚本中写逻辑。
"""


def query_name(hmap: dict[int, str], key: int) -> str:
    """按 key 查询 value。"""
    # 步骤提示：
    # 1) 处理 key 不存在的情况
    # 2) 返回查询结果
    if key not in hmap:
        raise KeyError(f"Key {key} not found")
    return hmap[key]
    


def remove_key(hmap: dict[int, str], key: int) -> None:
    """删除指定 key。"""
    # 步骤提示：
    # 1) 判断 key 是否存在
    # 2) 删除 key
    if key in hmap:
        del hmap[key]

    


def iterate_items(hmap: dict[int, str]) -> list[str]:
    """遍历键值对并返回格式化后的字符串列表。"""
    # 步骤提示：
    # 1) 遍历 hmap.items()
    # 2) 按 "key -> value" 格式拼接
    # 3) 收集并返回
    res: list[str] = []
    for key, val in hmap.items():
        # res.append(str(key)+" -> "+str(val))
        # 正确, 但是下面更好
        res.append(f"{key} -> {val}")
    return res
    


def iterate_keys(hmap: dict[int, str]) -> list[int]:
    """遍历并返回全部 key。"""
    # 可以直接 return list(hmap.keys())
    res: list[int] = []
    for key in hmap.keys():
        res.append(key)
    return res


def iterate_values(hmap: dict[int, str]) -> list[str]:
    """遍历并返回全部 value。"""
    res: list[str] = []
    for val in hmap.values():
        res.append(val)
    return res
    
