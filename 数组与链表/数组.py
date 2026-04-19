def insert(nums: list[int], num: int, index: int):
    """在数组的索引 index 处插入元素 num"""
    # 要求：
    # 1) 在索引 index 位置插入元素 num。
    # 2) 将 index 及其后的元素整体向后移动一位。
    # 3) 原地修改 nums，不返回新数组。

    # for i in range(len(nums)-1, index, -1):
    #   nums[i + 1] = nums[i]
    """注意上面代码循环的结尾是index+1"""
    for i in range(len(nums)-1, index, -1):
        nums[i] = nums[i-1]
    nums[index] = num

def remove(nums: list[int], index: int):
    """删除索引 index 处的元素"""
    # 要求：
    # 1) 删除索引 index 处的元素。
    # 2) 将 index 之后的元素整体向前移动一位。
    # 3) 原地修改 nums。
    for i in range(index, len(nums)-1):
        nums[i] = nums[i+1]

def extend(nums: list[int], enlarge: int) -> list[int]:
    """扩展数组长度"""
    # 要求：
    # 1) 新建长度为 len(nums) + enlarge 的数组。
    # 2) 将 nums 中元素按原顺序复制到新数组前半部分。
    # 3) 返回扩展后的新数组。
    new_nums = [0] * (len(nums) + enlarge)
    for i in range(len(nums)):
        new_nums[i] = nums[i]
    return new_nums



# =========================
# 参考答案（放在最下面）
# =========================
def insert_answer(nums: list[int], num: int, index: int):
    """参考答案：在数组的索引 index 处插入元素 num"""
    for i in range(len(nums) - 1, index, -1):
        nums[i] = nums[i - 1]
    nums[index] = num


def remove_answer(nums: list[int], index: int):
    """参考答案：删除索引 index 处的元素"""
    for i in range(index, len(nums) - 1):
        nums[i] = nums[i + 1]


def extend_answer(nums: list[int], enlarge: int) -> list[int]:
    """参考答案：扩展数组长度"""
    res = [0] * (len(nums) + enlarge)
    for i in range(len(nums)):
        res[i] = nums[i]
    return res

