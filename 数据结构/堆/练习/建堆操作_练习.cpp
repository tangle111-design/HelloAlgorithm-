#include <vector>

using namespace std;

/* 大顶堆：建堆操作练习壳 */
class MaxHeap {
  private:
    vector<int> maxHeap;

  public:
    /* 构造方法，根据输入列表建堆 */
    explicit MaxHeap(const vector<int> &nums);

    int size() const {
        return static_cast<int>(maxHeap.size());
    }

    int left(int i) {
        return 2 * i + 1;
    }

    int right(int i) {
        return 2 * i + 2;
    }

    int parent(int i) {
        return (i - 1) / 2;
    }

    /* 从节点 i 开始，从顶至底堆化 */
    void siftDown(int i);

    const vector<int> &data() const {
        return maxHeap;
    }
};

/* 构造方法，根据输入列表建堆 */
MaxHeap::MaxHeap(const vector<int> &nums) {
    // 步骤提示：
    // 1) 先把 nums 原样复制到 maxHeap。
    // 2) 最后一个非叶节点索引为 parent(size() - 1)。
    // 3) 从该索引开始，逆序遍历到 0。
    // 4) 对每个索引调用 siftDown，完成自底向上的堆化。
}

/* 从节点 i 开始，从顶至底堆化 */
void MaxHeap::siftDown(int i) {
    // 步骤提示：
    // 1) 在当前节点和左右子节点中找最大值位置 ma。
    // 2) 若 ma 仍为 i，说明该子树已是大顶堆，结束。
    // 3) 否则交换 i 与 ma。
    // 4) 令 i = ma，循环继续向下修复。
}
