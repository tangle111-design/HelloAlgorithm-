"""堆排序练习版 - 利用堆数据结构的排序算法。

核心思想：
1. 将数组构建成最大堆（根节点是最大值）
2. 重复将堆顶（最大值）与末尾元素交换
3. 对剩余元素重新堆化
4. 最终得到升序排列的数组

关键操作 - sift_down（向下堆化）：
从节点 i 开始，
将其与子节点中较大的那个交换，
直到满足堆的性质或到达叶节点。

时间复杂度：O(n log n)
空间复杂度：O(1)
稳定性：不稳定排序
"""


def sift_down(nums: list[int], n: int, i: int) -> None:
    """从节点 i 开始向下堆化。

    参数：
        nums: 数组
        n: 堆的长度
        i: 要堆化的节点索引
    """
    while True:
        l = 2 * i + 1   # 左子节点
        r = 2 * i + 2   # 右子节点
        ma = i          # 最大值的节点索引

        # 步骤 1：与左子节点比较
        if l < n and nums[l] > nums[ma]:
            ma = l

        # 步骤 2：与右子节点比较
        if r < n and nums[r] > nums[ma]:
            ma = r

        # 步骤 3：如果 i 已经是最大，结束堆化
        if ma == i:
            break

        # 步骤 4：交换并继续向下
        nums[i], nums[ma] = nums[ma], nums[i]
        i = ma


def heap_sort(nums: list[int]) -> None:
    """堆排序主函数。

    算法步骤：
    1. 建堆：从最后一个非叶节点开始向上堆化
    2. 排序：重复提取最大值到末尾
    """
    # 步骤 1：建堆操作
    # TODO: 从最后一个非叶节点开始（len//2-1），向前遍历到根节点（0）
    for i in range(len(nums) // 2 - 1, -1, -1):
        sift_down(nums, len(nums), i)

    # 步骤 2：提取最大元素
    for i in range(len(nums) - 1, 0, -1):
        # 交换堆顶和末尾元素
        nums[0], nums[i] = nums[i], nums[0]
        # 对剩余部分重新堆化
        sift_down(nums, i, 0)


if __name__ == "__main__":
    test_cases = [
        [4, 1, 3, 1, 5, 2],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
    ]

    print("=" * 60)
    print("堆排序测试")
    print("=" * 60)

    for arr in test_cases:
        original = arr.copy()
        heap_sort(arr)
        print(f"✅ {original} → {arr}")

    print("\n💡 关键要点：")
    print("- 利用完全二叉树的性质")
    print("- 原地排序，空间 O(1)")
    print("- 不稳定排序，但性能稳定")