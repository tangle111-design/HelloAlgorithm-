"""字符串哈希函数练习。"""


MODULUS = 1_000_000_007


def add_hash(key: str) -> int:
    """加法哈希。"""
    # 步骤提示：
    # 1) 遍历每个字符
    # 2) 用 ord(c) 累加
    # 3) 最后对 MODULUS 取模
    hash: int = 0
    for c in key:
        hash += ord(c)
    return hash % MODULUS


def mul_hash(key: str) -> int:
    """乘法哈希。"""
    # 步骤提示：
    # 1) 使用 rolling hash 思想
    # 2) 对每个字符做 hash = 31 * hash + ord(c)
    # 3) 返回取模结果
    hash = 1
    for c in key:
        hash = 31 * hash + ord(c)
    return hash % MODULUS



def xor_hash(key: str) -> int:
    """异或哈希。"""
    # 步骤提示：
    # 1) 初始化 hash = 0
    # 2) 遍历字符并与 ord(c) 异或
    # 3) 返回取模结果
    hash = 0
    for c in key:
        hash ^= ord(c)
    return hash % MODULUS


def rot_hash(key: str) -> int:
    """旋转哈希。"""
    # 步骤提示：
    # 1) 每轮先左移再右移混合
    # 2) 与当前字符编码做异或
    # 3) 最后取模
    hash = 0 # 初始值无必须要求
    for c in key:
        hash = (hash << 4) ^ (hash >> 28) ^ ord(c)
    return hash % MODULUS
    
