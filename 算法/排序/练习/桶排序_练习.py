"""桶排序练习版 - 适用于均匀分布的数据。

核心思想：
将数据分到有限数量的桶里，
每个桶分别排序（可使用其他排序算法），
最后按顺序合并所有桶。

适用场景：
- 数据分布均匀
- 数据范围已知（如 [0, 1) 区间的浮点数）

时间复杂度：O(n + k)
空间复杂度：O(n + k)
稳定性：取决于桶内使用的排序算法
"""


def bucket_sort(nums: list[float]) -> None:
    """桶排序实现（适用于 [0, 1) 区间的浮点数）。

    算法步骤：
    1. 初始化 k 个空桶（k = n/2）
    2. 将每个元素根据值映射到对应的桶
       映射公式：index = int(num * k)
    3. 对每个桶内部进行排序（可使用任何排序算法）
    4. 按顺序遍历所有桶，合并结果

    参数：
        nums: 待排序的浮点数列表（原地修改）
    """
    # 步骤 1：初始化桶
    # TODO: k = len(nums) // 2, 创建 k 个空桶
    k = len(nums) // 2
    buckets = [[] for _ in range(k)]

    # 步骤 2：分配元素到各桶
    for num in nums:
        i = int(num * k)
        buckets[i].append(num)

    # 步骤 3：对每个桶进行排序
    for bucket in buckets:
        bucket.sort()

    # 步骤 4：合并结果
    idx = 0
    for bucket in buckets:
        for num in bucket:
            nums[idx] = num
            idx += 1


if __name__ == "__main__":
    test_data = [0.49, 0.96, 0.82, 0.89, 0.17, 0.36, 0.68, 0.54]

    print("=" * 60)
    print("桶排序测试")
    print("=" * 60)

    print(f"原始数据: {test_data}")
    bucket_sort(test_data)
    print(f"✅ 排序结果: {test_data}")

    print("\n💡 关键要点：")
    print("- 数据均匀分布时效率很高")
    print("- 桶的数量影响性能")
    print("- 适合范围已知的浮点数")