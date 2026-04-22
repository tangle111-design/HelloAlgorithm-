def merge(nums: list[int], left: int, mid: int, right: int):
    """合并两个有序区间 [left, mid] 和 [mid + 1, right]"""
    tmp = [0] * (right - left + 1)

    i = left
    j = mid + 1
    k = 0

    # TODO 1: 双指针比较，把更小值写入 tmp
    while i <= mid and j <= right:
        if nums[i] <= nums[j]:
            tmp[k] = nums[i]
            i += 1
        else:
            tmp[k] = nums[j]
            j += 1
        k += 1

    # TODO 2: 处理左半区剩余元素
    while i <= mid:
        tmp[k] = nums[i]
        i += 1
        k += 1

    # TODO 3: 处理右半区剩余元素
    while j <= right:
        tmp[k] = nums[j]
        j += 1
        k += 1

    # TODO 4: 回写到原数组对应区间
    for p in range(len(tmp)):
        nums[left + p] = tmp[p]


def merge_sort(nums: list[int], left: int, right: int):
    """归并排序练习版（原地覆盖）"""
    # TODO 1: 递归终止条件
    if left >= right:
        return

    # TODO 2: 计算中点并递归处理左右区间
    mid = (left + right) // 2
    merge_sort(nums, left, mid)
    merge_sort(nums, mid + 1, right)

    # TODO 3: 合并两个有序子区间
    merge(nums, left, mid, right)
