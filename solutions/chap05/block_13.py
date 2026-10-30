"""Slimes：短い区間から解くDP

対応: 章末問題5.9
計算量: 時間 O(N³)、領域 O(N²)
原文: https://github.com/drken1215/book_algorithm_solution/blob/bf4af1b13b6fb1f58b8a921ab319096422f064d6/solutions/chap05.md
"""

import sys
from math import inf


def slime_cost(a):
    n = len(a)
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + a[i]
    dp = [[inf] * (n + 1) for _ in range(n + 1)]
    for i in range(n):
        dp[i][i + 1] = 0
    # 短い区間から解き、左右の区間の最小コストを使えるようにする。
    for width in range(2, n + 1):
        for i in range(n - width + 1):
            j = i + width
            # 最後の結合位置を試し、左右のコストに区間全体の大きさを加える。
            for k in range(i + 1, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + prefix[j] - prefix[i])
    return dp[0][n]


def main():
    it = iter(map(int, sys.stdin.buffer.read().split()))
    n = next(it)
    a = [next(it) for _ in range(n)]
    print(slime_cost(a))


if __name__ == "__main__":
    main()
