"""插入排序（Insertion Sort）- 类似整理扑克牌的排序方式。

核心思想：
将数组分为"已排序区间"和"未排序区间"，
每次从未排序区间取出一个元素，
插入到已排序区间的正确位置。

类比：
就像打牌时，每次拿到一张新牌，
都会将其插入到手牌中合适的位置。

时间复杂度：O(n²)（最佳 O(n)，当数组已有序）
空间复杂度：O(1)
稳定性：稳定排序
"""


def insertion_sort(nums: list[int]) -> None:
    """插入排序实现。

    算法步骤：
    1. 外循环从第2个元素开始（i=1）
    2. 取出当前元素 base = nums[i]
    3. 在已排序区间 [0, i-1] 中找到正确位置
    4. 将比 base 大的元素都向后移动一位
    5. 将 base 放入空出的位置

    参数：
        nums: 待排序的列表（原地修改）
    """
    for i in range(1, len(nums)):
        base = nums[i]
        j = i - 1

        while j >= 0 and nums[j] > base:
            nums[j + 1] = nums[j]
            j -= 1

        nums[j + 1] = base


if __name__ == "__main__":
    test_cases = [
        [4, 1, 3, 1, 5, 2],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
    ]

    print("插入排序测试")
    print("=" * 50)

    for arr in test_cases:
        original = arr.copy()
        insertion_sort(arr)
        print(f"✅ {original} → {arr}")