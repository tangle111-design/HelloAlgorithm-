#include <stdexcept>
#include <vector>

using namespace std;

/* 大顶堆：基础操作练习壳 */
class MaxHeap {
  private:
    vector<int> maxHeap;

  public:
    MaxHeap() = default;

    int size() const {
        return static_cast<int>(maxHeap.size());
    }

    bool isEmpty() const {
        return maxHeap.empty();
    }

    /* 获取左子节点的索引 */
    int left(int i);

    /* 获取右子节点的索引 */
    int right(int i);

    /* 获取父节点的索引 */
    int parent(int i);

    /* 访问堆顶元素 */
    int peek() const;

    /* 元素入堆 */
    void push(int val);

    /* 从节点 i 开始，从底至顶堆化 */
    void siftUp(int i);

    /* 元素出堆 */
    void pop();

    /* 从节点 i 开始，从顶至底堆化 */
    void siftDown(int i);

    const vector<int> &data() const {
        return maxHeap;
    }
};

/* 获取左子节点的索引 */
int MaxHeap::left(int i) {
    // 步骤提示：
    // 1) 完全二叉树中，索引 i 的左子节点索引为 2 * i + 1。
    // 2) 直接返回计算结果。
}

/* 获取右子节点的索引 */
int MaxHeap::right(int i) {
    // 步骤提示：
    // 1) 完全二叉树中，索引 i 的右子节点索引为 2 * i + 2。
    // 2) 直接返回计算结果。
}

/* 获取父节点的索引 */
int MaxHeap::parent(int i) {
    // 步骤提示：
    // 1) 索引 i 的父节点索引为 (i - 1) / 2。
    // 2) 注意 i = 0 时表示根节点，没有有效父节点。
}

/* 访问堆顶元素 */
int MaxHeap::peek() const {
    // 步骤提示：
    // 1) 先判断堆是否为空，空堆需要抛出异常。
    // 2) 非空时返回索引 0 处元素。
}

/* 元素入堆 */
void MaxHeap::push(int val) {
    // 步骤提示：
    // 1) 先把新元素追加到数组末尾。
    // 2) 从新元素位置开始执行 siftUp，恢复大顶堆性质。
}

/* 从节点 i 开始，从底至顶堆化 */
void MaxHeap::siftUp(int i) {
    // 步骤提示：
    // 1) 循环计算父节点索引 p = parent(i)。
    // 2) 若 i 已到根，或当前节点 <= 父节点，停止。
    // 3) 否则交换当前节点与父节点。
    // 4) 把 i 更新为 p，继续向上修复。
}

/* 元素出堆 */
void MaxHeap::pop() {
    // 步骤提示：
    // 1) 判空：空堆应抛出异常。
    // 2) 交换堆顶与末尾元素。
    // 3) 删除末尾元素。
    // 4) 从根节点执行 siftDown，恢复堆性质。
}

/* 从节点 i 开始，从顶至底堆化 */
void MaxHeap::siftDown(int i) {
    // 步骤提示：
    // 1) 计算左、右子节点索引。
    // 2) 在 i、left(i)、right(i) 三者中找最大值索引 ma。
    // 3) 若 ma == i，说明该子树已满足堆性质，停止。
    // 4) 否则交换 i 与 ma，并令 i = ma 继续向下修复。
}
