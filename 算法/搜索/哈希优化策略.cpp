/**
 * 哈希优化策略（Hash Optimization）- 两数之和问题
 *
 * 问题描述（LeetCode 1）：
 * 给定一个整数数组 nums 和一个目标值 target，
 * 在数组中找出和为 target 的两个元素，
 * 并返回它们的数组索引。
 *
 * 方法对比：
 * - 暴力法：O(n²) 时间，O(1) 空间
 * - 哈希表法：O(n) 时间，O(n) 空间 ← 本实现
 *
 * 核心思想：
 * 遍历数组时，对于每个元素 nums[i]，
 * 检查 (target - nums[i]) 是否已经在哈希表中。
 * 如果在，说明之前遇到过配对的元素；
 * 如果不在，将当前元素及其索引存入哈希表。
 */

/* 方法二：使用辅助哈希表优化 */
vector<int> twoSumHashTable(vector<int> &nums, int target) {
    int size = nums.size();

    // 创建哈希表存储 {元素值: 索引}
    unordered_map<int, int> dic;

    // 单层遍历数组
    for (int i = 0; i < size; i++) {
        // 检查 complement（补数）是否已存在于哈希表中
        if (dic.find(target - nums[i]) != dic.end()) {
            // 找到解！返回两个元素的索引
            return {dic[target - nums[i]], i};
        }

        // 将当前元素和其索引存入哈希表
        dic.emplace(nums[i], i);
    }

    // 未找到解，返回空向量
    return {};
}