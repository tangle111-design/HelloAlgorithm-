#include <iostream>
#include <stdexcept>
#include <vector>

using namespace std;

template <typename T>
void printVector(const vector<T> &vec) {
    cout << "[";
    for (size_t i = 0; i < vec.size(); i++) {
        cout << vec[i];
        if (i + 1 < vec.size()) {
            cout << ", ";
        }
    }
    cout << "]" << endl;
}

void printVectorMatrix(const vector<vector<int>> &mat) {
    for (const auto &row : mat) {
        printVector(row);
    }
}

/* 基于邻接矩阵实现的无向图类 */
class GraphAdjMat {
    vector<int> vertices;
    vector<vector<int>> adjMat;

public:
    GraphAdjMat(const vector<int> &vertices, const vector<vector<int>> &edges) {
        for (int val : vertices) {
            addVertex(val);
        }
        for (const vector<int> &edge : edges) {
            addEdge(edge[0], edge[1]);
        }
    }

    int size() const { return static_cast<int>(vertices.size()); }

    /* 添加顶点 */
    void addVertex(int val) {
        // 步骤提示：
        // 1) 记录当前顶点数量 n。
        // 2) 把新顶点值加入 vertices。
        // 3) 在邻接矩阵末尾新增一行（长度为 n，初值为 0）。
        // 4) 遍历所有行，在末尾补一列 0。
        int n = size();
        vertices.push_back(val);
        adjMat.emplace_back(vector<int>(n, 0));
        for (vector<int> &row : adjMat) {
            row.push_back(0);
        }
    }

    /* 删除顶点 */
    void removeVertex(int index) {
        if (index < 0 || index >= size()) {
            throw out_of_range("顶点不存在");
        }

        // 步骤提示：
        // 1) 从 vertices 删除下标 index 的顶点。
        // 2) 从 adjMat 删除第 index 行。
        // 3) 遍历每一行，删除第 index 列。
        vertices.erase(vertices.begin() + index);
        adjMat.erase(adjMat.begin() + index);
        for (vector<int> &row : adjMat) {
            row.erase(row.begin() + index);
        }
    }

    /* 添加边 */
    void addEdge(int i, int j) {
        if (i < 0 || j < 0 || i >= size() || j >= size() || i == j) {
            throw out_of_range("顶点不存在");
        }

        // 步骤提示：
        // 1) 无向图需要同时更新 (i, j) 与 (j, i)。
        // 2) 统一用 1 表示两点连通。
    }

    /* 删除边 */
    void removeEdge(int i, int j) {
        if (i < 0 || j < 0 || i >= size() || j >= size() || i == j) {
            throw out_of_range("顶点不存在");
        }

        // 步骤提示：
        // 1) 无向图需要同时更新 (i, j) 与 (j, i)。
        // 2) 用 0 表示两点不连通。
    }

    /* 打印邻接矩阵 */
    void print() {
        // 步骤提示：
        // 1) 先输出顶点列表。
        // 2) 再按行输出邻接矩阵。
    }
};
