"""フォード・ファルカーソン法

対応: 16.4
計算量: 整数容量で時間 O((V+E)(F+1))、領域 O(V+E)。Fは最大流量
原文: https://github.com/drken1215/book_algorithm_solution/blob/bf4af1b13b6fb1f58b8a921ab319096422f064d6/codes/chap16/code_16_1.cpp
"""

import sys


class Edge:
    def __init__(self, rev, source, to, cap):
        self.rev = rev
        self.source = source
        self.to = to
        self.cap = cap


class Graph:
    def __init__(self, n):
        self.adj = [[] for _ in range(n)]

    def __len__(self):
        return len(self.adj)

    def __getitem__(self, i):
        return self.adj[i]

    def reverse_edge(self, edge):
        return self.adj[edge.to][edge.rev]

    def run_flow(self, edge, flow):
        # 流した分だけ順方向の残余容量を減らし、逆方向の残余容量を増やす。
        edge.cap -= flow
        self.reverse_edge(edge).cap += flow

    def add_edge(self, source, to, cap):
        if cap < 0:
            raise ValueError("容量は非負整数にしてください")
        source_rev = len(self.adj[source])
        to_rev = len(self.adj[to]) + (source == to)
        self.adj[source].append(Edge(to_rev, source, to, cap))
        # 流れを後から取り消せるように、初期容量0の逆辺も用意する。
        self.adj[to].append(Edge(source_rev, to, source, 0))


class FordFulkerson:
    def dfs(self, graph, v, target, flow):
        if v == target:
            return flow
        self.seen[v] = True
        for edge in graph[v]:
            if self.seen[edge.to] or edge.cap == 0:
                continue
            # この経路に流せる量は、経路上の残余容量の最小値まで。
            sent = self.dfs(graph, edge.to, target, min(flow, edge.cap))
            if sent == 0:
                continue
            graph.run_flow(edge, sent)
            return sent
        return 0

    def solve(self, graph, start, target):
        """graphを残余グラフへ更新する。容量は非負整数。"""
        if start == target:
            raise ValueError("始点と終点は別の頂点にしてください")
        result = 0
        # 始点から出る容量の合計を流量の上限とする。
        upper_bound = sum(edge.cap for edge in graph[start])
        while True:
            self.seen = [False] * len(graph)
            flow = self.dfs(graph, start, target, upper_bound)
            # 残余グラフに始点から終点への経路がなくなれば、最大流に達している。
            if flow == 0:
                return result
            result += flow


def main():
    it = iter(map(int, sys.stdin.buffer.read().split()))
    n, m = next(it), next(it)
    graph = Graph(n)
    for _ in range(m):
        u, v, cap = next(it), next(it), next(it)
        graph.add_edge(u, v, cap)
    print(FordFulkerson().solve(graph, 0, n - 1))


if __name__ == "__main__":
    main()
