"""ヒープを使うダイクストラ法

対応: 14.6
計算量: 時間 O(V+E log(E+1))、領域 O(V+E)
原文: https://github.com/drken1215/book_algorithm_solution/blob/bf4af1b13b6fb1f58b8a921ab319096422f064d6/codes/chap14/code_14_4.cpp
"""

import sys
from heapq import heappop, heappush
from math import inf


def dijkstra(graph, start):
    """すべての辺重みは非負。heapq は最小ヒープ。"""
    dist = [inf] * len(graph)
    dist[start] = 0
    queue = [(0, start)]
    while queue:
        # ヒープから距離が最小の候補を取り出す。
        d, v = heappop(queue)
        if d > dist[v]:  # 以前の距離を持つ古いエントリ。
            continue
        for to, weight in graph[v]:
            candidate = dist[v] + weight
            if candidate < dist[to]:
                dist[to] = candidate
                heappush(queue, (candidate, to))
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
