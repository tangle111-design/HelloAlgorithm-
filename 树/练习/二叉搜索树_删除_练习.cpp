#include <iostream>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;

    explicit TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class BinarySearchTree {
  private:
    TreeNode *root;

  public:
    BinarySearchTree() : root(nullptr) {}

    void remove(int num) {
        // 步骤提示：
        // 1) 先处理空树。
        // 2) 用 cur/pre 查找目标节点位置。
        // 3) 若未找到直接返回。
        // 4) 删除分情况：
        //    - 0 或 1 个子节点：父节点直接接 child。
        //    - 2 个子节点：找中序后继，拷贝值，再递归删除后继节点。
        // 5) 注意 root 被删除时的重连处理。

        // 请在这里补充删除逻辑。
    }
};
