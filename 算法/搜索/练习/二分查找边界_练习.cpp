#include <vector>

using namespace std;

/*
 * 辅助函数：返回 target 的最左插入点
 * 说明：边界查找依赖该函数，请先完成它
 */
int binarySearchInsertion(vector<int> &nums, int target) {
    int left = 0;
    int right = static_cast<int>(nums.size()) - 1;

    while (left <= right) {
        int mid = left + (right - left) / 2;

        // 提示：
        // 1) nums[mid] < target：left = mid + 1
        // 2) nums[mid] >= target：right = mid - 1
    }

    return left;
}

/* 二分查找最左一个 target */
int binarySearchLeftEdge(vector<int> &nums, int target) {
    // 步骤 1：先求 target 的最左插入点
    int index = binarySearchInsertion(nums, target);

    // 步骤 2：校验 index 是否越界，或是否真的指向 target
    // 若不满足条件返回 -1

    // 步骤 3：满足条件则返回 index
    return index;
}

/* 二分查找最右一个 target */
int binarySearchRightEdge(vector<int> &nums, int target) {
    // 步骤 1：将问题转化为查找 target + 1 的最左插入点
    int index = binarySearchInsertion(nums, target + 1);

    // 步骤 2：最右 target 的位置应为 index - 1
    int rightEdge = index - 1;

    // 步骤 3：校验 rightEdge 是否有效且 nums[rightEdge] == target
    // 若不满足条件返回 -1

    // 步骤 4：返回 rightEdge
    return rightEdge;
}
