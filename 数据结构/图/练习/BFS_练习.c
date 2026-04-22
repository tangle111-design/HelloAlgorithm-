#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define MAX_SIZE 100

typedef struct Vertex {
    int val;
} Vertex;

typedef struct AdjListNode {
    Vertex *vertex;
    struct AdjListNode *next;
} AdjListNode;

typedef struct GraphAdjList {
    Vertex *vertices[MAX_SIZE];
    AdjListNode *heads[MAX_SIZE];
    int size;
} GraphAdjList;

/* 节点队列结构体 */
typedef struct {
    Vertex *vertices[MAX_SIZE];
    int front, rear, size;
} Queue;

/* 构造函数 */
Queue *newQueue() {
    Queue *q = (Queue *)malloc(sizeof(Queue));
    q->front = q->rear = q->size = 0;
    return q;
}

/* 判断队列是否为空 */
int isEmpty(Queue *q) {
    return q->size == 0;
}

/* 入队操作 */
void enqueue(Queue *q, Vertex *vet) {
    q->vertices[q->rear] = vet;
    q->rear = (q->rear + 1) % MAX_SIZE;
    q->size++;
}

/* 出队操作 */
Vertex *dequeue(Queue *q) {
    Vertex *vet = q->vertices[q->front];
    q->front = (q->front + 1) % MAX_SIZE;
    q->size--;
    return vet;
}

/* 找到顶点在邻接表中的头节点 */
AdjListNode *findNode(GraphAdjList *graph, Vertex *vet) {
    for (int i = 0; i < graph->size; i++) {
        if (graph->vertices[i] == vet) {
            return graph->heads[i];
        }
    }
    return NULL;
}

/* 检查顶点是否已被访问 */
bool isVisited(Vertex **visited, int size, Vertex *vet) {
    for (int i = 0; i < size; i++) {
        if (visited[i] == vet) {
            return true;
        }
    }
    return false;
}

/* 广度优先遍历 */
void graphBFS(
    GraphAdjList *graph,
    Vertex *startVet,
    Vertex **res,
    int *resSize,
    Vertex **visited,
    int *visitedSize
) {
    Queue *queue = newQueue();

    // 步骤提示：
    // 1) 先把起点入队，并标记为已访问。
    // 2) 当队列非空时，循环执行：
    //    a. 弹出队首顶点，加入结果序列。
    //    b. 找到该顶点的邻接链表并遍历所有邻接点。
    //    c. 对每个未访问邻接点：入队 + 标记访问。
    // 3) 循环结束后释放队列内存。

    // TODO: 在这里补全 BFS 逻辑。

    free(queue);
}
