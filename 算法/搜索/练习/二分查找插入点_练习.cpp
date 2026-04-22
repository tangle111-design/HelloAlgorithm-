#include <vector>

using namespace std;

/* 二分查找插入点（无重复元素） */
int binarySearchInsertionSimple(vector<int> &nums, int target) {
    // 步骤 1：初始化双闭区间 [left, right]
    int left = 0;
    int right = static_cast<int>(nums.size()) - 1;

    // 步骤 2：循环查找 target 或其应插入的位置
    while (left <= right) {
        // 步骤 3：计算中点
        int mid = left + (right - left) / 2;

        // 步骤 4：根据比较结果移动边界
        // 1) nums[mid] < target：去右半区间
        // 2) nums[mid] > target：去左半区间
        // 3) nums[mid] == target：直接返回 mid
    }

    // 步骤 5：未命中时，left 即插入点
    return left;
}

/* 二分查找插入点（存在重复元素，返回最左插入点） */
int binarySearchInsertion(vector<int> &nums, int target) {
    // 步骤 1：初始化双闭区间 [left, right]
    int left = 0;
    int right = static_cast<int>(nums.size()) - 1;

    // 步骤 2：循环逼近最左插入位置
    while (left <= right) {
        // 步骤 3：计算中点
        int mid = left + (right - left) / 2;

        // 步骤 4：关键点在于“相等时继续向左收缩”
        // 1) nums[mid] < target：left 右移
        // 2) nums[mid] > target：right 左移
        // 3) nums[mid] == target：right 左移（继续找更靠左的位置）
    }

    // 步骤 5：left 即最左插入点
    return left;
}
