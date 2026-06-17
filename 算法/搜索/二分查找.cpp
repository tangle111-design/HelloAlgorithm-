/**
 * 二分查找（Binary Search）- 迭代版本（双闭区间）
 *
 * 问题描述：
 * 在有序数组中查找目标值 target，
 * 若存在则返回其索引，否则返回 -1
 *
 * 算法思路：
 * 使用双闭区间 [i, j]，每次将区间缩小一半：
 * - 计算 mid = i + (j-i)/2 （防止溢出）
 * - 比较 nums[mid] 与 target
 * - 根据结果调整左边界或右边界
 *
 * 时间复杂度：O(log n)
 * 空间复杂度：O(1)
 */

int binarySearch(vector<int> &nums, int target) {
    // 初始化双闭区间 [0, n-1]
    int i = 0, j = nums.size() - 1;

    // 循环直到区间为空（i > j 时退出）
    while (i <= j) {
        // 计算中点索引 m（使用这种方式防止整数溢出）
        int m = i + (j - i) / 2;

        if (nums[m] < target)
            // target 在右半区 [m+1, j]
            i = m + 1;
        else if (nums[m] > target)
            // target 在左半区 [i, m-1]
            j = m - 1;
        else
            // 找到目标元素，返回索引
            return m;
    }

    // 未找到目标元素
    return -1;
}