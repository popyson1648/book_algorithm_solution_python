"""すべての最小全域木に必要な辺

対応: 章末問題15.3
計算量: 時間 O(E log(E+1)+V(V+Eα(V)))、領域 O(V+E)
原文: https://github.com/drken1215/book_algorithm_solution/blob/bf4af1b13b6fb1f58b8a921ab319096422f064d6/solutions/chap15.md
"""

import sys
from math import inf


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


def necessary_edges(n, edges):
    """入力は連結無向グラフ。edgesは(重み,u,v)。"""
    edges = sorted(edges)

    def calc(excluded=-1):
        cost = 0
        selected = []
        uf = UnionFind(n)
        for i, (weight, u, v) in enumerate(edges):
            if i == excluded or uf.is_same(u, v):
                continue
            selected.append(i)
            cost += weight
            uf.merge(u, v)
        # 全域木に必要な辺数に届かなければ、連結にできない。
        if len(selected) < n - 1:
            return inf, selected
        return cost, selected

    base, mst = calc()
    count = total = 0
    # 最小全域木の各辺を1本ずつ除き、同じ重みの全域木を作れるか調べる。
    for edge_id in mst:
        cost, _ = calc(edge_id)
        # 除くと最小コストが増えるか非連結になる辺は、どの最小全域木にも必要。
        if cost > base:
            count += 1
            total += edges[edge_id][0]
    return count, total


def main():
    it = iter(map(int, sys.stdin.buffer.read().split()))
    n, m = next(it), next(it)
    edges = []
    for _ in range(m):
        u, v, w = next(it), next(it), next(it)
        edges.append((w, u - 1, v - 1))
    print(*necessary_edges(n, edges))


if __name__ == "__main__":
    main()
