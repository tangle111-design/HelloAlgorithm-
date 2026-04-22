#include <unordered_map>
#include <vector>

using namespace std;

// 给定整数数组 nums 和目标值 target，返回任意一组满足 nums[i] + nums[j] == target 的下标
/* 方法：辅助哈希表 */
vector<int> twoSumHashTable(vector<int> &nums, int target) {
    // 步骤 1：创建哈希表，记录“数值 -> 下标”
    unordered_map<int, int> dic;

    // 步骤 2：遍历数组，每次先查“补数”是否已出现
    for (int i = 0; i < static_cast<int>(nums.size()); i++) {
        int complement = target - nums[i];

        // 步骤 3：若补数在哈希表中，立即返回答案

        // 步骤 4：若未命中，把当前值与下标写入哈希表
        // 提示：要先查再写，避免同一个元素被使用两次
    }

    // 步骤 5：若无解，返回空数组
    return {};
}
