"""再帰DFSによる二部グラフ判定

対応: 13.8
計算量: 時間 O(V+E)、領域 O(V+E)
原文: https://github.com/drken1215/book_algorithm_solution/blob/bf4af1b13b6fb1f58b8a921ab319096422f064d6/codes/chap13/code_13_5.cpp
"""

import sys


def dfs(graph, v, color, current=0):
    color[v] = current
    for next_v in graph[v]:
        if color[next_v] != -1:
            # 同じ色の頂点が隣接していれば、2色で塗り分けられない。
            if color[next_v] == current:
                return False
            continue
        if not dfs(graph, next_v, color, 1 - current):
            return False
    return True


def is_bipartite(graph):
    color = [-1] * len(graph)
    result = True
    # グラフが分かれていても、すべての連結成分を調べる。
    for v in range(len(graph)):
        if color[v] != -1:
            continue
        if not dfs(graph, v, color):
            result = False
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
