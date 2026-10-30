"""葉から貪欲に選ぶ木の最大独立集合

対応: 章末問題18.1
計算量: 時間・領域 O(V)
原文: https://github.com/drken1215/book_algorithm_solution/blob/bf4af1b13b6fb1f58b8a921ab319096422f064d6/solutions/chap18.md
"""

import sys


def maximum_independent_set(graph):
    used = [False] * len(graph)

    def rec(v, parent=-1):
        exist = False
        for child in graph[v]:
            if child == parent:
                continue
            rec(child, v)
            if used[child]:
                exist = True
        # 子の選択を先に決め、選ばれた子がなければこの頂点を選ぶ。
        if not exist:
            used[v] = True

    rec(0)
    return sum(used)


def main():
    it = iter(map(int, sys.stdin.buffer.read().split()))
    n = next(it)
    graph = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = next(it) - 1, next(it) - 1
        graph[u].append(v)
        graph[v].append(u)
    print(maximum_independent_set(graph))


if __name__ == "__main__":
    main()
