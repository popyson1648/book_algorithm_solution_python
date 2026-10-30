"""最小全域木の辺重みのメディアン

対応: 章末問題15.2
計算量: 時間 O(V+E log(E+1))、領域 O(V+E)
原文: https://github.com/drken1215/book_algorithm_solution/blob/bf4af1b13b6fb1f58b8a921ab319096422f064d6/solutions/chap15.md
"""

import sys


class UnionFind:
    def __init__(self, n=0):
        self.init(n)

    def init(self, n):
        # 根には負のサイズ、その他には親番号を記録する。
        self.par = [-1] * n

    def root(self, x):
        if self.par[x] < 0:
            return x
        # 経路圧縮：親を直接根につなぎ直し、次回以降の探索を短くする。
        self.par[x] = self.root(self.par[x])
        return self.par[x]

    def is_same(self, x, y):
        return self.root(x) == self.root(y)

    def merge(self, x, y):
        x, y = self.root(x), self.root(y)
        if x == y:
            return False
        if self.par[x] > self.par[y]:
            x, y = y, x
        self.par[x] += self.par[y]
        self.par[y] = x
        return True

    def size(self, x):
        return -self.par[self.root(x)]


def median_tree(n, edges):
    uf = UnionFind(n)
    count = 0
    result = 0
    for weight, u, v in sorted(edges):
        if uf.is_same(u, v):
            continue
        uf.merge(u, v)
        count += 1
        # 採用する辺を重み順に数え、中央値の位置に達したら終了する。
        if count == (n + 1) // 2:
            result = weight
            break
    return result


def main():
    it = iter(map(int, sys.stdin.buffer.read().split()))
    while True:
        n, m = next(it), next(it)
        if n == 0:
            break
        edges = []
        for _ in range(m):
            u, v, w = next(it), next(it), next(it)
            edges.append((w, u - 1, v - 1))
        print(median_tree(n, edges))


if __name__ == "__main__":
    main()
