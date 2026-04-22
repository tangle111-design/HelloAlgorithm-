def add_hash(key: str) -> int:
    """加法哈希"""
    hash = 0
    modulus = 1000000007
    for c in key:
        hash += ord(c)
    return hash % modulus
'''  ocr()函数：
功能	将单个字符转换为其对应的 Unicode 码位（整数）。
参数	一个长度为1的字符串（单个字符）。
返回值	一个整数。
反函数	chr()，将 Unicode 码位（整数）转换回对应的字符。
'''

def mul_hash(key: str) -> int:
    """乘法哈希"""
    hash = 0
    modulus = 1000000007
    for c in key:
        hash = 31 * hash + ord(c) # 31 是一个经验选择的质数
    return hash % modulus

def xor_hash(key: str) -> int:
    """异或哈希"""
    hash = 0
    modulus = 1000000007
    for c in key:
        hash ^= ord(c)
    return hash % modulus

def rot_hash(key: str) -> int:
    """旋转哈希"""
    ''' 分布非常均匀
		对字符顺序高度敏感
		结合了移位操作的扩散特性
	'''
    hash = 0
    modulus = 1000000007
    for c in key:
        hash = (hash << 4) ^ (hash >> 28) ^ ord(c)
    return hash % modulus