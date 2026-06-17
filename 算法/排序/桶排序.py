"""桶排序（Bucket Sort）- 适用于均匀分布的数据。

核心思想：
将数据分到有限数量的桶里，
每个桶分别排序（可使用其他排序算法），
最后按顺序合并所有桶。

适用场景：
数据分布均匀，且范围已知（如 [0, 1) 区间的浮点数）

时间复杂度：O(n + k)（k为桶的数量）
空间复杂度：O(n + k)
稳定性：取决于桶内使用的排序算法
"""


def bucket_sort(nums: list[float]) -> None:
    """桶排序实现（适用于 [0, 1) 区间的浮点数）。

    算法步骤：
    1. 初始化 k 个空桶
    2. 将每个元素分配到对应的桶中
    3. 对每个桶内部进行排序
    4. 按顺序合并所有桶的结果

    参数：
        nums: 待排序的浮点数列表（原地修改）
    """
    k = len(nums) // 2
    buckets = [[] for _ in range(k)]

    for num in nums:
        i = int(num * k)
        buckets[i].append(num)

    for bucket in buckets:
        bucket.sort()

    i = 0
    for bucket in buckets:
        for num in bucket:
            nums[i] = num
            i += 1


if __name__ == "__main__":
    test_data = [0.49, 0.96, 0.82, 0.89, 0.17, 0.36, 0.68, 0.54]
    
    print("桶排序测试")
    print("=" * 50)
    print(f"原始数据: {test_data}")
    
    bucket_sort(test_data)
    print(f"✅ 排序结果: {test_data}")