"""冒泡排序练习版 - 通过相邻元素比较交换实现排序。

核心思想：
每一轮遍历将最大的元素"冒泡"到数组末尾。
就像水中的气泡，大的会浮到水面。

时间复杂度：O(n²)
空间复杂度：O(1)
稳定性：稳定排序
"""


def bubble_sort(nums: list[int]) -> None:
    """基础版冒泡排序。

    算法步骤：
    1. 外循环控制未排序区间的右边界（从 n-1 递减到 1）
    2. 内循环在 [0, i] 区间内两两比较相邻元素
    3. 若前一个 > 后一个，则交换它们
    4. 每轮结束后，最大元素到达位置 i

    参数：
        nums: 待排序列表（原地修改）
    """
    # 步骤 1：获取数组长度
    # TODO: n = len(nums)
    n = len(nums)

    # 步骤 2：外循环 - 控制每轮的右边界
    for i in range(n - 1, 0, -1):
        # TODO: 内循环 - 在 [0, i] 区间内比较
        for j in range(i):
            if nums[j] > nums[j + 1]:
                # 步骤 3：交换相邻元素
                # TODO: nums[j], nums[j+1] = nums[j+1], nums[j]
                nums[j], nums[j + 1] = nums[j + 1], nums[j]


def bubble_sort_optimized(nums: list[int]) -> None:
    """优化版冒泡排序（带提前终止标志）。

    优化思路：
    若某轮没有发生任何交换，说明数组已有序，可提前结束。
    """
    n = len(nums)

    for i in range(n - 1, 0, -1):
        flag = False

        for j in range(i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                flag = True

        if not flag:
            break


if __name__ == "__main__":
    test_cases = [
        [4, 1, 3, 1, 5, 2],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
    ]

    print("=" * 60)
    print("冒泡排序测试")
    print("=" * 60)

    for arr in test_cases:
        original = arr.copy()
        bubble_sort_optimized(arr)
        print(f"✅ {original} → {arr}")

    print("\n💡 关键要点：")
    print("- 每轮确定一个最大值的位置")
    print("- 优化：无交换时提前终止")
    print("- 稳定排序，适合小规模数据")