from __future__ import annotations

from collections import deque
from dataclasses import dataclass


@dataclass(frozen=True)
class Vertex:
    val: int


class GraphAdjList:
    """无向图邻接表表示。"""

    def __init__(self) -> None:
        self.adj_list: dict[Vertex, list[Vertex]] = {}

    def add_vertex(self, vet: Vertex) -> None:
        if vet not in self.adj_list:
            self.adj_list[vet] = []

    def add_edge(self, vet1: Vertex, vet2: Vertex) -> None:
        if vet1 == vet2:
            raise ValueError("不允许自环")
        self.add_vertex(vet1)
        self.add_vertex(vet2)
        self.adj_list[vet1].append(vet2)
        self.adj_list[vet2].append(vet1)


def graph_bfs(graph: GraphAdjList, start_vet: Vertex) -> list[Vertex]:
    """广度优先遍历练习。"""
    res: list[Vertex] = []
    visited: set[Vertex] = set()
    que: deque[Vertex] = deque()

    # 步骤提示：
    # 1) 把起点加入 visited 和队列。
    # 2) 循环直到队列为空：
    #    a. 队首出队，记录到 res。
    #    b. 遍历它的所有邻接点。
    #    c. 对未访问邻接点执行“标记访问 + 入队”。
    # 3) 返回遍历结果 res。

    # TODO: 在这里补全 BFS 主循环。

    return res
