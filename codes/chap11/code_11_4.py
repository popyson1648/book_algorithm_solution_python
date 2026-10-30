"""連結成分の個数

対応: 11.7
計算量: 時間 O(V+Eα(V))、領域 O(V)
原文: https://github.com/drken1215/book_algorithm_solution/blob/bf4af1b13b6fb1f58b8a921ab319096422f064d6/codes/chap11/code_11_4.cpp
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


def count_components(n, edges):
    uf = UnionFind(n)
    for a, b in edges:
        uf.unite(a, b)
    result = 0
    # 各グループには根が1つずつあるので、根の個数を数える。
    for x in range(n):
        if uf.root(x) == x:
            result += 1
    return result


def main():
    it = iter(map(int, sys.stdin.buffer.read().split()))
    n, m = next(it), next(it)
    print(count_components(n, [(next(it), next(it)) for _ in range(m)]))


if __name__ == "__main__":
    main()
