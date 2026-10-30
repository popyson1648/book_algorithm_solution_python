"""木の重み付き最大独立集合

対応: 18.2
計算量: 時間・領域 O(V)
原文: https://github.com/drken1215/book_algorithm_solution/blob/bf4af1b13b6fb1f58b8a921ab319096422f064d6/codes/chap18/code_18_1.cpp
"""

import sys


def maximum_weight_independent_set(graph, weights):
    dp1 = [0] * len(graph)  # 根を選ばない。
    dp2 = [0] * len(graph)  # 根を選ぶ。

    def dfs(v, parent=-1):
        for child in graph[v]:
            if child != parent:
                dfs(child, v)
        dp1[v], dp2[v] = 0, weights[v]
        for child in graph[v]:
            if child != parent:
                # 親を選ばない場合、各子は選ぶ・選ばないのうち重みの大きい方を使う。
                dp1[v] += max(dp1[child], dp2[child])
                # 親を選ぶ場合、隣接する子は選べない。
                dp2[v] += dp1[child]

    dfs(0)
    return max(dp1[0], dp2[0])


def main():
    it = iter(map(int, sys.stdin.buffer.read().split()))
    n = next(it)
    weights = [next(it) for _ in range(n)]
    graph = [[] for _ in range(n)]
    for _ in range(n - 1):
        a, b = next(it), next(it)
        graph[a].append(b)
        graph[b].append(a)

    print(maximum_weight_independent_set(graph, weights))


if __name__ == "__main__":
    main()
