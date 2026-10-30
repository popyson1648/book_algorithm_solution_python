"""union by sizeと経路圧縮

対応: 11.6
計算量: 初期化 O(N)、操作あたり償却 O(α(N))、領域 O(N)
原文: https://github.com/drken1215/book_algorithm_solution/blob/bf4af1b13b6fb1f58b8a921ab319096422f064d6/codes/chap11/code_11_3.cpp
"""

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


def main():
    uf = UnionFind(7)
    uf.unite(1, 2)
    uf.unite(2, 3)
    uf.unite(5, 6)
    print(int(uf.is_same(1, 3)))
    print(int(uf.is_same(2, 5)))
    uf.unite(1, 6)
    print(int(uf.is_same(2, 5)))


if __name__ == "__main__":
    main()
