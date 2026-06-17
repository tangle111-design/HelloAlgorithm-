"""归并排序（Merge Sort）- 分治思想的经典应用。

核心思想：
1. 将数组从中间分成两半
2. 分别对两半进行归并排序
3. 将两个有序的子数组合并成一个有序数组

特点：
- 稳定排序
- 时间复杂度稳定为 O(n log n)
- 需要额外空间 O(n)

时间复杂度：O(n log n)
空间复杂度：O(n)
稳定性：稳定排序
"""


def merge(nums: list[int], left: int, mid: int, right: int) -> None:
    """合并两个有序子数组 [left, mid] 和 [mid+1, right]。"""
    tmp = [0] * (right - left + 1)
    i, j, k = left, mid + 1, 0

    while i <= mid and j <= right:
        if nums[i] <= nums[j]:
            tmp[k] = nums[i]
            i += 1
        else:
            tmp[k] = nums[j]
            j += 1
        k += 1

    while i <= mid:
        tmp[k] = nums[i]
        i += 1
        k += 1
    while j <= right:
        tmp[k] = nums[j]
        j += 1
        k += 1

    for k in range(len(tmp)):
        nums[left + k] = tmp[k]


def merge_sort(nums: list[int], left: int, right: int) -> None:
    """归并排序主函数。"""
    if left >= right:
        return

    mid = (left + right) // 2
    merge_sort(nums, left, mid)
    merge_sort(nums, mid + 1, right)
    merge(nums, left, mid, right)


if __name__ == "__main__":
    test_cases = [
        [4, 1, 3, 1, 5, 2],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
    ]

    print("归并排序测试")
    print("=" * 50)

    for arr in test_cases:
        original = arr.copy()
        merge_sort(arr, 0, len(arr) - 1)
        print(f"✅ {original} → {arr}")