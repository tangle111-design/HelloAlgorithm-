"""插入排序练习版 - 类似整理扑克牌的方式。

核心思想：
将数组分为"已排序"和"未排序"两部分，
每次从未排序部分取出一个元素，
插入到已排序部分的正确位置。

类比：
就像打牌时，拿到新牌后插入到手牌中合适的位置。

时间复杂度：O(n²)（最佳 O(n)）
空间复杂度：O(1)
稳定性：稳定排序
"""


def insertion_sort(nums: list[int]) -> None:
    """插入排序实现。

    算法步骤：
    1. 外循环从第2个元素开始（i=1），逐个处理
    2. 取出当前元素 base = nums[i]
    3. 内循环：在已排序区间 [0, i-1] 中找正确位置
       将比 base 大的元素都向后移动一位
    4. 将 base 放入空出的位置

    参数：
        nums: 待排序列表（原地修改）
    """
    # 步骤 1：外循环遍历每个元素（从第2个开始）
    for i in range(1, len(nums)):
        # 步骤 2：取出当前元素作为基准
        # TODO: base = nums[i]
        base = nums[i]

        j = i - 1

        # 步骤 3：内循环 - 找到 base 的正确位置
        while j >= 0 and nums[j] > base:
            # 步骤 4：将比 base 大的元素向右移动
            # TODO: nums[j+1] = nums[j]
            nums[j + 1] = nums[j]
            j -= 1

        # 步骤 5：将 base 放入正确位置
        # TODO: nums[j+1] = base
        nums[j + 1] = base


if __name__ == "__main__":
    test_cases = [
        [4, 1, 3, 1, 5, 2],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
    ]

    print("=" * 60)
    print("插入排序测试")
    print("=" * 60)

    for arr in test_cases:
        original = arr.copy()
        insertion_sort(arr)
        print(f"✅ {original} → {arr}")

    print("\n💡 关键要点：")
    print("- 已排序区间逐渐扩大")
    print("- 最佳情况 O(n)（已有序时）")
    print("- 适合小规模或基本有序的数据")