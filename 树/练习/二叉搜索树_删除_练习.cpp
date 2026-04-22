#include <iostream>
using namespace std;

struct TreeNode {
  int val;
  TreeNode* left;
  TreeNode* right;

  explicit TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class BinarySearchTree {
 private:
  TreeNode* root;

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

    if (root == nullptr) {
      return;
    }
    TreeNode* cur = root;
    TreeNode* pre = nullptr;
    while (cur != nullptr) {
      if (cur->val < num) {
        pre = cur;
        cur = cur->right;
      } else if (cur->val > num) {
        pre = cur;
        cur = cur->left;
      } else {
        break;
      }
    }
    if (cur == nullptr) {
      return;
    }
    if (cur->left == nullptr || cur->right == nullptr) {
      // 巧妙的child
      // 当子节点数量 = 0 / 1 时， child = nullptr / 该子节点
      TreeNode* child = cur->left != nullptr ? cur->left : cur->right;
      if (cur != root) {
        if (pre->left == cur) {
          pre->left = child;
        } else {
          pre->right = child;
        }
      } else {
        root = child;
      }
      delete cur;
    } else  // 两个子节点都存在
    {
      // 获取中序遍历中 cur 的下一个节点
      TreeNode* successor = cur->right;
      while (successor->left != nullptr) {
        successor = successor->left;
      }

      int val = successor->val;  // 暂存val
      remove(successor->val);    // 调用remove()删除successor
      cur->val = val;            // 将cur替换为后继节点
    }
  }

  // 改进版
  void remove(int num) {
    if (root == nullptr) return;

    TreeNode* cur = root;
    TreeNode* pre = nullptr;

    // 1. 查找待删除节点及其父节点
    while (cur != nullptr) {
      if (cur->val == num) break;
      pre = cur;
      if (cur->val < num)
        cur = cur->right;
      else
        cur = cur->left;
    }

    if (cur == nullptr) return;  // 未找到

    // 2. 处理有两个子节点的情况（核心改进：非递归删除后继）
    if (cur->left != nullptr && cur->right != nullptr) {
      // 找到中序后继：右子树的最左节点
      TreeNode* succ = cur->right;
      TreeNode* succ_pre = cur;  // 后继的父节点
      while (succ->left != nullptr) {
        succ_pre = succ;
        succ = succ->left;
      }

      // 用后继的值覆盖待删除节点
      cur->val = succ->val;

      // 将待删除目标转移到后继节点（后继最多有一个右子节点）
      cur = succ;
      pre = succ_pre;
    }

    // 3. 此时 cur 最多只有一个子节点，获取其子节点（可能为 nullptr）
    TreeNode* child = (cur->left != nullptr) ? cur->left : cur->right;

    // 4. 从父节点摘除 cur
    if (cur == root) {
      root = child;
    } else {
      if (pre->left == cur)
        pre->left = child;
      else
        pre->right = child;
    }
    delete cur;
  }
};
