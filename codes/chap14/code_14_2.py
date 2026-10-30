"""ベルマン・フォード法

対応: 14.5
計算量: 時間 O(V(V+E))、領域 O(V+E)
原文: https://github.com/drken1215/book_algorithm_solution/blob/bf4af1b13b6fb1f58b8a921ab319096422f064d6/codes/chap14/code_14_2.cpp
"""

import sys
from math import inf


def bellman_ford(graph, start):
    n = len(graph)
    dist = [inf] * n
    dist[start] = 0
    negative_cycle = False
    for iteration in range(n):
        updated = False
        for v in range(n):
            # 始点からまだ到達できていない頂点からは緩和しない。
            if dist[v] == inf:
                continue
            for to, weight in graph[v]:
                if dist[to] > dist[v] + weight:
                    dist[to] = dist[v] + weight
                    updated = True
        # 一度も更新されなければ、これ以上短い経路は見つからない。
        if not updated:
            break
        # 頂点数と同じ回数だけ反復しても更新されるなら、
        # 始点から到達できる負閉路がある。
        if iteration == n - 1:
            negative_cycle = True
    # 始点から到達できる負閉路だけを検出する。
    return dist, negative_cycle


def main():
    it = iter(map(int, sys.stdin.buffer.read().split()))
    n, m, start = next(it), next(it), next(it)
    graph = [[] for _ in range(n)]
    for _ in range(m):
        a, b, w = next(it), next(it), next(it)
        graph[a].append((b, w))

    dist, negative_cycle = bellman_ford(graph, start)
    if negative_cycle:
        print("NEGATIVE CYCLE")
    else:
        for d in dist:
            print("INF" if d == inf else d)


if __name__ == "__main__":
    main()
