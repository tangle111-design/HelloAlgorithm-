#include <stdexcept>
#include <unordered_map>
#include <unordered_set>
#include <vector>

using namespace std;

struct Vertex {
    int val;

    explicit Vertex(int x) : val(x) {}
};

class GraphAdjList {
  public:
    unordered_map<Vertex *, vector<Vertex *>> adjList;

    void addVertex(Vertex *vet) {
        if (!adjList.count(vet)) {
            adjList[vet] = {};
        }
    }

    void addEdge(Vertex *vet1, Vertex *vet2) {
        if (vet1 == vet2) {
            throw invalid_argument("不允许自环");
        }
        addVertex(vet1);
        addVertex(vet2);
        adjList[vet1].push_back(vet2);
        adjList[vet2].push_back(vet1);
    }
};

/* 深度优先遍历辅助函数 */
void dfs(GraphAdjList &graph, unordered_set<Vertex *> &visited, vector<Vertex *> &res, Vertex *vet) {
    // 步骤提示：
    // 1) 先记录当前顶点，并标记已访问。
    // 2) 遍历当前顶点的所有邻接点。
    // 3) 遇到未访问的邻接点时递归调用 dfs。

    // TODO: 在这里补全递归 DFS。
}

/* 深度优先遍历 */
vector<Vertex *> graphDFS(GraphAdjList &graph, Vertex *startVet) {
    vector<Vertex *> res;
    unordered_set<Vertex *> visited;

    // 步骤提示：
    // 1) 初始化结果容器与 visited。
    // 2) 以 startVet 作为递归入口调用 dfs。
    // 3) 返回遍历结果。

    // TODO: 在这里补全 DFS 入口逻辑。

    return res;
}
