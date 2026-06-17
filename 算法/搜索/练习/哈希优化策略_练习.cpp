/**
 * 哈希优化策略练习版（C++）- 两数之和问题
 *
 * 问题描述：
 * 给定数组 nums 和目标值 target，
 * 找出两个数使它们的和等于 target，
 * 返回这两个数的索引。
 *
 * 哈希表法 vs 暴力法：
 * - 暴力法：双重循环 O(n²)
 * - 哈希表：单层循环 O(n)，空间换时间
 *
 * 核心思路：
 * 遍历每个元素时，检查 "target - 当前值"
 * 是否已经在哈希表中出现过。
 * 如果在 → 找到解！
 * 如果不在 → 将当前值存入哈希表供后续使用
 */

vector<int> twoSumHashTable(vector<int> &nums, int target) {
    // 步骤 1：获取数组长度
    // TODO: size = nums.size()
    int size = nums.size();

    // 步骤 2：创建哈希表
    // 存储格式：{元素值: 索引}
    // TODO: unordered_map<int, int> dic
    unordered_map<int, int> dic;

    // 步骤 3：遍历数组
    for (int i = 0; i < size; i++) {
        // 步骤 4：计算补数（complement）
        // complement = target - nums[i]
        // 即：如果找到一个数等于 complement，就能凑成 target

        // 步骤 5：在哈希表中查找补数
        // TODO: 使用 dic.find(target - nums[i]) 查找
        if (dic.find(target - nums[i]) != dic.end()) {
            // 找到解！返回两个索引
            // TODO: return {dic[target - nums[i]], i}
            return {dic[target - nums[i]], i};
        }

        // 步骤 6：将当前元素存入哈希表
        // TODO: dic.emplace(nums[i], i)
        dic.emplace(nums[i], i);
    }

    // 步骤 7：未找到解
    // TODO: return {}（空向量）
    return {};
}