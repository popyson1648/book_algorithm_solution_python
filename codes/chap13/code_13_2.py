"""再帰DFSの基本形

対応: 13.3
計算量: 時間 O(V+E)、領域 O(V+E)
原文: https://github.com/drken1215/book_algorithm_solution/blob/bf4af1b13b6fb1f58b8a921ab319096422f064d6/codes/chap13/code_13_2.cpp
"""

import sys


def dfs(graph, v, seen):
    # 先に訪問済みにし、閉路があっても同じ頂点を繰り返し探索しない。
    seen[v] = True
    for next_v in graph[v]:
        if seen[next_v]:
            continue
        dfs(graph, next_v, seen)


def main():
    it = iter(map(int, sys.stdin.buffer.read().split()))
    n, m = next(it), next(it)
    graph = [[] for _ in range(n)]
    for _ in range(m):
        a, b = next(it), next(it)
        graph[a].append(b)

    seen = [False] * n
    for v in range(n):
        if not seen[v]:
            dfs(graph, v, seen)


if __name__ == "__main__":
    main()
