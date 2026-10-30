"""BFSによる無向グラフのs-t到達判定

対応: 章末問題13.2
計算量: 時間・領域 O(V+E)
原文: https://github.com/drken1215/book_algorithm_solution/blob/bf4af1b13b6fb1f58b8a921ab319096422f064d6/solutions/chap13.md
"""

import sys
from collections import deque


def bfs(graph, start):
    # 始点からの最短距離を記録する。-1はまだ到達していない頂点を表す。
    dist = [-1] * len(graph)
    dist[start] = 0
    queue = deque([start])
    while queue:
        v = queue.popleft()
        for x in graph[v]:
            if dist[x] != -1:
                continue
            # 近い頂点から探索するため、初めて発見したときの距離が最短になる。
            dist[x] = dist[v] + 1
            queue.append(x)
    return dist


def main():
    it = iter(map(int, sys.stdin.buffer.read().split()))
    n, m, start, target = next(it), next(it), next(it), next(it)
    graph = [[] for _ in range(n)]
    for _ in range(m):
        a, b = next(it), next(it)
        graph[a].append(b)
        graph[b].append(a)
    print("Yes" if bfs(graph, start)[target] != -1 else "No")


if __name__ == "__main__":
    main()
