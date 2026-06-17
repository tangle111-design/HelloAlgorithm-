"""选择排序（Selection Sort）- 每轮选出最小元素。

核心思想：
每轮从未排序区间中选择最小的元素，
与未排序区间的第一个元素交换位置。

特点：
- 交换次数最少（最多 n-1 次）
- 不稳定排序（可能改变相同元素的相对顺序）

时间复杂度：O(n²) （无论什么情况都是）
空间复杂度：O(1)
稳定性：不稳定排序
"""


def selection_sort(nums: list[int]) -> None:
    """选择排序实现。

    算法步骤：
    1. 外循环控制当前要确定的位置 i
    2. 内循环在 [i, n-1] 中找最小元素
    3. 记录最小元素的索引 k
    4. 将 nums[i] 与 nums[k] 交换

    参数：
        nums: 待排序的列表（原地修改）
    """
    n = len(nums)

    for i in range(n - 1):
        k = i

        for j in range(i + 1, n):
            if nums[j] < nums[k]:
                k = j

        nums[i], nums[k] = nums[k], nums[i]


if __name__ == "__main__":
    test_cases = [
        [4, 1, 3, 1, 5, 2],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
    ]

    print("选择排序测试")
    print("=" * 50)

    for arr in test_cases:
        original = arr.copy()
        selection_sort(arr)
        print(f"✅ {original} → {arr}")