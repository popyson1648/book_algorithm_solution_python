"""クラスカル法

対応: 15.3
計算量: 時間 O(V+E log(E+1))、領域 O(V+E)
原文: https://github.com/drken1215/book_algorithm_solution/blob/bf4af1b13b6fb1f58b8a921ab319096422f064d6/codes/chap15/code_15_1.cpp
"""

import sys


class UnionFind:
    def __init__(self, n):
        self.par = [-1] * n
        self.siz = [1] * n

    def root(self, x):
        if self.par[x] == -1:
            return x
        # 経路圧縮：親を直接根につなぎ直し、次回以降の探索を短くする。
        self.par[x] = self.root(self.par[x])
        return self.par[x]

    def is_same(self, x, y):
        return self.root(x) == self.root(y)

    def unite(self, x, y):
        x, y = self.root(x), self.root(y)
        if x == y:
            return False
        # 小さい木を大きい木に付ける。
        if self.siz[x] < self.siz[y]:
            x, y = y, x
        self.par[y] = x
        self.siz[x] += self.siz[y]
        return True

    def size(self, x):
        return self.siz[self.root(x)]


def kruskal(n, edges):
    """edges は (重み, u, v)。非連結なら最小全域森の重みを返す。"""
    result = 0
    uf = UnionFind(n)
    # 重みの小さい辺から、異なる連結成分どうしをつなぐ。
    for weight, u, v in sorted(edges):
        # 両端がすでにつながっている辺を加えると閉路ができるため、採用しない。
        if uf.is_same(u, v):
            continue
        result += weight
        uf.unite(u, v)
    return result


def main():
    it = iter(map(int, sys.stdin.buffer.read().split()))
    n, m = next(it), next(it)
    edges = []
    for _ in range(m):
        u, v, w = next(it), next(it), next(it)
        edges.append((w, u, v))
    print(kruskal(n, edges))


if __name__ == "__main__":
    main()
