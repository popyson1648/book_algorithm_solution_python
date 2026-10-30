"""木の独立集合の数え上げ

対応: 章末問題18.2
計算量: 時間・領域 O(V)
原文: https://github.com/drken1215/book_algorithm_solution/blob/bf4af1b13b6fb1f58b8a921ab319096422f064d6/solutions/chap18.md
"""

import sys


MOD = 1000000007


def count_independent_sets(graph):
    # 各部分木で、根を選ばない場合と選ぶ場合の独立集合の個数を記録する。
    dp1 = [1] * len(graph)
    dp2 = [1] * len(graph)

    def rec(v, parent=-1):
        for child in graph[v]:
            if child != parent:
                rec(child, v)
        for child in graph[v]:
            if child != parent:
                # 親を選ばない場合、子は選ぶ・選ばないの両方を数えられる。
                dp1[v] = dp1[v] * (dp1[child] + dp2[child]) % MOD
                # 親を選ぶ場合、子は選べない。子の部分木どうしの選び方は掛け合わせる。
                dp2[v] = dp2[v] * dp1[child] % MOD

    rec(0)
    return (dp1[0] + dp2[0]) % MOD


def main():
    it = iter(map(int, sys.stdin.buffer.read().split()))
    n = next(it)
    graph = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = next(it) - 1, next(it) - 1
        graph[u].append(v)
        graph[v].append(u)
    print(count_independent_sets(graph))


if __name__ == "__main__":
    main()
