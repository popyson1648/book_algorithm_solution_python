"""DFSの帰りがけ順によるトポロジカルソート

対応: 13.9
計算量: 時間 O(V+E)、領域 O(V+E)
原文: https://github.com/drken1215/book_algorithm_solution/blob/bf4af1b13b6fb1f58b8a921ab319096422f064d6/codes/chap13/code_13_6.cpp
"""

import sys


def topological_sort(graph):
    """入力はDAG（有向非巡回グラフ）。閉路は検出しない。"""
    seen = [False] * len(graph)
    order = []

    def rec(v):
        seen[v] = True
        for next_v in graph[v]:
            if not seen[next_v]:
                rec(next_v)
        # 行き先の探索がすべて終わった帰りがけに記録する。
        order.append(v)

    for v in range(len(graph)):
        if not seen[v]:
            rec(v)
    # 帰りがけ順を逆にすると、各辺の始点が終点より前に並ぶ。
    order.reverse()
    return order


def main():
    it = iter(map(int, sys.stdin.buffer.read().split()))
    n, m = next(it), next(it)
    graph = [[] for _ in range(n)]
    for _ in range(m):
        a, b = next(it), next(it)
        graph[a].append(b)

    for v in topological_sort(graph):
        print(v, end=" -> ")
    print()


if __name__ == "__main__":
    main()
