def sift_down(nums: list[int], n: int, i: int):
    """从节点 i 开始向下调整为大顶堆（区间长度为 n）"""
    while True:
        l = 2 * i + 1
        r = 2 * i + 2
        ma = i

        # TODO 1: 在 i/l/r 三者中找最大值下标 ma
        if l < n and nums[l] > nums[ma]:
            ma = l
        if r < n and nums[r] > nums[ma]:
            ma = r

        # TODO 2: 如果当前 i 已经最大，说明堆化结束
        if ma == i:
            break

        # TODO 3: 交换并继续向下调整
        nums[i], nums[ma] = nums[ma], nums[i]
        i = ma


def heap_sort(nums: list[int]):
    """堆排序练习版（原地排序）"""
    n = len(nums)

    # TODO 1: 建堆（从最后一个非叶子结点开始下沉）
    for i in range(n // 2 - 1, -1, -1):
        sift_down(nums, n, i)

    # TODO 2: 依次把堆顶最大值放到数组尾部，再缩小堆范围
    for i in range(n - 1, 0, -1):
        nums[0], nums[i] = nums[i], nums[0]
        sift_down(nums, i, 0)
