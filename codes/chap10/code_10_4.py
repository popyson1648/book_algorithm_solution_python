"""重み付きグラフの隣接リスト

対応: 10.4
計算量: 時間・領域 O(V+E)
原文: https://github.com/drken1215/book_algorithm_solution/blob/bf4af1b13b6fb1f58b8a921ab319096422f064d6/codes/chap10/code_10_4.cpp
"""

import sys


class Edge:
    def __init__(self, to, w):
        self.to = to
        self.w = w


def build_graph(n, edges):
    graph = [[] for _ in range(n)]
    for a, b, w in edges:
        graph[a].append(Edge(b, w))
    return graph


def main():
    it = iter(map(int, sys.stdin.buffer.read().split()))
    n, m = next(it), next(it)
    build_graph(n, [(next(it), next(it), next(it)) for _ in range(m)])


if __name__ == "__main__":
    main()
