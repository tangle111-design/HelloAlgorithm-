"""堆排序（Heap Sort）- 利用堆数据结构的排序算法。

核心思想：
1. 将数组构建成最大堆（根节点是最大值）
2. 重复将堆顶（最大值）与末尾元素交换
3. 对剩余元素重新堆化
4. 最终得到升序排列的数组

特点：
- 原地排序，空间复杂度 O(1)
- 不稳定排序
- 时间复杂度稳定 O(n log n)

时间复杂度：O(n log n)
空间复杂度：O(1)
稳定性：不稳定排序
"""


def sift_down(nums: list[int], n: int, i: int) -> None:
    """从节点 i 开始，从顶至底堆化。

    参数：
        nums: 数组
        n: 堆的长度（不是数组长度）
        i: 当前要堆化的节点索引
    """
    while True:
        l = 2 * i + 1   # 左子节点
        r = 2 * i + 2   # 右子节点
        ma = i          # 最大值的节点

        if l < n and nums[l] > nums[ma]:
            ma = l
        if r < n and nums[r] > nums[ma]:
            ma = r

        if ma == i:
            break

        nums[i], nums[ma] = nums[ma], nums[i]
        i = ma


def heap_sort(nums: list[int]) -> None:
    """堆排序主函数。"""
    # 建堆操作：从最后一个非叶节点开始向上堆化
    for i in range(len(nums) // 2 - 1, -1, -1):
        sift_down(nums, len(nums), i)

    # 提取最大元素，循环 n-1 轮
    for i in range(len(nums) - 1, 0, -1):
        nums[0], nums[i] = nums[i], nums[0]
        sift_down(nums, i, 0)


if __name__ == "__main__":
    test_cases = [
        [4, 1, 3, 1, 5, 2],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
    ]

    print("堆排序测试")
    print("=" * 50)

    for arr in test_cases:
        original = arr.copy()
        heap_sort(arr)
        print(f"✅ {original} → {arr}")