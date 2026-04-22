def quicksort_hoare(arr):
    """使用Hoare分区方案的快速排序"""
    def _quicksort(low, high):
        if low < high:
            # 分区操作，返回基准位置
            pivot_index = partition_hoare(arr, low, high)
            # 递归排序左右子数组
            _quicksort(low, pivot_index)
            _quicksort(pivot_index + 1, high)
    
    _quicksort(0, len(arr) - 1)
    print()
    return arr

def partition_hoare(arr, low, high):
    """Hoare分区方案"""
    # 选择中间元素作为基准
    pivot = arr[(low + high) // 2]
    print("当前基准",pivot)
    
    i = low - 1
    j = high + 1
    
    while True:
        # 从左向右找到第一个大于等于基准的元素
        i += 1
        while arr[i] < pivot:
            i += 1
        
        # 从右向左找到第一个小于等于基准的元素
        j -= 1
        while arr[j] > pivot:
            j -= 1
        
        # 如果指针相遇或交叉，分区完成
        if i >= j:
            return j
        
        # 交换元素
        arr[i], arr[j] = arr[j], arr[i]
        
def quick_sort(arr):
    """非递归实现的快速排序（使用栈模拟递归）"""
    if len(arr) <= 0:
        return
    
    # 使用列表模拟栈，存储需要排序的范围
    ranges = []
    ranges.append((0, len(arr) - 1))
    
    while ranges:
        # 弹出栈顶的范围
        start, end = ranges.pop()
        if start >= end:
            continue
        
        # 选择中间点作为基准
        mid = arr[(start + end) // 2]
        left, right = start, end
        
        # Hoare分区方案
        while True:
            # 从左向右找到第一个大于等于基准的元素
            while arr[left] < mid:
                left += 1
            # 从右向左找到第一个小于等于基准的元素
            while arr[right] > mid:
                right -= 1
            
            if left <= right:
                # 交换元素
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
            else:
                break
        
        # 将子范围压入栈中
        if start < right:
            ranges.append((start, right))
        if end > left:
            ranges.append((left, end))


def quicksort_3way(arr, low, high):
    if low >= high:
        return
    # 三路分区
    lt, i, gt = low, low, high
    pivot = arr[low]   # 选择第一个元素为基准（可随机优化）
    while i <= gt:
        if arr[i] < pivot:
            arr[lt], arr[i] = arr[i], arr[lt]
            lt += 1
            i += 1
        elif arr[i] > pivot:
            arr[i], arr[gt] = arr[gt], arr[i]
            gt -= 1
        else:  # arr[i] == pivot
            i += 1
    # 递归处理小于区和大于区
    quicksort_3way(arr, low, lt - 1)
    quicksort_3way(arr, gt + 1, high)


