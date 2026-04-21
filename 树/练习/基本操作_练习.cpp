#include <iostream>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;

    explicit TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

void build_demo_tree() {
    // 步骤提示：
    // 1) 创建 1~5 号节点。
    // 2) 按层连接为一棵简单二叉树。
    // 3) 在 n1->left 与 n2 之间插入节点 P。
    // 4) 再把 P 删除，恢复原连接。
    // 5) 释放动态分配的节点内存。

    // 请在这里补充构建、插入、删除与释放逻辑。
}
