/**
 * 二分查找练习版（C++）
 *
 * 问题描述：
 * 在有序数组中查找目标值 target，
 * 若存在返回其索引，否则返回 -1
 *
 * 核心思想 - 分治策略：
 * 每次将搜索区间缩小一半：
 * 1. 计算中间位置 mid = (left + right) / 2
 * 2. 比较 nums[mid] 与 target
 * 3. 根据比较结果调整区间边界
 *
 * 时间复杂度：O(log n)
 * 空间复杂度：O(1)
 */

int binarySearch(vector<int> &nums, int target) {
    // 步骤 1：初始化双闭区间 [0, n-1]
    // TODO: 设置 i = 0, j = nums.size() - 1
    int i = 0, j = nums.size() - 1;

    // 步骤 2：循环直到区间为空
    // TODO: 使用 while 循环，条件为 i <= j
    while (i <= j) {
        // 步骤 3：计算中点索引
        // TODO: m = i + (j - i) / 2 （注意这种写法可以防止溢出）
        int m = i + (j - i) / 2;

        // 步骤 4：比较并调整区间
        // TODO: 使用 if-else if-else 结构处理三种情况：
        if (nums[m] < target)
            // 情况1：target 在右半区
            // TODO: 更新左边界 i = m + 1
            i = m + 1;
        else if (nums[m] > target)
            // 情况2：target 在左半区
            // TODO: 更新右边界 j = m - 1
            j = m - 1;
        else
            // 情况3：找到目标！
            // TODO: 返回 m
            return m;
    }

    // 步骤 5：未找到目标
    // TODO: 返回 -1
    return -1;
}