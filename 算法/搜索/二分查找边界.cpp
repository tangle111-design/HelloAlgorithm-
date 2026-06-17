/**
 * 二分查找边界（Binary Search for Boundaries）
 *
 * 功能：
 * - 查找目标值的**最左边界**（第一个出现的位置）
 * - 查找目标值的**最右边界**（最后一个出现的位置）
 *
 * 应用场景：
 * - 在有重复元素的有序数组中精确定位
 * - 统计某个值出现的次数（right - left + 1）
 *
 * 核心技巧：
 * 利用"查找插入点"的函数来实现边界查找
 */

/* 查找最左一个 target */
int binarySearchLeftEdge(vector<int> &nums, int target) {
    // 复用插入点函数：找到 target 应该插入的位置
    // 这个位置就是最左侧的 target 索引（如果存在的话）
    int i = binarySearchInsertion(nums, target);

    // 边界检查：
    // 1. i == nums.size()：target 比所有元素都大，应该插入到末尾
    // 2. nums[i] != target：位置 i 的元素不是 target，说明 target 不存在
    if (i == nums.size() || nums[i] != target) {
        return -1; // 未找到 target
    }

    return i; // 返回最左侧索引
}

/* 查找最右一个 target */
int binarySearchRightEdge(vector<int> &nums, int target) {
    // 技巧：查找 "target + 1" 的插入点
    // 这样得到的是首个 > target 的位置
    int i = binarySearchInsertion(nums, target + 1);

    // 最右侧的 target 就在 i 的前一个位置
    int j = i - 1;

    // 边界检查：j < 0 或 nums[j] != target 说明不存在
    if (j == -1 || nums[j] != target) {
        return -1;
    }

    return j; // 返回最右侧索引
}