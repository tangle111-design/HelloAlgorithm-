def partition_hoare(arr: list[int], low: int, high: int) -> int:
    """Hoare 分区方案练习壳"""
    # 核心理解：
    # 1) 选一个基准值（这里用中间值）
    # 2) 左指针找 >= pivot 的元素，右指针找 <= pivot 的元素
    # 3) 若未交错就交换，直到 i >= j
    pivot = arr[(low + high) // 2]
    i = low - 1
    j = high + 1

    while True:
        # TODO 1: i 右移到第一个 >= pivot 的位置
        i += 1
        while arr[i] < pivot:
            i += 1

        # TODO 2: j 左移到第一个 <= pivot 的位置
        j -= 1
        while arr[j] > pivot:
            j -= 1

        # TODO 3: 指针交错时返回分界点
        if i >= j:
            return j

        # TODO 4: 交换错位元素
        arr[i], arr[j] = arr[j], arr[i]


def quicksort_hoare(arr: list[int]) -> list[int]:
    """递归版快速排序（Hoare 分区）"""

    def _quicksort(low: int, high: int):
        # 注意：Hoare 分区返回 j 后，递归区间是 [low, j] 和 [j + 1, high]
        if low < high:
            pivot_index = partition_hoare(arr, low, high)
            _quicksort(low, pivot_index)
            _quicksort(pivot_index + 1, high)

    if arr:
        _quicksort(0, len(arr) - 1)
    return arr


def quick_sort_iterative(arr: list[int]):
    """非递归快速排序练习壳（栈模拟）"""
    if not arr:
        return

    ranges: list[tuple[int, int]] = [(0, len(arr) - 1)]

    while ranges:
        start, end = ranges.pop()
        if start >= end:
            continue

        # 可练习点：把这里替换成你熟悉的任意分区方案
        pivot = arr[(start + end) // 2]
        left, right = start, end

        # TODO 1: 在 [start, end] 上完成一次 Hoare 风格分区
        while True:
            while arr[left] < pivot:
                left += 1
            while arr[right] > pivot:
                right -= 1

            if left <= right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
            else:
                break

        # TODO 2: 把左右子区间入栈，继续处理
        if start < right:
            ranges.append((start, right))
        if left < end:
            ranges.append((left, end))


def quicksort_3way(arr: list[int], low: int, high: int):
    """三路快排练习壳（适合大量重复值）"""
    if low >= high:
        return

    # 三路分区含义：
    # [low, lt-1] < pivot
    # [lt, i-1]  == pivot
    # [i, gt]    未处理
    # [gt+1, high] > pivot
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
