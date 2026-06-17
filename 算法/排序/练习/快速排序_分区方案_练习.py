"""快速排序变体练习版 - 不同分区方案和优化策略。

本文件包含三种快速排序的变体实现：

1. Hoare 分区方案（原始版本）
   - 使用中间元素作为基准
   - 指针从两端向中间移动
   - 返回的分区点可能不同

2. 非递归实现（使用栈模拟）
   - 用栈存储待排序区间
   - 避免递归导致的栈溢出风险
   - 适合深度较大的情况

3. 三路分区（处理重复元素）
   - 将数组分为三部分：< pivot, = pivot, > pivot
   - 大量重复元素时效率更高
   - 减少不必要的递归调用

每种方案针对不同场景进行优化。
"""


def quicksort_hoare(arr: list[int]) -> list[int]:
    """Hoare分区方案的快速排序。"""
    def _quicksort(low: int, high: int) -> None:
        if low < high:
            pivot_index = partition_hoare(arr, low, high)
            _quicksort(low, pivot_index)
            _quicksort(pivot_index + 1, high)

    _quicksort(0, len(arr) - 1)
    return arr


def partition_hoare(arr: list[int], low: int, high: int) -> int:
    """Hoare分区方案。

    特点：
    - 选择中间元素作为基准
    - 指针 i 从左找 >= pivot，j 从右找 <= pivot
    - 交换后继续，直到指针相遇
    """
    pivot = arr[(low + high) // 2]
    i, j = low - 1, high + 1

    while True:
        i += 1
        while arr[i] < pivot:
            i += 1

        j -= 1
        while arr[j] > pivot:
            j -= 1

        if i >= j:
            return j

        arr[i], arr[j] = arr[j], arr[i]


def quick_sort_iterative(arr: list[int]) -> None:
    """非递归快速排序（使用栈模拟）。

    核心思路：
    - 使用列表模拟系统栈
    - 存储待处理的 [start, end] 区间
    - 循环处理直到栈为空
    """
    if len(arr) <= 0:
        return

    ranges = [(0, len(arr) - 1)]

    while ranges:
        start, end = ranges.pop()
        if start >= end:
            continue

        mid = arr[(start + end) // 2]
        left, right = start, end

        while True:
            while arr[left] < mid:
                left += 1
            while arr[right] > mid:
                right -= 1

            if left <= right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
            else:
                break

        if start < right:
            ranges.append((start, right))
        if end > left:
            ranges.append((left, end))


def quicksort_3way(arr: list[int], low: int, high: int) -> None:
    """三路分区快速排序。

    适用场景：数组中有大量重复元素

    将数组分为三个区域：
    - [low, lt-1]: < pivot
    - [lt, gt]: == pivot
    - [gt+1, high]: > pivot

    只需对 < 和 > 区域递归，= 的区域已经有序！
    """
    if low >= high:
        return

    lt, i, gt = low, low, high
    pivot = arr[low]

    while i <= gt:
        if arr[i] < pivot:
            arr[lt], arr[i] = arr[i], arr[lt]
            lt += 1
            i += 1
        elif arr[i] > pivot:
            arr[i], arr[gt] = arr[gt], arr[i]
            gt -= 1
        else:
            i += 1

    quicksort_3way(arr, low, lt - 1)
    quicksort_3way(arr, gt + 1, high)


if __name__ == "__main__":
    test_arr = [4, 1, 3, 1, 5, 2, 3, 3]

    print("=" * 60)
    print("快速排序变体测试")
    print("=" * 60)

    original = test_arr.copy()
    result = quicksort_hoare(test_arr.copy())
    print(f"✅ Hoare分区: {original} → {result}")

    test_arr2 = original.copy()
    quick_sort_iterative(test_arr2)
    print(f"✅ 非递归版: {original} → {test_arr2}")

    test_arr3 = original.copy()
    quicksort_3way(test_arr3, 0, len(test_arr3) - 1)
    print(f"✅ 三路分区: {original} → {test_arr3}")

    print("\n💡 关键要点：")
    print("- Hoare: 原始版本，代码简洁")
    print("- 非递归: 避免栈溢出，适合大数据量")
    print("- 三路分区: 优化重复元素多的场景")