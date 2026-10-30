"""木の深さと部分木サイズ

対応: 13.10
計算量: 時間・領域 O(V)
原文: https://github.com/drken1215/book_algorithm_solution/blob/bf4af1b13b6fb1f58b8a921ab319096422f064d6/codes/chap13/code_13_9.cpp
"""

import sys


def tree_info(graph, root=0):
    depth = [0] * len(graph)
    subtree_size = [0] * len(graph)

    def dfs(v, parent=-1, d=0):
        depth[v] = d
        # 親へ戻る辺を除き、子の部分木を先に探索する。
        for child in graph[v]:
            if child != parent:
                dfs(child, v, d + 1)
        # 子の探索が終わってから、自分自身と各子の部分木の頂点数を合計する。
        subtree_size[v] = 1
        for child in graph[v]:
            if child != parent:
                subtree_size[v] += subtree_size[child]

    dfs(root)
    return depth, subtree_size


def main():
    it = iter(map(int, sys.stdin.buffer.read().split()))
    n = next(it)
    graph = [[] for _ in range(n)]
    for _ in range(n - 1):
        a, b = next(it), next(it)
        graph[a].append(b)
        graph[b].append(a)

    depth, subtree_size = tree_info(graph)
    for v in range(n):
        print(f"{v}: depth = {depth[v]}, subtree_size = {subtree_size[v]}")


if __name__ == "__main__":
    main()
