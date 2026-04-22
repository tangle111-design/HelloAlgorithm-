#include <vector>

using namespace std;

/* 二分查找（双闭区间） */
int binarySearch(vector<int> &nums, int target) {
    // 步骤 1：初始化左右指针，表示当前搜索区间 [left, right]
    int left = 0;
    int right = static_cast<int>(nums.size()) - 1;

    // 步骤 2：当区间非空时循环
    while (left <= right) {
        // 步骤 3：计算中点，避免 (left + right) 溢出
        int mid = left + (right - left) / 2;

        // 步骤 4：比较 nums[mid] 和 target，缩小到一半区间
        // 1) 若 nums[mid] < target，目标只可能在右半区间
        // 2) 若 nums[mid] > target，目标只可能在左半区间
        // 3) 若相等，直接返回 mid
    }

    // 步骤 5：循环结束说明未找到，返回 -1
    return -1;
}
