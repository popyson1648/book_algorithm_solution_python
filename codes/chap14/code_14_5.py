"""フロイド・ワーシャル法

対応: 14.7
計算量: 時間 O(V³+E)、領域 O(V²)
原文: https://github.com/drken1215/book_algorithm_solution/blob/bf4af1b13b6fb1f58b8a921ab319096422f064d6/codes/chap14/code_14_5.cpp
"""

import sys
from math import inf


def floyd_warshall(n, edges):
    dp = [[inf] * n for _ in range(n)]
    for v in range(n):
        dp[v][v] = 0
    for a, b, weight in edges:
        # 多重辺の最小値と負の自己ループも保つ。
        dp[a][b] = min(dp[a][b], weight)
    # 途中で通ってよい頂点を1つずつ増やし、kを経由する場合と比べる。
    for k in range(n):
        for i in range(n):
            if dp[i][k] == inf:
                continue
            for j in range(n):
                if dp[k][j] == inf:
                    continue
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
    # 自分自身に戻る経路の重みが負なら、負閉路が存在する。
    return dp, any(dp[v][v] < 0 for v in range(n))


def main():
    it = iter(map(int, sys.stdin.buffer.read().split()))
    n, m = next(it), next(it)
    edges = [(next(it), next(it), next(it)) for _ in range(m)]
    dp, negative_cycle = floyd_warshall(n, edges)
    if negative_cycle:
        print("NEGATIVE CYCLE")
    else:
        for row in dp:
            print(" ".join("INF" if d == inf else str(d) for d in row))


if __name__ == "__main__":
    main()
