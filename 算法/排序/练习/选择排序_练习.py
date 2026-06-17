"""选择排序练习版 - 每轮选出最小元素。

核心思想：
每轮从未排序区间中选择最小的元素，
与未排序区间的第一个元素交换位置。

特点：
- 交换次数最少（最多 n-1 次）
- 无论什么情况都是 O(n²)
- 不稳定排序

时间复杂度：O(n²)
空间复杂度：O(1)
稳定性：不稳定排序
"""


def selection_sort(nums: list[int]) -> None:
    """选择排序实现。

    算法步骤：
    1. 外循环控制当前要确定的位置 i
    2. 假设当前位置 i 就是最小值，记录索引 k=i
    3. 内循环在 [i+1, n-1] 中寻找更小的元素
    4. 如果找到更小的，更新 k
    5. 循环结束后，交换 nums[i] 和 nums[k]

    参数：
        nums: 待排序列表（原地修改）
    """
    n = len(nums)

    # 步骤 1：外循环 - 确定每个位置
    for i in range(n - 1):
        k = i

        # 步骤 2：内循环 - 寻找最小元素的索引
        for j in range(i + 1, n):
            if nums[j] < nums[k]:
                k = j

        # 步骤 3：交换最小元素到位置 i
        # TODO: nums[i], nums[k] = nums[k], nums[i]
        nums[i], nums[k] = nums[k], nums[i]


if __name__ == "__main__":
    test_cases = [
        [4, 1, 3, 1, 5, 2],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
    ]

    print("=" * 60)
    print("选择排序测试")
    print("=" * 60)

    for arr in test_cases:
        original = arr.copy()
        selection_sort(arr)
        print(f"✅ {original} → {arr}")

    print("\n💡 关键要点：")
    print("- 每轮只交换一次（找最小值）")
    print("- 时间复杂度恒定 O(n²)")
    print("- 不稳定排序（可能改变相同元素的相对顺序）")