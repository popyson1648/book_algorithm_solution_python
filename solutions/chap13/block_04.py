"""BFSによる二部グラフ判定

対応: 章末問題13.3
計算量: 時間・領域 O(V+E)
原文: https://github.com/drken1215/book_algorithm_solution/blob/bf4af1b13b6fb1f58b8a921ab319096422f064d6/solutions/chap13.md
"""

import sys
from collections import deque


def is_bipartite(graph):
    color = [-1] * len(graph)
    result = True
    # すべての連結成分で、隣接する頂点を異なる色にできるか調べる。
    for start in range(len(graph)):
        if color[start] != -1:
            continue
        color[start] = 0
        queue = deque([start])
        while queue:
            v = queue.popleft()
            for next_v in graph[v]:
                if color[next_v] != -1:
                    # 同じ色の頂点が隣接していれば、グラフ全体も二部グラフではない。
                    if color[next_v] == color[v]:
                        result = False
                    continue
                color[next_v] = 1 - color[v]
                queue.append(next_v)
    return result


def main():
    it = iter(map(int, sys.stdin.buffer.read().split()))
    n, m = next(it), next(it)
    graph = [[] for _ in range(n)]
    for _ in range(m):
        a, b = next(it), next(it)
        graph[a].append(b)
        graph[b].append(a)
    print("Yes" if is_bipartite(graph) else "No")


if __name__ == "__main__":
    main()
