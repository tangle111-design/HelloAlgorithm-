#include <queue>
#include <vector>

using namespace std;

/* 基于堆查找数组中最大的 k 个元素 */
priority_queue<int, vector<int>, greater<int>> topKHeap(vector<int> &nums, int k) {
  // 步骤提示：
  // 1) 使用小顶堆保存“当前最大的 k 个元素”。
  // 2) 先把前 k 个元素入堆，建立大小为 k 的初始窗口。
  // 3) 从第 k 个下标开始遍历后续元素。
  // 4) 若当前元素大于堆顶，先弹出堆顶再把当前元素入堆。
  // 5) 遍历结束后，堆中即为最大 k 个元素。
  priority_queue<int, vector<int>, greater<int>> heap;
  for (int i = 0; i < k; i++) {
    heap.push(nums[i]);
  }
  for (int i = k; i < nums.size(); i++) {
    if (heap.top() < nums[i]) {
      heap.pop();
      heap.push(nums[i]);
    }
  }
  return heap;
}
