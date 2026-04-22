#include <iostream>
#include <stdexcept>
#include <unordered_map>
#include <vector>

using namespace std;

struct Vertex {
    int val;

    explicit Vertex(int x) : val(x) {}
};

vector<int> vetsToVals(const vector<Vertex *> &vets) {
    vector<int> vals;
    vals.reserve(vets.size());
    for (Vertex *vet : vets) {
        vals.push_back(vet->val);
    }
    return vals;
}

void printVector(const vector<int> &vec) {
    cout << "[";
    for (size_t i = 0; i < vec.size(); i++) {
        cout << vec[i];
        if (i + 1 < vec.size()) {
            cout << ", ";
        }
    }
    cout << "]" << endl;
}

/* 基于邻接表实现的无向图类 */
class GraphAdjList {
  public:
    unordered_map<Vertex *, vector<Vertex *>> adjList;

    /* 在 vector 中删除指定节点 */
    void remove(vector<Vertex *> &vec, Vertex *vet) {
        // 步骤提示：
        // 1) 线性扫描 vec。
        // 2) 找到目标节点后删除该位置元素。
        // 3) 删除后立即结束，避免越界与重复删除。

        // TODO: 在这里补全删除逻辑。
    }

    /* 构造方法 */
    GraphAdjList(const vector<vector<Vertex *>> &edges) {
        // 步骤提示：
        // 1) 遍历每条边 [u, v]。
        // 2) 先确保 u、v 都已加入邻接表。
        // 3) 再添加无向边 u-v。

        // TODO: 在这里补全构造逻辑。
    }

    int size() {
        return static_cast<int>(adjList.size());
    }

    /* 添加边 */
    void addEdge(Vertex *vet1, Vertex *vet2) {
        if (!adjList.count(vet1) || !adjList.count(vet2) || vet1 == vet2) {
            throw invalid_argument("不存在顶点");
        }

        // 步骤提示：
        // 1) 无向边需要双向添加。
        // 2) 分别把 vet2 加到 vet1 的链表、把 vet1 加到 vet2 的链表。

        // TODO: 在这里补全添加边逻辑。
    }

    /* 删除边 */
    void removeEdge(Vertex *vet1, Vertex *vet2) {
        if (!adjList.count(vet1) || !adjList.count(vet2) || vet1 == vet2) {
            throw invalid_argument("不存在顶点");
        }

        // 步骤提示：
        // 1) 在 vet1 的邻接链表中删除 vet2。
        // 2) 在 vet2 的邻接链表中删除 vet1。

        // TODO: 在这里补全删除边逻辑。
    }

    /* 添加顶点 */
    void addVertex(Vertex *vet) {
        if (adjList.count(vet)) {
            return;
        }

        // 步骤提示：
        // 1) 为该顶点创建空邻接链表。

        // TODO: 在这里补全添加顶点逻辑。
    }

    /* 删除顶点 */
    void removeVertex(Vertex *vet) {
        if (!adjList.count(vet)) {
            throw invalid_argument("不存在顶点");
        }

        // 步骤提示：
        // 1) 删除该顶点在邻接表中的主键记录。
        // 2) 遍历其余所有顶点的邻接链表。
        // 3) 把所有指向该顶点的边删除。

        // TODO: 在这里补全删除顶点逻辑。
    }

    /* 打印邻接表 */
    void print() {
        // 步骤提示：
        // 1) 遍历邻接表的每个键值对。
        // 2) 输出顶点值与邻接顶点值列表。

        // TODO: 在这里补全打印逻辑。
    }
};
