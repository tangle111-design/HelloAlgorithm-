/**
 * 二分查找插入点（Binary Search Insertion Point）
 *
 * 功能：在有序数组中找到 target 应该插入的位置
 * 应用场景：
 * - 维护有序序列的插入操作
 * - 查找第一个大于/等于 target 的位置
 *
 * 版本1：无重复元素的情况
 * 版本2：存在重复元素的情况（返回最左侧的插入点）
 */

/* 二分查找插入点（无重复元素版本） */
int binarySearchInsertionSimple(vector<int> &nums, int target) {
    int i = 0, j = nums.size() - 1; // 双闭区间 [0, n-1]

    while (i <= j) {
        int m = i + (j - i) / 2;

        if (nums[m] < target) {
            i = m + 1; // target 在右半区
        } else if (nums[m] > target) {
            j = m - 1; // target 在左半区
        } else {
            return m; // 找到 target，直接返回
        }
    }

    // 未找到，返回插入点 i
    return i;
}

/* 二分查找插入点（存在重复元素版本 - 返回最左侧位置） */
int binarySearchInsertion(vector<int> &nums, int target) {
    int i = 0, j = nums.size() - 1;

    while (i <= j) {
        int m = i + (j - i) / 2;

        if (nums[m] < target) {
            i = m + 1;
        } else if (nums[m] > target) {
            j = m - 1;
        } else {
            // 关键区别：不立即返回，而是继续向左搜索
            // 这样可以找到最左侧的 target 位置
            j = m - 1;
        }
    }

    // 返回插入点 i（即第一个 >= target 的位置）
    return i;
}