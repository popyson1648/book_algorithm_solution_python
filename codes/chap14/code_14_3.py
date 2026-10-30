"""ヒープを使わないダイクストラ法

対応: 14.6
計算量: 時間 O(V²+E)、領域 O(V+E)
原文: https://github.com/drken1215/book_algorithm_solution/blob/bf4af1b13b6fb1f58b8a921ab319096422f064d6/codes/chap14/code_14_3.cpp
"""

import sys
from math import inf


def dijkstra(graph, start):
    """すべての辺重みは非負。"""
    n = len(graph)
    used = [False] * n
    dist = [inf] * n
    dist[start] = 0
    for _ in range(n):
        # 未確定の頂点のうち、始点からの距離が最小のものを次に確定する。
        min_dist, min_v = inf, -1
        for v in range(n):
            if not used[v] and dist[v] < min_dist:
                min_dist, min_v = dist[v], v
        if min_v == -1:
            break
        for to, weight in graph[min_v]:
            dist[to] = min(dist[to], dist[min_v] + weight)
        used[min_v] = True
    return dist


def main():
    it = iter(map(int, sys.stdin.buffer.read().split()))
    n, m, start = next(it), next(it), next(it)
    graph = [[] for _ in range(n)]
    for _ in range(m):
        a, b, w = next(it), next(it), next(it)
        graph[a].append((b, w))

    dist = dijkstra(graph, start)
    for d in dist:
        print("INF" if d == inf else d)


if __name__ == "__main__":
    main()
