/**
 * 二分查找边界练习版（C++）
 *
 * 功能：在有重复元素的有序数组中查找边界
 *
 * 最左边界：第一个出现 target 的位置
 * 最右边界：最后一个出现 target 的位置
 *
 * 实现技巧：
 * 利用"查找插入点"函数来实现边界查找
 * - 最左边界 = target 的插入点
 * - 最右边界 = (target+1) 的插入点 - 1
 */

/* 查找最左侧的 target */
int binarySearchLeftEdge(vector<int> &nums, int target) {
    // 步骤 1：调用插入点函数获取位置
    // TODO: i = binarySearchInsertion(nums, target)
    int i = binarySearchInsertion(nums, target);

    // 步骤 2：边界检查
    // TODO: 检查两种情况：
    //       1. i == nums.size()（target 比所有元素都大）
    //       2. nums[i] != target（该位置不是 target）
    //       如果满足任一条件，return -1
    if (i == nums.size() || nums[i] != target) {
        return -1; // 未找到
    }

    // 步骤 3：返回最左侧索引
    // TODO: return i
    return i;
}

/* 查找最右侧的 target */
int binarySearchRightEdge(vector<int> &nums, int target) {
    // 步骤 1：查找 "target+1" 的插入点
    // 这样得到的是首个 > target 的位置
    // TODO: i = binarySearchInsertion(nums, target + 1)
    int i = binarySearchInsertion(nums, target + 1);

    // 步骤 2：计算最右侧位置
    // 最右侧的 target 就在 i 的前一个位置
    // TODO: j = i - 1
    int j = i - 1;

    // 步骤 3：边界检查
    // TODO: 若 j == -1 或 nums[j] != target，return -1
    if (j == -1 || nums[j] != target) {
        return -1;
    }

    // 步骤 4：返回结果
    // TODO: return j
    return j;
}

/**
 * 💡 应用示例：统计 target 出现次数
 * count = binarySearchRightEdge(...) - binarySearchLeftEdge(...) + 1
 */