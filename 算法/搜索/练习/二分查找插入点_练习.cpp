/**
 * 二分查找插入点练习版（C++）
 *
 * 功能：找到 target 在有序数组中的插入位置
 *
 * 版本1：无重复元素
 * - 找到 target 直接返回其位置
 * - 找不到则返回应该插入的位置
 *
 * 版本2：有重复元素
 * - 返回最左侧的插入位置
 * - 关键技巧：即使找到 target 也不立即返回，继续向左搜索
 */

/* 版本1：无重复元素的插入点查找 */
int binarySearchInsertionSimple(vector<int> &nums, int target) {
    // 步骤 1：初始化区间
    // TODO: i = 0, j = nums.size() - 1
    int i = 0, j = nums.size() - 1;

    // 步骤 2：循环查找
    while (i <= j) {
        int m = i + (j - i) / 2;

        // 步骤 3：三种情况判断
        if (nums[m] < target) {
            // TODO: target 在右半区，i = m + 1
            i = m + 1;
        } else if (nums[m] > target) {
            // TODO: target 在左半区，j = m - 1
            j = m - 1;
        } else {
            // 找到 target，直接返回
            // TODO: return m
            return m;
        }
    }

    // 步骤 4：返回插入点
    // TODO: return i
    return i;
}

/* 版本2：有重复元素 - 返回最左侧位置 */
int binarySearchInsertion(vector<int> &nums, int target) {
    int i = 0, j = nums.size() - 1;

    while (i <= j) {
        int m = i + (j - i) / 2;

        if (nums[m] < target) {
            i = m + 1;
        } else if (nums[m] > target) {
            j = m - 1;
        } else {
            // ⭐ 关键区别！
            // 即使找到了 target 也不返回
            // 而是继续向左搜索，以找到最左侧的位置
            // TODO: j = m - 1
            j = m - 1;
        }
    }

    // 返回最左侧的插入点
    // TODO: return i
    return i;
}