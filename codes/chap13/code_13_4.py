"""有向グラフのs-t到達可能性

対応: 13.7
計算量: 時間 O(V+E)、領域 O(V+E)
原文: https://github.com/drken1215/book_algorithm_solution/blob/bf4af1b13b6fb1f58b8a921ab319096422f064d6/codes/chap13/code_13_4.cpp
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
    n, m, start, target = next(it), next(it), next(it), next(it)
    graph = [[] for _ in range(n)]
    for _ in range(m):
        a, b = next(it), next(it)
        graph[a].append(b)

    seen = [False] * n
    dfs(graph, start, seen)
    print("Yes" if seen[target] else "No")


if __name__ == "__main__":
    main()
